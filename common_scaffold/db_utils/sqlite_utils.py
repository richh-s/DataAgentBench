import sqlite3
import pandas as pd
from common_scaffold.config import SQLITE_PATH

def sqlite_query(sql, db_path=None):
    db_path = db_path or SQLITE_PATH
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df
