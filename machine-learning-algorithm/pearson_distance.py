import numpy as np
from math import sqrt

def pearson_distance(other_stock, tw_stock) :
    '''Calculate distance between two vectors using pearson method'''
    sum1 = sum(other_stock)
    sum2 = sum(tw_stock)

    sum1Sq = sum([pow(v,2) for v in other_stock])
    sum2Sq = sum([pow(v,2) for v in tw_stock])

    pSum = sum([other_stock[i] * tw_stock[i] for i in range(len(other_stock))])

    num = pSum - (sum1*sum2/len(other_stock))
    den = sqrt((sum1Sq - pow(sum1,2)/len(other_stock)) * (sum2Sq - pow(sum2,2)/len(other_stock)))

    if den == 0 : return 0.0
    return 1.0 - num/den

def get_datasetCorrelation(dataset):
    '''get correlation stock with costumer's stock'''
    data, data_id = dictionary_to_list(dataset)
    correlation_data = []
    correlation_id = []
    tw_stock = []

    for ratio in data[:][len(data[0])]:
            tw_stock.append(ratio)

    for category in range(len(data[0])-1):
        other_stock = []
        for ratio in data[:][category]:
            other_stock.append(ratio)
        
        if pearson_distance(other_stock, tw_stock) >= 0.6:
            correlation_data.append(other_stock)
            #correlation_id.append(data_id[category])

    return correlation_data, tw_stock, correlation_id

def dictionary_to_list(dataset):
    '''transfer dictionary dataset to list dataset'''
    data = []
    data_id = []

    for key in dataset.keys():
        data.append(list(dataset[key].values()))
    for key in dataset.keys():
        for stock_name in dataset[key].keys():
            print(stock_name)
            break
        break

    return data, data_id