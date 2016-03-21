import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


headers = ['name','title','department','salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv', header=False, names=headers, converters={'salary': lambda x: float(x.replace('$', ''))})

df = chicago

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(pd.rolling_mean(df['salary'], 12), color='b')

ax2 = ax1.twinx()
ax2.plot(pd.rolling_median(df['salary'], 12), color='r')

plt.show()


