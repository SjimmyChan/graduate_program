import pymysql
import os
from datetime import datetime
from sql import maxCount_sql
from sql import sorted_data
from sql import get_TWStockDate
from sql import save_correlationID
from sql import companyInfo
from sql import save_predictionRatio

#start_date = datetime.date(2015, 1, 1)
#end_date = datetime.date(2018, 1, 1)

########################calculate########################

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
        cursor.execute(get_TWStockDate(stockid, date))
        data = cursor.fetchall()
        if not data:
            #print("None")
            absence_date.append(date)
        else:
            #print("insert", date, str(stockid), data[0][1])
            data_insert(dataset, date, str(stockid), data[0][1])
    return absence_date

def save_data(data_id, stock_id, correlation_ratio, cursor, db):
    for location in range(len(data_id)):
        sql = save_correlationID(stock_id, data_id[location], correlation_ratio[location][0])
        cursor.execute(sql)
        db.commit()

#############################clean#############################

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

#############################database#############################

def get_companyList():
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()    
    
    companylist = []
    try:
        cursor.execute(companyInfo)
        companylist = cursor.fetchall()
        print("get company list complete")
    except:
        print("get company list error!!")

    return companylist

    #disconnect
    db.close()

def run_getDataset(dataset):
    '''get world stock data'''
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    #get data and sorted
    try:
        get_sortAllData(dataset, cursor)
        print("get international data complete")
    except:
        print ("run get dataset error!!")

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
        print("get costumer stock data complete")
    except:
        print("run get costumer stock error!!")
    dataset = clean_absence(dataset, absence_date)
    return dataset

    #disconnect
    db.close()

def save_correlationData(data_id, stock_id, correlation_ratio):
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    try:
        save_data(data_id, stock_id, correlation_ratio, cursor, db)
        print("{} correlated data saved".format(stock_id))
    except:
        print("save correlation data error!!")
    #disconnect
    db.close()

def save_predictRatio(stock_id, ratio, date):
    #connect mysql
    db = pymysql.connect(host='birdyoserv.ga', port=3307, user='admin', passwd='1234', db='stock_analytics')
    #db = pymysql.connect("localhost", "root", "root", "stock_analytics")
    cursor = db.cursor()

    try:
        cursor.execute(save_predictionRatio(stock_id, ratio, None, date))
        db.commit()
        print("save stock : {} complete".format(stock_id))
    except:
        print("save predict ratio error!!")

    #disconnect
    db.close()