import twstock
import datetime
import json
import os 
import datetime
import sys
import apyori
import numpy as np
from get_mysql import run_getDataset
from get_mysql import run_getCostumerStock
from pearson_distance import get_datasetCorrelation

def get_dataJson(stockid):
    #get sorted data
    dataset = dict()
    data_correlated = []
    data_twstock = []
    data_id = []

    dataset = run_getDataset(dataset)
    dataset = run_getCostumerStock(dataset, stockid) #stockid from db
    data_correlated, data_twstock, data_id = get_datasetCorrelation(dataset)
    #------------------------------
    #dataset_json = json.dumps(dataset, ensure_ascii=False)

    #with open('data.json', 'w', encoding="utf-8") as filejson:
    #    json.dump(dataset_json, filejson, ensure_ascii=False)
    #filejson.close()
    #------------------------------
    return data_correlated, data_twstock, data_id
    


