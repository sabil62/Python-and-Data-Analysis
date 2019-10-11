# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:52:02 2019

@author: User
"""
import pandas as pd

left=pd.DataFrame({'teams':['Nepal','India','Bhutan','Srilanka'],
                   'rank':[1,3,5,7],
                   'division':[1,5,4,3]})
right=pd.DataFrame({'teams':['Nepal','India','Pakistan','Maledives'],
                    'rank':[1,3,4,8],
                    'division':[1,5,1,2]})

#concatenate
a=pd.concat([left,right])
print(a)

#Merge and join
b=pd.merge(left,right,on='teams')
print(b)
print('------------------------------------------------------------------')

#inner join (same as orginal merge)
c=pd.merge(left,right,on='teams',how='inner')
print(c)
print('------------------------------------------------------------------')

#left join
d=pd.merge(left,right,on='teams',how='left')
print(d)
print('------------------------------------------------------------------')

#right join
e=pd.merge(left,right,on='teams',how='right')
print(e)
print('------------------------------------------------------------------')

#outer join
f=pd.merge(left,right,on='teams',how='outer')
print(f)
print('------------------------------------------------------------------')
#here on is for all the column heads (compare above and below outer joins)
f=pd.merge(left,right,on=['teams','rank','division'],how='outer')
print(f)
print('------------------------------------------------------------------')

