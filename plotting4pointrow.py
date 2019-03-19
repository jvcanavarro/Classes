import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


cols = pd.read_csv('iris.csv', nrows=1).columns
df = pd.read_csv('iris.csv',nrows = 5, usecols = cols[:-1])

x = []
y = []
xy = []
for i in range (len(df.index)):
    xy.append(df.iloc[i, :].tolist())
    # x.append(df.iloc[i, :-2].tolist(), df.iloc[i, 2:].tolist())
    # y.append(df.iloc[i, 2:].tolist())
print(xy)
# y2 = np.arange(len(xy) * 2)
df.plot.area()
plt.show()