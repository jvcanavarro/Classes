import numpy as np
import pandas as pd


def split_dataFrame(data):
    pass


def return_mmm():
    pass


def closet_row(index, dataset, show_range):
    pass


# opening iris data
dataFrame = pd.read_csv("iris.csv.txt")

# mean, max and min of each column
print(dataFrame.mean(), "\n")
print(dataFrame.iloc[:, dataFrame.columns != 'species'].max(), "\n")
print(dataFrame.iloc[:, dataFrame.columns != 'species'].min(), "\n")

# 10 rows with lower sum
print()