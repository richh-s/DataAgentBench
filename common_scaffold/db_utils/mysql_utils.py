import mysql.connector
import pandas as pd
from common_scaffold import config

def mysql_query(sql, db=None, host=None, user=None, password=None, port=None):
    conn = mysql.connector.connect(
        host=host or config.MYSQL_HOST,
        user=user or config.MYSQL_USER,
        password=password or config.MYSQL_PASSWORD,
        database=db or config.MYSQL_DB,
        port=port or config.MYSQL_PORT
    )
    df = pd.read_sql(sql, conn)
    conn.close()
    return df
