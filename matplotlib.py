# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 22:15:24 2019

@author: User
"""

import matplotlib.pyplot as plt
x= [0,1,2,3,4,5,6]
y= [i**2 for i in x]
z= [i**3 for i in x]
plt.plot(x,y,'r',label='square')
plt.plot(x,z,':',label='cubic')
plt.legend()

#this is just to show axes comment this out
plt.xlim(-1,7)
plt.ylim(-50,300)
plt.show()
print (y)