import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Titanic.csv')
        #print(dataset.isnull().sum())

wrangle_fare = dataset[pd.notnull(dataset['Fare'])]
        #print(wrangle_fare.isnull().sum())
 
#separting classes by fare       
class_A = wrangle_fare[wrangle_fare['Fare']<20]
class_B = wrangle_fare[(wrangle_fare['Fare']>20) & (wrangle_fare['Fare']<50)]
class_C = wrangle_fare[wrangle_fare['Fare'].between(50,100)]

#survivor group
survivor_A = class_A['Survived'].mean()
survivor_B = class_B['Survived'].mean()
survivor_C = class_C['Survived'].mean()

#converting to a Dataframe because these are independent value
final_df = pd.DataFrame({'Survivors':[survivor_A,survivor_B,survivor_C]},
                         index=['POOR ','MID CLASS','RICH'])

final_df.plot.bar()
plt.show()

print('This clearly shows richer class has higher survival rate')