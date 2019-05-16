import  pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def open_dataset(filename):
    return pd.read_csv(filename)

def split_dataset(dataset):
    dataset = dataset.sample(frac=1).reset_index(drop=True)
        return dataset[:]

files = ['diabetes.csv', 'iris.csv', 'glass.csv']

dataset = open_dataset(files[0])
dataset['class'].replace(['tested_negative', 'tested_positive'], [0, 1],inplace=True)
