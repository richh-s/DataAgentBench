"""
SQLite utility functions.
Provides query interface to SQLite databases and returns pandas DataFrame.
"""

import sqlite3
import pandas as pd
from common_scaffold.config import SQLITE_PATH


def sqlite_query(sql: str, db_path: str = None) -> pd.DataFrame:
    """
    Execute an SQL query on a SQLite database and return the result as a pandas DataFrame.

    Args:
        sql (str): SQL query to execute.
        db_path (str, optional): Path to the SQLite database file.
                                 Defaults to config.SQLITE_PATH.

    Returns:
        pd.DataFrame: Query result.
    """
    db_path = db_path or SQLITE_PATH

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql, conn)
    conn.close()

    return df
