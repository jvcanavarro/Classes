import pandas as pd
import numpy as np

# Part 1: Data Basic Operations
def closest_row(index, dataFrame, line = None,  show_range = 1, rang = False):
    if not line:
        line = dataFrame.iloc[index].tolist()
    dataFrame['euc_distance'] = np.linalg.norm(
        dataFrame.iloc[:, :-1].sub(line[:-1]), axis=1)
    if rang:
        return dataFrame.sort_values(['euc_distance']).iloc[1:show_range+1]
    return dataFrame.sort_values(['euc_distance']).iloc[0, -2]


def make_euclidian_prediction(dataFrame):
    right_predictions = 0
    train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)
    for i in range(len(test_data.index)):
        row_of_test = test_data.iloc[i].tolist()
        # train_data['euc_distance'] = np.linalg.norm(
        #    train_data.iloc[:, :-1].sub(row_of_test[:-1]), axis=1)
        if closest_row(i, train_data, row_of_test) == row_of_test[-1]:
            right_predictions += 1
        train_data.drop('euc_distance', axis=1, inplace=True)
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
for rnge in list_of_ranges:
    print(closest_row(12, dataFrame, None, rnge, True), '\n')
    dataFrame.drop('euc_distance', axis=1, inplace=True)

# Part 2: Predicting Species
# 1st Task - Mix Data
dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)

# 2nd Task - Separe Training and Test Data (2/1)
train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)

# 3rd Task - Make Predictions Based on Euc. Distance
pd.options.mode.chained_assignment = None
print("Number of right predictions:",
      make_euclidian_prediction(dataFrame))

# 4th Task - Make Predictions Based on Sin.
