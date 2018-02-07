
# coding: utf-8

# In[6]:


'''
Pandas
* Extinsively used in Data Science
* Dataframe= Important data structure thar represents data in tabular format
* Dataframe= Main object of Pandas 
'''


#creating dataframe 

import pandas as pd

#csv stands for comma seperated values
df=pd.read_csv("SampleCSVFile_2kb.csv") #loading data to data frame
print(df)

#data can also be loaded from list of tuples
print(df.shape)  #gives rowsand cols
print(df.head())    #gives first 5 rows by default
print(df.tail())    #gives last 5 rows by default
# head, tail borrowed from UNIX commands

#slicing data
print(df[2:5])    #data from 2nd row till 4th row 
print(df.columns)   #list of all columns

print(df['col_name'])   #gives a new data frame with just 1 col
#same as df.col_name

print(df[['col_name_1','col_name_2']])
# gives a new data frame for 2 or more cols

df['col_name'].min()
df['col_name'].max()
df['col_name'].describe() #gives min,max,count of entire col
#Also gives mean,std, 25%, 50%, 75% of entire col

df[df.col_name==df.col_name.max()]
#selects entire row for which col_name has max value of col_name

df.day[df.col_name==df.col_name.max()]
#gives only the day value of the row with max temperature 




