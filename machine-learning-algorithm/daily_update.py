import os 
import re
import datetime
import time
import numpy as np
import tensorflow as tf
import json
import pymysql
from get_mysql import ratio_clean
from get_mysql import save_predictRatio
from sql import daily_ratio
from sql import maxCount_sql
from sql import get_savedCorrelationID
from machine_learning_keras import get_predict

def predict():

    correlation_data = []
    stock_id_list = ['2330', '2327', '3008']

    #get current date
    now = datetime.datetime.now()
    current_date = "{}-{}-{}".format(now.year, now.month, now.day)
    correlation_data = get_correlationData(current_date)
    
    while not correlation_data:
        now = now - datetime.timedelta(days = 1)
        current_date = "{}-{}-{}".format(now.year, now.month, now.day)
        correlation_data = get_correlationData(current_date)

    for stock_id in stock_id_list:
        predict = get_predict(stock_id, correlation_data, get_pearsonRatio(stock_id))
        save_predictRatio(stock_id, predict[0][0], current_date)

def get_correlationData(current_date):

    correlation_data = []
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    cursor.execute(maxCount_sql) 
    maxcount = cursor.fetchall()
    for location in range(len(maxcount)):
        place_clean = "".join(maxcount[location]) #format place string
        cursor.execute(daily_ratio(place_clean, current_date))
        data = cursor.fetchall()
        for ratio in data:
            correlation_data.append(ratio_clean(ratio))

    return correlation_data

    db.close()

def get_pearsonRatio(stock_id):
    
    correlation_ratio = []
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    cursor.execute(get_savedCorrelationID(stock_id))
    data = cursor.fetchall()
    for ratio in data:
        correlation_ratio.append(ratio[0])
    
    return correlation_ratio
    
    db.close()

predict()