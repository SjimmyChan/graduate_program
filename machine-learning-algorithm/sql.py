
def sorted_data(place):
    sort_sql = """
        SELECT
            `time`, ratio 
        FROM
            world_stock_price
        WHERE
            type = "{}" 
    """.format(place)
    return sort_sql

maxCount_sql = """
SELECT
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

def getTWStockDate(stockid, date):
    sql = """
    SELECT DISTINCT  
        `date` as time, difference as ratio, no as stockid
    FROM
        tw_stock_price
    WHERE
        no = {0} and
        `date` = '{1}'
    """.format(stockid, date)
    return sql