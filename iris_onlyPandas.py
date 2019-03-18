import pandas as pd
import numpy as np


def euclidian_distance(dataFrame, row):
    return np.linalg.norm(dataFrame.iloc[:, :-1].sub(row[:-1]), axis=1)

def cosine_similarity(dataFrame, row):
    cosine_sim = []
    for index in range (len(dataFrame.index)):
        nom = np.sum(np.multiply(row[:-1], dataFrame.iloc[index, :-1]))
        denom = np.sqrt(np.sum(np.square(row[:-1]))) * np.sqrt(np.sum(np.square(dataFrame.iloc[index, :-1].tolist())))
        sim = nom / denom
        cosine_sim.append(abs(1-sim))
    return cosine_sim
    
def lowest_distance_rows(index, dataFrame,  euc_distance, defined_row=None,  num_of_rows=1):
    best_matching_rows = []
    if not defined_row:
        defined_row = dataFrame.iloc[index].tolist()
    if euc_distance:
        dataFrame['distance'] = euclidian_distance(dataFrame, defined_row) 
    else:
        dataFrame['distance'] = cosine_similarity(dataFrame, defined_row) 
    best_matching_rows =  dataFrame.sort_values(['distance']).iloc[0, -2]
    if num_of_rows > 1:
        best_matching_rows = dataFrame.sort_values(['distance']).iloc[1:num_of_rows+1]
    dataFrame.drop('distance', axis=1 , inplace=True)
    return best_matching_rows

def make_predictions(test_data, train_data, euclidian_prediction = True):
    right_predictions = 0
    for i in range(len(test_data.index)):   
        row_of_test = test_data.iloc[i].tolist()
        if lowest_distance_rows(i, train_data, row_of_test, euclidian_prediction) == row_of_test[-1]:
            right_predictions += 1
    return right_predictions

# Part 1: Data Basic Operations

# opening iris data
pd.options.mode.chained_assignment = None
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
    print(lowest_distance_rows(12, dataFrame, True, None, show_range), '\n')

# Part 2: Predicting Species

# 1st Task - Mix Data
dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)

# 2nd Task - Separe Training and Test Data (2/1)
train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)

# 3rd Task - Make Predictions Based on Euc. Distance
print("Euclidian Distance - Number of right predictions:",
      make_predictions(test_data, train_data))

# 4th Task - Make Predictions Based on Sin.
print("Cosine - Number of right predictions:",
      make_predictions(test_data, train_data, False))
