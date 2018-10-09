import twstock
import datetime
import json
import os 
import datetime
import sys
import apyori
import numpy as np
from get_mysql import run_getCostumerStock
from get_mysql import run_getDataset
from pearson_distance import get_datasetCorrelation


def get_dataJson(stock_id):
    #get sorted data
    dataset = dict()
    data_correlated = []
    data_twstock = []
    data_id = []
    data_ratio = []

    #get international data
    dataset = run_getDataset(dataset)
    dataset = run_getCostumerStock(dataset, stock_id) #stockid from db
    data_correlated, data_twstock, data_id, data_ratio = get_datasetCorrelation(dataset)
    #------------------------------
    '''dataset_json = json.dumps(data_correlated, ensure_ascii=False)
    with open('correlated.json', 'w', encoding="utf-8") as filejson:
        json.dump(dataset_json, filejson, ensure_ascii=False)
    filejson.close()

    dataset_json = json.dumps(data_twstock, ensure_ascii=False)
    with open('twstock.json', 'w', encoding="utf-8") as filejson:
        json.dump(dataset_json, filejson, ensure_ascii=False)
    filejson.close()

    dataset_json = json.dumps(data_ratio, ensure_ascii=False)
    with open('correlated_ratio.json', 'w', encoding="utf-8") as filejson:
        json.dump(dataset_json, filejson, ensure_ascii=False)
    filejson.close()'''
    #------------------------------
    return data_correlated, data_twstock, data_id, data_ratio
    


