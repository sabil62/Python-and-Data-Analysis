import pandas as pd
import matplotlib.pyplot as plt

Dataset=pd.read_csv('1000 Sales Records.csv')

#print(Dataset.head(10))
#pd.set_option('display_max_columns',10)
#print(Dataset.describe())

#find the list of units sold greater than 9600
get_columns=Dataset.loc[:,['Units Sold','Region']]
                    #print(Dataset['Region'])=>worked
for i in get_columns.itertuples():
    if i[1]>9600:   #i[2] not supported as it is Region(a string)
        print(i)
        
#print(Dataset.describe())

#WAP to find relation between units sold and profit
get_columns2=Dataset.loc[:,['Units Sold','Total Profit']]
                    #print(get_columns2['Total Profit'])
x=list(get_columns2['Units Sold'])
y=list(get_columns2['Total Profit'])
plt.scatter(x,y)    
plt.xlabel('units sold',fontsize=32)
plt.show()

#WAP to show top 10 profits through a piechart
get_columns_profit=Dataset.loc[:,['Region','Total Profit']]
arrange_columns=get_columns_profit.sort_values(by='Total Profit',ascending=False)
top_ten_profits=arrange_columns[:10]
plt.pie(top_ten_profits['Total Profit'],labels=top_ten_profits['Region'])
plt.show()

