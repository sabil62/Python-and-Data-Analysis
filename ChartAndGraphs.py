# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:30:09 2019

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np

#for histogram
a=np.random.rand(4,2)
plt.hist(a) #this is histogram
plt.show()

#for bar graph
b=[2,4,6,8,10]
c=[120,80,95,150,130]
plt.bar(b,c)
plt.show()

#for other bar graph
d={'a':25,'b':45,'c':52}
for index,key in enumerate(d):
    plt.bar(index,d[key])
plt.show()

#for pie chart
plt.pie([10,20,25],labels=['city','town','villages'])
plt.show()

#scatter plot
x=[0,10,2,4,5,5,4,4,7,12,15,12,11,11,1,12,12,1,2,11,12,1,2,3,4,5,6,7,8,9],
y=[0,1,2,4,2,1,1,11,12,6,11,6,13,11,1,12,11,1,3,11,7,1,2,3,4,5,6,7,8,9],
plt.scatter(x,y)
plt.show()