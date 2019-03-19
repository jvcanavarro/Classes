import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def euclidian_distance(dataFrame, row):
    return np.linalg.norm(dataFrame.iloc[:, :-1].sub(row[:-1]), axis=1)


def cosine_similarity(dataFrame, row):
    cosine_sim = []
    for index in range(len(dataFrame.index)):
        nom = np.sum(np.multiply(row[:-1], dataFrame.iloc[index, :-1].tolist()))
        denom = np.sqrt(np.sum(np.square(
            row[:-1]))) * np.sqrt(np.sum(np.square(dataFrame.iloc[index, :-1].tolist())))
        cosine_sim.append(1 - (nom / denom))
    return cosine_sim


def plot_ibk_dots():
    pass

def lowest_distance_rows(index, dataFrame,  euc_prediction, defined_row=None,  num_of_rows=1, multiple_lines = False):
    best_matching_species = []

    if not defined_row:
        defined_row = dataFrame.iloc[index].tolist()

    if euc_prediction == True:
        dataFrame['distance'] = euclidian_distance(dataFrame, defined_row)
    else:
        dataFrame['distance'] = cosine_similarity(dataFrame, defined_row)

    best_matching_species = dataFrame.sort_values(['distance']).iloc[0, -2]

    if multiple_lines: 
        best_matching_species = dataFrame.sort_values(['distance']).iloc[1:num_of_rows+1]
        print(best_matching_species)
    
    dataFrame.drop('distance', axis=1, inplace=True)

    return best_matching_species

def randomize_data(dataFrame):
    dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)
    return dataFrame[:100], dataFrame[100:].reset_index(drop=True)

def check_right_prediction(possible_predictions, answer):
    if answer in possible_predictions:
        return True
    return False

def count_predictions(test_data, train_data, num_of_rows, euclidian_prediction=True):
    right_predictions = 0
    for i in range(len(test_data.index)):
        row_of_test = test_data.iloc[i].tolist()
        if check_right_prediction(lowest_distance_rows(i, train_data, euclidian_prediction, row_of_test, num_of_rows), row_of_test[-1]):
            right_predictions += 1
    return right_predictions

def evaluate_predictions(dataFrame, test_data, train_data, num_of_rows):
    euc_right_predictions = count_predictions(test_data, train_data, num_of_rows)
    train_data, test_data = randomize_data(dataFrame)
    cos_right_predictions = count_predictions(test_data, train_data, num_of_rows, False)
    return euc_right_predictions, cos_right_predictions

# opening iris data
pd.options.mode.chained_assignment = None
dataFrame = pd.read_csv("iris.csv")
list_of_ranges = [1, 3, 5]

# mean, max and min of each column (a, b)
print(dataFrame.mean(), "\n")
print(dataFrame.iloc[:, :-1].max(), "\n")
print(dataFrame.iloc[:, :-1].min(), "\n")

# 10 rows with lower sum (c)
print(dataFrame.sum(axis=1, numeric_only=True).sort_values(
    ascending=True).head(10), '\n')

# closest line(s) of nth line (d, e ,f)
for show_range in list_of_ranges:
    print(lowest_distance_rows(12, dataFrame, True, None, show_range, True), '\n')


# 1st Task - Mix Data
dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)

# 2nd Task - Separe Training and Test Data (2/1)
train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)

# 3rd Task - Make Predictions Based on Euc. Distance & Cosine Similarity

num_of_right_predictions = []

for show_range in list_of_ranges:
    num_of_right_predictions.append( evaluate_predictions(dataFrame, test_data, train_data, show_range))

print('Ranges 1/3/5 (euc_dist | cos_sim):', num_of_right_predictions)
