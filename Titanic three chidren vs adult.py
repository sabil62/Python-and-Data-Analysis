import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Titanic.csv')
#Wrangle
age_wrangle = dataset[pd.notnull(dataset['Age'])]
            #print(age_wrangle.isnull().sum())

#CHILDREN
child=age_wrangle[age_wrangle['Age']<20]
            #print(child.count())
child_survived = child['Survived'].sum()
child_total = child['PassengerId'].count()#basically we just want to COUNT the no of passenger so we used passengerId anything could be done
            #print(child_total)

#ADULT
adult = age_wrangle[age_wrangle['Age'] >= 20]
adult_survived = adult['Survived'].sum()
adult_total = adult['PassengerId'].count()

'''VVVVVVV I  S E C T I O N
Here the given datas are in 1d   like print(adult_survived or child_survived etc so we have to 
convert to a 2d model or dataframe inorder to use the plot that we have been doing df.plot.bar() wala plot'''

#Converting to a dataframe
Dataframe_conversion = pd.DataFrame({'Survived':[child_survived,adult_survived],
                                     'Total':[child_total,adult_total]},index=['child','adult'])
'''if you are finding it difficult to understand dataframe dictionary(above) then:
    basically, think (Survived and Total) which is enclosed in colon as COLUMNS TITLE,
    the data you entered inside survive.. is gradually converted to colons
    that is why i have printed the result below( print(Dataframe_conversion) )'''
print(Dataframe_conversion)

#Ploting in graph
Dataframe_conversion.plot.bar()     #you can use color by .bar(color=['red','green'])
plt.ylabel('no of people')
plt.show()
            




