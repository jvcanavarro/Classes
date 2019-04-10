import pandas as pd
import numpy as np
#import math
#from decimal import Decimal


#def jaccard_similarity(dataFrame, row):
#    intersection_cardinality = len(set.intersection(*[set(dataFrame), set(row)]))
#    union_cardinality = len(set.union(*[set(dataFrame), set(row)]))
#    return 1 - (intersection_cardinality/float(union_cardinality))


#def nth_root(value, n_root):
#    root_value = 1/float(n_root)
#    return round(Decimal(value) ** Decimal(root_value), 3)


#def minkowski_distance(x, y, p_value):
#    return nth_root(sum(pow(abs(a-b), p_value) for a, b in zip(x, y)), p_value)


#def manhattan_distance(dataFrame, row):
#    return sum(abs(dataFrame - row) for dataFrame, row in zip(dataFrame, row))


#def cosine_similarity(dataFrame, row):
#    return 1 - np.dot(dataFrame, row) / (np.sqrt(np.dot(dataFrame, dataFrame)) * np.sqrt(np.dot(row, row)))


def euclidian_distance(dataFrame, row):
    return np.linalg.norm(dataFrame.iloc[:, :-1].sub(row[:-1]), axis=1)


def lowest_distance_rows(index, dataFrame,  euc_prediction=True, defined_row=None,  num_of_rows=1, multiple_lines=False):
    best_matching_species = []

    if not defined_row:
        defined_row = dataFrame.iloc[index].tolist()

    if euc_prediction == True:
        dataFrame['distance'] = euclidian_distance(dataFrame, defined_row)
    #else:
        #dataFrame['distance'] = dataFrame.iloc[:, :-1].apply(cosine_similarity, row=(defined_row[:-1]), axis=1)

    best_matching_species = dataFrame.sort_values(['distance']).iloc[0, -2]

    if multiple_lines:
        best_matching_species = dataFrame.sort_values(
            ['distance']).iloc[1:num_of_rows+1]

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


# opening iris/glass/diabetes data
pd.options.mode.chained_assignment = None
files = ['iris.csv', 'glass.csv', 'diabetes.csv']
# dataFrame = pd.read_csv("iris.csv")
knn = [1, 3]


# closest line(s) of nth line (KNN)

# dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)
# train_data, test_data = dataFrame[:100], dataFrame[100:].reset_index(drop=True)

# for k in knn:
    # print(lowest_distance_rows(11, dataFrame, True, None, k, True), '\n')

#for show_range in list_of_ranges:
    # print('Actual Range:',show_range)
    # print("Euclidian Distance - Number of right predictions: ", count_predictions(test_data, train_data, show_range))
    # print('Right Predictions - Euclidian Distance:', count_predictions(test_data, train_data, show_range) / 50 * 100,'%')
    # train_data, test_data = randomize_data(dataFrame)
    # print("Cosine Similarity - Number of right predictions:",count_predictions(test_data, train_data, show_range, False))
    # print('Right Predictions - Cosine Similarity:', count_predictions(test_data, train_data, show_range, False) / 50 * 100,'%')
    # print()
