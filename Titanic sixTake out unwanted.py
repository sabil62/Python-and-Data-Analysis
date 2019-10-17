import pandas as pd

dataset = pd.read_csv('Titanic.csv')
wrangled = dataset[pd.notnull(dataset['Age'])]

#Group by age + count() garera jun ma less than 5 passenger cha teslai hatakao 
group_by_Age = wrangled.groupby('Age',as_index=False)
total_Passengers_by_Age = group_by_Age['PassengerId'].count()
count_Age_grt_5 = total_Passengers_by_Age[total_Passengers_by_Age['PassengerId']>5]

#List is needed to convert the data without less than 5 data
age_gt5_list = count_Age_grt_5['Age'].values.tolist()

#final dataframe where less than 5 data is eliminated
age_gt5_df = wrangled[wrangled['Age'].isin(age_gt5_list)]

''' See the difference '''
print(wrangled['PassengerId'].count())
print('vs')
print(age_gt5_df['PassengerId'].count())