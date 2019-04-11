﻿import matplotlib.pyplot as plt
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
    return answer in possible_predictions


def count_predictions(test_data, train_data, num_of_rows, euclidian_prediction=True):
    right_predictions = 0
    for i in range(len(test_data.index)):
        row_of_test = test_data.iloc[i].tolist()
        if check_right_prediction(lowest_distance_rows(i, train_data, euclidian_prediction, row_of_test, num_of_rows), row_of_test[-1]):
            right_predictions += 1
    return right_predictions


def calculate_final_results(test_data, train_data, k, file_name, euc_distance = True):
    hits = count_predictions(test_data, train_data, k, euc_distance)
    misses = len(test_data) - hits
    accuracy = hits / len(test_data) * 100
    if euc_distance:
        return round(accuracy, 2), hits, misses, 'euclidian', file_name, len(test_data), k
    return round(accuracy, 2), hits, misses, 'cosine', file_name, len(test_data), k


pd.options.mode.chained_assignment = None
files = ['iris.csv', 'glass.csv']
knn = [1, 3]

list_results = [] 
for file_name in files:
    print('\nProcessing...')
    print('Dataset: ', file_name, '\n')
    dataFrame = pd.read_csv(file_name)
    train_data, test_data = randomize_data(dataFrame)
    for k in knn:
        list_results.append(list(calculate_final_results(test_data, train_data, file_name, k)))
        train_data, test_data = randomize_data(dataFrame)
        list_results.append(list(calculate_final_results(test_data, train_data, file_name, k, False)))

print('-'*80)

columns = ['prec', 'hits', 'misses', 'distance', 'KNN', 'test_length', 'file']
results = pd.DataFrame(data=list_results, columns=columns)
print(results)
print('\nStandard Deviation:', round(results['prec'].std(), 2))
print('Mean Absolute Error:', round(results['misses'].mean(), 2))
print('Mean Absolute Deviation', round(results['prec'].mad(), 2))
print('Accuracy:', round(results['prec'].mean(), 2), '%')
# TODO: Confusion Matrix

# iris(k1,k3)-glass(k1,k3)-diabetes(k1,k3)
weka_precision = [96.0784,96.0784,67.1233,63.0137,72.7969,74.7126]
weka_error = [100 - x for x in weka_precision]
x = np.arange(len(weka_precision))
width = 0.6
plt.figure()
prec = plt.bar(x, weka_precision, width, color='c')
error = plt.bar(x, weka_error, width, color='r')
plt.xlabel('Datasets')
plt.ylabel('Precision')
plt.title('Weka')
plt.xticks(x, ('iris k1', 'iris  k3', 'glass k1', 'glass k3', 'diab. k1', 'diab. k3'))
# plt.grid(linestyle='--', color='k')
plt.legend((prec[0], error[0]), ('Precision', 'Error'))
plt.show()