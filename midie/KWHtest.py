from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import statsmodels.api as sm
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")
# print(data)

# DataFrame be like:
#    \  Column  ...
# index     0   ...
# index+1   1   ...
# ...       ... ...
# each column is a series
# like a 2-dim array but with tags

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
data = data[['group', 'CA']]
# print(data)

group = [[],[],[]]
# divide CA column into three new series according to the id column
for i in range (0, data['group'].size): 
    # range (0, data['group'].size) means from 0 to the size of the column - 1
    if data['group'][i] == 1:
        group[0].append(data['CA'][i])
    elif data['group'][i] == 2:
        group[1].append(data['CA'][i]) 
    elif data['group'][i] == 3:
        group[2].append(data['CA'][i])
    else:
        print("Error: group id not found")
        
print(group)

# describeBy + summary
for g in group:
    group_data = Series(g)
    print(group_data.describe())
    print("")

# Q-Q Graph
import numpy as np 
import pylab

for i in range (0, len(group)):
    measurements = group[i]
    stats.probplot(measurements, dist="norm", plot=pylab)
    pylab.show()

# Shapiro-Wilk test
for i in range (0, len(group)):
    print("Group", i + 1, ": ", stats.shapiro(group[i]))
    
# Levene test for equal variances.(center = "mean")

print("levene Test: ", stats.levene(group[0], group[1], group[2], center='mean'))

# Kruskal-Wallis H Test

stat, p = stats.kruskal(group[0], group[1], group[2])
print('stat=%f, p=%f' % (stat, p))
# if you only need 3 digits after the decimal point
# print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('不能拒绝原假设，样本集分布相同')
else:
    print('拒绝原假设，样本集分布可能不同')

#  Friedman rank sum test. 反正都要用到矩阵的
for g in group:
    print(len(g))
# not the same length
# so only combine the first 9 elements into square
data_square = np.array([group[0][:9] , group[1][:9] , group[2][:9]])

# print(data_array)
# print(*data_array.T)

# Conduct the Friedman Test
print(stats.friedmanchisquare(*data_square.T))

# Nemenyi’s test 
# !pip install command is only for kaggle module installation
# remove it on your own computer
#!pip install scikit_posthocs
import scikit_posthocs as sp

print(sp.posthoc_nemenyi_friedman(data_square.T))