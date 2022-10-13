from scipy import stats
import pandas as pd
from pandas import DataFrame, Series
import statsmodels.api as sm
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")
print(data)

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
print(data)

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
        
for i in range (0, len(group)):
    print(Series(group[i]).describe())
    data = sm.datasets.longley.load()
    data.exog = sm.add_constant(data.exog)
    model = sm.OLS(data.endog, data.exog)
    mod_fit = model.fit()
    res = mod_fit.resid # 获取了构造的模型的残差，获取了数据
    # 主要调用方法
    probplot = sm.ProbPlot(res) # 实例probplot
    probplot.qqplot(line='s') # 调用函数
    plt.show()
    
# count     9.000000
# mean     37.777778
# std       9.243616
# min      30.000000
# 25%      32.000000
# 50%      34.000000
# 75%      40.000000
# max      58.000000
# dtype: float64

# count     11.000000
# mean     377.727273
# std       98.181557
# min      263.000000
# 25%      325.000000
# 50%      367.000000
# 75%      381.000000
# max      579.000000
# dtype: float64

# count      10.000000
# mean      902.600000
# std       153.857943
# min       775.000000
# 25%       796.750000
# 50%       828.000000
# 75%       957.500000
# max      1230.000000
# dtype: float64

