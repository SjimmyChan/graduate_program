import pymysql
import os
from datetime import datetime
from sql import maxCount_sql
from sql import sorted_data
from sql import getTWStockDate

#start_date = datetime.date(2015, 1, 1)
#end_date = datetime.date(2018, 1, 1)

#diff_date = end_date - start_date

def get_sortAllData(dataset, cursor):
    '''execute sql get data and sorted'''
    cursor.execute(maxCount_sql) 
    maxcount = cursor.fetchall()
    for location in range(len(maxcount)):
        place_clean = "".join(maxcount[location]) #format place string 
        cursor.execute(sorted_data(place_clean))
        data = cursor.fetchall()
        for row in range(len(data)):
            data_insert(dataset, str(data[row][0]), place_clean, ratio_clean(data[row][1]))

def get_twstock(dataset, stockid, cursor):
    '''get stock information'''
    absence_date = []
    for date in dataset.keys():
        cursor.execute(getTWStockDate(stockid, date))
        data = cursor.fetchall()
        if not data:
            #print("None")
            absence_date.append(date)
        else:
            #print("insert", date, str(stockid), data[0][1])
            data_insert(dataset, date, str(stockid), data[0][1])
    return absence_date

def clean_absence(dataset, absence_date):
    for date in absence_date:
        if date in dataset.keys():
            dataset.pop(date)
    return dataset

def ratio_clean(ratio):
    '''format ratio to float'''
    clean = "".join(ratio)
    data = clean[0:-1]
    return float(data)

def data_insert(data, date, place, ratio):
    '''insert new place:{ratio} to previous one'''
    place_ratio = dict()
    previous_data = dict()
    if date in data:
        previous_data = data[date]
        previous_data[place] = ratio
        data[date] = previous_data
    else:
        place_ratio[place] = ratio
        data[date] =  place_ratio
    return data

def run_getDataset(dataset):
    '''get world stock data'''
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    #get data and sorted
    try:
        get_sortAllData(dataset, cursor)
    except:
        print ("error occur!!")

    #output dataset:
    #dataset = {'date':{'place':{'ratio': }}}
    #dataset = {'2018, 1, 1':{'台灣股市': 0.87}}
    return dataset

    #disconnect
    db.close()

def run_getCostumerStock(dataset, stockid):
    '''get costumer choose stock in dataset'''
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()
    absence_date = []

    #get stock data into dataset
    try:
        absence_date = get_twstock(dataset, stockid, cursor)
        #get_twstock(dataset, stockid, cursor)
    except:
        print("error occur!!")
    dataset = clean_absence(dataset, absence_date)
    return dataset

    #disconnect
    db.close()
