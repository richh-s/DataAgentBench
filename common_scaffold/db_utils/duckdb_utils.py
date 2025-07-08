"""
DuckDB utility functions.
These include querying DuckDB and listing tables.
"""

import duckdb
import pandas as pd
from pathlib import Path


def duckdb_query(db_path: str, sql: str) -> pd.DataFrame:
    """
    Execute a query on a DuckDB database and return the result as a pandas DataFrame.

    Args:
        db_path (str): Path to the .duckdb file.
        sql (str): SQL query to execute.

    Returns:
        pd.DataFrame: Query result.
    """
    db_file = Path(db_path)
    if not db_file.exists():
        raise FileNotFoundError(f"DuckDB file not found: {db_path}")
    
    conn = duckdb.connect(database=str(db_file))
    df = conn.execute(sql).fetchdf()
    conn.close()
    return df


def list_tables(db_path: str) -> pd.DataFrame:
    """
    List all tables in a DuckDB database.

    Args:
        db_path (str): Path to the .duckdb file.

    Returns:
        pd.DataFrame: DataFrame with a single column 'table_name' listing all tables.
    """
    sql = """
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'main';
    """
    return duckdb_query(db_path, sql)
