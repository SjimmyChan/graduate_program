import os 
import re
import numpy as np
import tensorflow as tf
from statistics_json import get_dataJson
from get_mysql import get_companyList
from machine_learning import get_prediction
from machine_learning import data_training
#from machine_learning import get_dataPredict

data_correlated = []
data_twstock = []
data_id = []
company_list = []
result = 0

#get current company's stock list
company_list = get_companyList()

step = 0
for stock_id in company_list:
    step += 1
    #get training data
    data_correlated, data_twstock, data_id = get_dataJson(stock_id)

    data_correlated = np.array(data_correlated)
    data_twstock = np.array(data_twstock)
    #get predict
    #session, prediction = data_training(data_correlated, data_twstock)
    #saver = tf.train.Saver()
    #saver.save(session, save_path = 'data/', global_step=step)

#for stock_id in company_list:

