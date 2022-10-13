from tokenize import group
from turtle import clear
from scipy import stats
import pandas as pd
from pandas import DataFrame as df

data = pd.read_csv("data.csv")
print(data)

# remove lines with missing values
data.dropna(inplace=True) # inplace=True means the data frame will be changed
# with out it, the data frame will not be changed and you'll need to assign it to a new variable
# like this: data = data.dropna()
# you can tell python what are the missing values by adding the argument na_values=[...]
# like this: data = data.dropna(na_values=["?", "N/A"])
# you can also specify the columns you want to check for missing values
# like this: data = data.dropna(subset=["column1", "column2"])

# fill missing values with a specific value 
data.fillna(0, inplace=True) # fill missing values with 0

# you can tell the data frame to only use certain columns
data = data[['id', 'CA']]
print(data)

# divide CA column into three new series according to the id column
