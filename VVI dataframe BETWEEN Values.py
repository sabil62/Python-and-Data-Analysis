# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:31:07 2019

@author: User
"""


import pandas as pd

dataset=pd.read_csv('Titanic.csv')

wrangle=dataset[pd.notnull(dataset['Age'])]

count_age=wrangle[wrangle['Age']<16]
print(count_age['Age'])

count_age_B=wrangle[ (wrangle['Age']>16) & (wrangle['Age']<25)]
print(count_age_B['Age'])

count_age_C=wrangle[wrangle['Age'].between(25,70)]
print(count_age_C['Age'])