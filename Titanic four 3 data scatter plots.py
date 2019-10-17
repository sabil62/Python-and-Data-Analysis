'''This is not 3 data scatter plot , titanic five is real one'''
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('Titanic.csv')

wrangle=dataset[pd.notnull(dataset['Age'])]

wrangle_grouped=wrangle.groupby('Survived')

wrangle['Age'].plot.hist()
plt.show()

plt.figure()
survived=wrangle_grouped['Age']
survived.plot.hist()
plt.legend()
plt.show()
print(wrangle_grouped['Age'].mean())
