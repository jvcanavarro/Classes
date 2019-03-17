import pandas as pd
import numpy as np


def closest_row(index, dataset, show_range):
    line = dataset.iloc[index, :-1].tolist()
    dataset['eu_distance'] = np.linalg.norm(dataset.iloc[:, :-1].sub(line), axis=1)
    return dataset.sort_values(['eu_distance']).iloc[1:show_range+1]

# opening iris data
dataFrame = pd.read_csv("iris.csv.txt")

# mean, max and min of each column
print(dataFrame.mean(), "\n")
print(dataFrame.iloc[:, dataFrame.columns != 'species'].max(), "\n")
print(dataFrame.iloc[:, dataFrame.columns != 'species'].min(), "\n")

# 10 rows with lower sum
print(dataFrame.sum(axis=1, numeric_only=True).sort_values(ascending=True).head(10))

# closest line(s) of nth line
list_of_ranges = [5, 3, 1]
for rnge in list_of_ranges:
    print(closest_row(12, dataFrame, rnge))
    dataFrame.drop('eu_distance', axis=1, inplace=True)