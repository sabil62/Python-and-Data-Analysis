''' For reln between no of survivor(male/female) and total people(male/female) '''
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Titanic.csv')
            #print(dataset.isnull().sum())

#wrangle the null ones
age_wrangle = dataset[pd.notnull(dataset['Age'])]
cabin_wrangle_df = age_wrangle[pd.notnull(age_wrangle['Cabin'])]
            #print(cabin_wrangle.isnull().sum())

#Group
group_by_gender = cabin_wrangle_df.groupby('Sex')
            #print(group_by_gender.sum())

#total passengers
total_passengers = group_by_gender['PassengerId'].count()

#survived passengers
survived_passengers = group_by_gender['Survived'].sum()
            #print(survived_passengers)

#New dataframe because we have to merge total and survived as they have separateley count and sum operations
combined_df=pd.merge(survived_passengers,total_passengers,how='inner',on='Sex')
#renaming passengerID to Total 
combined_df.columns=['Survived','Total']
            #print(combined_df)


#P L O T  B A R G R A P H]
combined_df.plot.bar(color=['red','orange'])
plt.ylabel('no of passengers')
plt.title('Relation between survived and total people GROUPED BY gender')
#plt.text(32,1,-0.2,-50)
plt.show()

#this is just to show difference between video and real
print(combined_df)
print(combined_df['Survived'].loc['male'])#this is wrong in video here.loc[0] isnt possible(down)
print(combined_df['Total'].loc['female'])#as the index here is male/female instead of tranditional 0 1
