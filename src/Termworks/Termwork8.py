# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# pandas
# ...............................................................

import pandas as pd
import numpy as np 

data=pd.read_csv('X:\\Python\\src\\Termworks\\tw8.csv')
column=list(data.columns)
print('The Given Colums are :-')
for i in column:
    print(i)
x=input("Enter the column name-> ")
print(f"Unique values in {x} are-> ")
uniqueValues=np.unique(data[x])
print(uniqueValues)
col_data=list(data[x])
print('frequency of occurance')
for i in uniqueValues:
    print(i,'appears',col_data.count(i))
print('Total no of record in data frame is',len(col_data))