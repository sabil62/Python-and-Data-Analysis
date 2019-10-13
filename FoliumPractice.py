# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:21:39 2019

@author: User
"""

#SORTED VALUES FUCTION
a=[100,200,1,3,4,2,7,5,6,700]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#In a dictionary
b={'name':['aman','bman','cman'],
   'age':[20,25,18],
   'roll':[12,18,19]}
c=b.loc[:,'age']
d=c.sort_values()
print(d)