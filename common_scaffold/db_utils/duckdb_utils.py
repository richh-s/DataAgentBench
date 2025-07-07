import duckdb
import pandas as pd
from common_scaffold.config import DUCKDB_PATH

def duckdb_query(sql, db_path=None):
    db_path = db_path or DUCKDB_PATH
    conn = duckdb.connect(db_path)
    df = conn.execute(sql).fetchdf()
    conn.close()
    return df
