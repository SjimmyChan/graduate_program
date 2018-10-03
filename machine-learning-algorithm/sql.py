#######################GET DATA########################

#get place stock's ratio
def sorted_data(place):
    sort_sql = """
        SELECT DISTINCT
            `time`, ratio 
        FROM
            world_stock_price
        WHERE
            type = "{}" 
    """.format(place)
    return sort_sql

#history data max = 784
maxCount_sql = """
SELECT DISTINCT
    x.type
FROM
    (
        SELECT
            COUNT(*) as totalcount,
            type
        FROM
            world_stock_price
        GROUP BY
            type
    ) x
WHERE
    (
        SELECT
            max(x.totalcount) as maxCount
        FROM
            (
                SELECT
                    COUNT(*) as totalcount
                FROM
                    world_stock_price
                GROUP BY
                    type
            ) x
    ) = totalcount
ORDER BY x.type ASC
"""
#get costumer's stock data
def get_TWStockDate(stockid, date):
    sql = """
    SELECT DISTINCT  
        `date` as time, difference as ratio, no as stockid
    FROM
        tw_stock_price
    WHERE
        no = '{0}' and
        `date` = '{1}'
    """.format(stockid, date)
    return sql

#get company stockid
companyInfo = """
SELECT DISTINCT  
    no as stockid
FROM
    tw_company_list"""

#get twstock correlation international stock data
def get_savedCorrelationID(stock_id):
    sql = """
    SELECT 
        internationalstock_name as other_stock_id
    FROM
        stock_relationship
    WHERE
        stock_id = "{}"
    """.format(stock_id)
    return sql

###############################SAVE################################

#save twstock correlation international stock data
def save_correlationID(stock_id, data_name):
    sql = """
    INSERT INTO `stock_relationship`
        (`twstock_id`, `internationalstock_name`)
    VALUES
        ("{}", "{}")
    """.format(stock_id, data_name)
    return sql

#save predict ratio to database
def save_predictionRatio(stock_id, ratio, accuracy, date):
    sql = """
    INSERT INTO `predict_ratio`
        (`no`, `result`, `accuracy`, `date`)
    VALUES
        ("{}", "{}", "{}", "{}")
    """.format(stock_id, ratio, accuracy, date)
    return sql