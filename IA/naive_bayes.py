import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def probability(row, dataFrame):
    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))

    return p


def lowest_distance_rows(index, dataFrame):

    defined_row = dataFrame.iloc[index].tolist()

    dataFrame['probability'] = dataFrame.iloc[:, :-1].apply(probability, row=(defined_row[:-1]), axis=1)

    best_matching = dataFrame.sort_values(['probability'], ascending=False).iloc[0, -2]

    dataFrame.drop('probability', axis=1, inplace=True)

    return best_matching


def check_prediction(row, test_data):
	


def naive_bayes(dataFrame):
	train_data, test_data = split_dataFrame(dataFrame)
	right_predictions = 0
	for row in test_data:
		if check_prediction(row, train_data):
			right_predictions += 1
	return right_predictions

def open_dataFrame(filename):
    return pd.read_csv(filename)

def split_dataFrame(dataFrame):
    dataFrame = dataFrame.sample(frac=1).reset_index(drop=True)
    train_len = int (0.67 * len(dataFrame))
    return dataFrame[:train_len], dataFrame[train_len:].reset_index(drop=True)

def show_data_information(dataFrame):
	print('---dataFrame Information---')
	print(dataFrame.describe(), '\n')

def analyse_dataFrames(files):
	for file in files:
		dataFrame = open_dataFrame(file)
		show_data_information(dataFrame)
		print("dataFrame: ", file)
		print("Number of Right Predictions:", naive_bayes(dataFrame))

def main():
	files = ['diabetes.csv', 'iris.csv', 'glass.csv']
	analyse_dataFrames(files)

main()