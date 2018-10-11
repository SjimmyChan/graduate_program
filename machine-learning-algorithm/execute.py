import os 
import re
import numpy as np
import tensorflow as tf
import json
from statistics_json import get_dataJson
from get_mysql import get_companyList
from get_mysql import save_correlationData
from machine_learning_keras import data_training

result = 0

#def readjson(filename):
#    with open(filename,'r') as load_f:
#        load_dict = json.load(load_f)
#    return load_dict

#x = readjson("correlated.json")
#y = readjson("twstock.json")
#cr = readjson("correlated_ratio.json")

#x = np.array(x)
#y = np.array(y)
#cr = np.array(cr)

#print(x.shape, y.shape, cr.shape)

def initialize():
    
    data_correlated = []
    data_twstock = []
    data_id = []
    data_ratio = []
    company_list = ['2330', '2327', '3008']
    
    #get current company's stock list
    #company_list = get_companyList()
    #get training data
    for stock in company_list:
        #if len(stock[0]) == 4:
            #print(stock[0])
        data_correlated, data_twstock, data_id, data_ratio = get_dataJson(stock)
        if not data_twstock:
            print("no {} stock data".format(stock))
            continue
        else:
            #data training
            data_training(stock, data_correlated, data_ratio, data_twstock)
            save_correlationData(data_id, stock, data_ratio)
        #else:
        #    print("unconcerned stock id")

initialize()

