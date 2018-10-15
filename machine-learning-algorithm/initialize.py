import numpy as np
import tensorflow as tf
from get_requireData import get_dataSet
from connect_database import get_companyList
from connect_database import save_correlationData
from machine_learning_keras import data_training

def initialize():
    data_correlated = []
    data_twstock = []
    data_id = []
    data_ratio = []
    company_list = []
    
    #get current company's stock list
    company_list = get_companyList()
    
    for stock in company_list:
        if len(stock[0]) == 4:
            #print(stock[0])
            #get training data
            data_correlated, data_twstock, data_id, data_ratio = get_dataSet(stock[0])
            if not data_twstock:
                print("no {} stock data".format(stock[0]))
                continue
            else:
                #data training
                data_training(stock[0], data_correlated, data_ratio, data_twstock)
                save_correlationData(data_id, stock[0], data_ratio)
        else:
            print("unconcerned stock id")

initialize()

