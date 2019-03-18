import pandas as pd
import numpy as np

# Part 1: Data Basic Operations

def closest_rows(index, dataFrame, line=None,  num_of_rows=1, multLines=False):
    best_matching_rows = []
    if not line:
        line = dataFrame.iloc[index].tolist()
    dataFrame['euc_distance'] = np.linalg.norm(
        dataFrame.iloc[:, :-1].sub(line[:-1]), axis=1)
    best_matching_rows =  dataFrame.sort_values(['euc_distance']).iloc[0, -2]
    if multLines:
        best_matching_rows = dataFrame.sort_values(['euc_distance']).iloc[1:num_of_rows+1]
    dataFrame.drop('euc_distance', axis=1 , inplace=True)
    return best_matching_rows


def make_euclidian_prediction(test_data, train_data):
    right_predictions = 0
    for i in range(len(test_data.index)):   # iterate throw all test_data rows
        row_of_test = test_data.iloc[i].tolist()
        if closest_rows(i, train_data, row_of_test) == row_of_test[-1]:
            right_predictions += 1
    return right_predictions


# opening iris data
dataFrame = pd.read_csv("iris.csv.txt")

# mean, max and min of each column (a, b)
print(dataFrame.mean(), "\n")
print(dataFrame.iloc[:, :-1].max(), "\n")
print(dataFrame.iloc[:, :-1].min(), "\n")

# 10 rows with lower sum (c)
print(dataFrame.sum(axis=1, numeric_only=True).sort_values(
    ascending=True).head(10), '\n')

# closest line(s) of nth line (d, e ,f)
list_of_ranges = [5, 3, 1]
for show_range in list_of_ranges:
    print(closest_rows(12, dataFrame, None, show_range, True), '\n')

# Part 2: Predicting Species
# 1st Task - Mix Data
dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)

# 2nd Task - Separe Training and Test Data (2/1)
train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)

# 3rd Task - Make Predictions Based on Euc. Distance
pd.options.mode.chained_assignment = None
print("Number of right predictions:",
      make_euclidian_prediction(test_data, train_data))

# 4th Task - Make Predictions Based on Sin.
