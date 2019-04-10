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


def cosine_similarity(dataFrame, row):
    return 1 - np.dot(dataFrame, row) / (np.sqrt(np.dot(dataFrame, dataFrame)) * np.sqrt(np.dot(row, row)))


def euclidian_distance(dataFrame, row):
    return np.linalg.norm(dataFrame.iloc[:, :-1].sub(row[:-1]), axis=1)


def lowest_distance_rows(index, dataFrame,  euc_prediction=True, defined_row=None,  num_of_rows=1, multiple_lines=False):
    best_matching_species = []
    if not defined_row:
        defined_row = dataFrame.iloc[index].tolist()

    if euc_prediction == True:
        dataFrame['distance'] = euclidian_distance(dataFrame, defined_row)
    else:
        dataFrame['distance'] = dataFrame.iloc[:, :-1].apply(cosine_similarity, row=(defined_row[:-1]), axis=1)

    best_matching_species = dataFrame.sort_values(['distance']).iloc[0, -2]

    if multiple_lines:
        best_matching_species = dataFrame.sort_values(
            ['distance']).iloc[1:num_of_rows+1]

    dataFrame.drop('distance', axis=1, inplace=True)

    return best_matching_species


def randomize_data(dataFrame):
    dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)
    return np.split(dataFrame, [int(.66*len(dataFrame))])


def check_right_prediction(possible_predictions, answer):
    if answer in possible_predictions:
        # print(answer, possible_predictions)
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

knn = [1, 3]

for file_name in files:
    print('Dataset: ', file_name)
    dataFrame = pd.read_csv(file_name)
    dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)
    train_data, test_data = np.split(dataFrame, [int(.66*len(dataFrame))])
    for k in knn:
        acc_euc, acc_cos = []
        print('Actual Range:',k)
        acc_euc = count_predictions(test_data, train_data, k) / len(test_data) * 100
        print('Right Predictions - Euclidian Distance:', acc_euc,'%')
        train_data, test_data = randomize_data(dataFrame)
        acc_cos = count_predictions(test_data, train_data, k, False) / len(test_data) * 100
        print('Right Predictions - Cosine Similarity:', acc_cos,'%')
        print()

