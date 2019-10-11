import pandas
import numpy as np

#comparing between numpy and panda with series
arr=np.array([1,2,3,4])
print(arr)
brr=pandas.Series(arr)   #series gives indexes
print(brr)

#Giving index to a series panda
crr=pandas.Series(arr,index=['one','two','three','four'])
print(crr)

#for 2D data USING  D A T A F R A M E
drr=pandas.DataFrame(arr)
print(drr)      #a 0 appears above

#MAKING A 2D MATRIX WITH ROW AND COLUMN INDEX
weather_events={
    'day__': ['Sun','Mond','Tues','Wed'],
    '__weather': ['rainy','windy','chilly','sunny'],
    'temperature': [20,30,25,35]
}
twoD=pandas.DataFrame(weather_events)
print(twoD)                           #this creates table like structure but there is index 0 1 2 3 only

#MAKING BOTH ROW AND COLUMN INDEXES
#same weather events
weather_eve={
    '___day_':['sun','mon','tues','wed'],
    '_weather_':['sunny','windy','chilly','rainy'],
    'temperature':[20,21,22,26]
}
weateven=pandas.DataFrame(weather_eve,index=['one__','two__','three','four_'])
print(weateven)
