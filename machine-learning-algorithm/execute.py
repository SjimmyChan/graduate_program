import os 
import re
from statistics_json import get_dataJson
#from machine_learning import get_dataPredict

data_correlated = []
data_twstock = []
data_id = []
result = 0

#get training data
data_correlated, data_twstock, data_id = get_dataJson(2330)

#get predict
#result = get_dataPredict(data_correlated, data_twstock)