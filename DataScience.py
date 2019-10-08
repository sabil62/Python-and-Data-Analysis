import numpy as np
a = [1, 2, 3]
b = np.array(a)
print(b)

# Arrange
c= np.arange(5,25)
print(c)              #prints 5 upto 24

#linspace
d=np.linspace(5,25,5)
print(d)               #print 5 10........25 5steps

#zeros
e=np.zeros(8)        #8 zeros
f=np.zeros((5,5))      #5*5 matrix zero
print(e)
print(f)

#reshape
g=np.zeros(8)
h=g.reshape((2,2,2))  #always make multiple of original(here 2*2*2=8
print(h)

#ravel
i=np.array([[1,2,3],[10000,2000,300]])
print(i)
j=i.ravel()
print(j)     #ravel flattens the matarix



