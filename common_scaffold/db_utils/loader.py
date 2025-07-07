from .mongo_utils import mongo_query
from .sqlite_utils import sqlite_query
from .duckdb_utils import duckdb_query
from .mysql_utils import mysql_query

def query_db(db_type, **kwargs):
    if db_type == "mongo":
        return mongo_query(**kwargs)
    elif db_type == "sqlite":
        return sqlite_query(**kwargs)
    elif db_type == "duckdb":
        return duckdb_query(**kwargs)
    elif db_type == "mysql":
        return mysql_query(**kwargs)
    else:
        raise ValueError(f"Unsupported db_type: {db_type}")
