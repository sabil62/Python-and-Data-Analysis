import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Titanic.csv')

#VVI SYNTAX FOR DISPLAYING ALL COLUMNS
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)

#print(dataset.describe())

#NOW IS THE MAIN PART 
#print(dataset.isnull().sum()) this is for checking

age_wrangled=dataset[pd.notnull(dataset['Age'])]
#print(age_wrangled.isnull().sum())
cabin_wrangled=age_wrangled[pd.notnull(age_wrangled['Cabin'])]
#print(cabin_wrangled.isnull().sum())

group_by_gender=cabin_wrangled.groupby('Sex')
parent_vs_siblings=group_by_gender[['Parch','SibSp']]

final_mean=parent_vs_siblings.sum()
final_sum=parent_vs_siblings.mean()
final_mean.plot.bar()
final_sum.plot.bar(color=['red','green'])
plt.show()


print('This shows In both male and female, siblings are likely to be saved more then parent')