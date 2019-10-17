import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Titanic.csv')

wrangled = dataset[pd.notnull(dataset['Age'])]

group_by_age = wrangled.groupby('Age',as_index=False)

age_mean_data = group_by_age.mean()

total_passengers_in_each_AgeGroup = group_by_age['PassengerId'].count()
            #print(total_passengers_in_each_AgeGroup) prints total pass in each age group

            #age_mean_datas_Age_list = age_mean_data['Age'].tolist()

'''Dont forget to do .tolist() in ['Age'] wala as it is responsible for groupby '''
scatter = plt.scatter(age_mean_data['Age'].tolist(),age_mean_data['Survived'],
                      s=50, alpha=1, c=total_passengers_in_each_AgeGroup['PassengerId'],
                      cmap='RdYlGn',vmin=0,vmax=30)
plt.colorbar(scatter, label = 'no of passengers')
plt.show()

print(total_passengers_in_each_AgeGroup)


