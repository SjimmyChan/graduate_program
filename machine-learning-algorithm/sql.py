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

#get daily international stock ratio
def daily_ratio(place, date):
    sql = """
        SELECT DISTINCT
            ratio 
        FROM
            world_stock_price
        WHERE
            type = '{}' and
            `time` = '{}'
    """.format(place, date)
    return sql

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
        correlation_ratio
    FROM
        stock_relationship
    WHERE
        twstock_id = '{}'
    """.format(stock_id)
    return sql

###############################SAVE################################

#save twstock correlation international stock data
def save_correlationID(stock_id, data_name, correlation_ratio):
    sql = """
    INSERT INTO stock_relationship
        (twstock_id, internationalstock_name, correlation_ratio)
    VALUES
        ("{}", "{}", {})""".format(stock_id, data_name, correlation_ratio)
    return sql

#save predict ratio to database
def save_predictionRatio(stock_id, ratio, accuracy, date):
    sql = """
    INSERT INTO `predict_ratio`
        (`no`, `result`, `accuracy`, `date`)
    VALUES
        ("{}", "{}", "{}", "{}")""".format(stock_id, ratio, accuracy, date)
    return sql