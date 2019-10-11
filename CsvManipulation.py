

import pandas as pd

Dataset=pd.read_csv('1000 Sales Records.csv')

#shape functions for no of rows and column
print(Dataset.shape)    #prints(1000,14) means 1000rows and 14 colums

#Describe() VVI function
print(Dataset.describe())

#head() function 
# print(Dataset.head())  or print(Dataset.head(10))

#tail() function
#print(Dataset.tail(10))  prints from 

#sum function
print(Dataset.sum())

#std or standard deviation
print(Dataset.std())