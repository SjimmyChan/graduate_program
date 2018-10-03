import os 
import re
import numpy as np
import tensorflow as tf
from statistics_json import get_dataJson
from get_mysql import get_companyList

data_correlated = []
data_twstock = []
data_id = []
company_list = []
result = 0

#get current company's stock list
#company_list = get_companyList()

#get training data
data_correlated, data_twstock, data_id = get_dataJson(2330)
print("data initial complete")
data_correlated = np.array(data_correlated)
data_twstock = np.array(data_twstock)
data_id = np.array(data_id)
print(data_correlated.shape, data_id.shape, data_twstock.shape)
    #get predict
    #session, prediction = data_training(data_correlated, data_twstock)
    #saver = tf.train.Saver()
    #saver.save(session, save_path = 'data/', global_step=step)

#for stock_id in company_list:

