from connect_database import run_getCostumerStock
from connect_database import run_getDataset
from pearson_distance import get_datasetCorrelation


def get_dataSet(stock_id):
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

    return data_correlated, data_twstock, data_id, data_ratio
    


