import numpy as np
from scipy.stats import pearsonr
from math import sqrt

def get_datasetCorrelation(dataset):
    '''get correlation stock with costumer's stock'''
    data, data_id = dictionary_to_list(dataset)
    correlation_data = []
    correlation_id = []
    correlation_ratio = []
    tw_stock = []

    try:
        for ratio in data[:][len(data[0])]:
            tw_stock.append(ratio)
    except:
        print("costumer data doesn't exist")

    for category in range(len(data[0])-1):
        other_stock = []
        for ratio in data[:][category]:
            other_stock.append(ratio)
        correlation_data.append(other_stock)
        correlation_id.append(data_id[category])
        correlation_ratio.append(pearsonr(other_stock, tw_stock))

    return correlation_data, tw_stock, correlation_id, correlation_ratio

def dictionary_to_list(dataset):
    '''transfer dictionary dataset to list dataset'''
    data = []
    data_id = []

    for key in dataset.keys():
        data.append(list(dataset[key].values()))
    for key in dataset.keys():
        for stock_name in dataset[key].keys():
            data_id.append(stock_name)
        break

    return data, data_id