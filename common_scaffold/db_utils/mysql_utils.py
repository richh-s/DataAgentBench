"""
MySQL utility functions.
These include ensuring the database exists and is populated,
querying MySQL using SQLAlchemy, and checking database existence & tables.
"""

from sqlalchemy import create_engine
import mysql.connector
import pandas as pd
from pathlib import Path
import re
from common_scaffold import config


def mysql_query(sql: str, db_name: str = None) -> pd.DataFrame:
    """
    Execute a MySQL query and return result as a pandas DataFrame.
    Uses SQLAlchemy for better compatibility.

    Args:
        sql (str): SQL query to execute.
        db (str): Database name. If None, use config.MYSQL_DB.

    Returns:
        pd.DataFrame: Query result.
    """
    db_name = db_name or config.MYSQL_DB

    uri = (
        f"mysql+mysqlconnector://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}"
        f"@{config.MYSQL_HOST}:{config.MYSQL_PORT}/{db_name}"
    )
    engine = create_engine(uri)

    with engine.connect() as conn:
        df = pd.read_sql(sql, conn)

    return df


def database_exists(db_name: str) -> bool:
    """
    Check if a MySQL database exists.

    Args:
        db_name (str): Target database name.

    Returns:
        bool: True if the database exists, False otherwise.
    """
    conn = mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        port=config.MYSQL_PORT
    )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES;")
    dbs = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return db_name in dbs


def database_has_tables(db_name: str) -> bool:
    """
    Check if a MySQL database has at least one table.

    Args:
        db_name (str): Target database name.

    Returns:
        bool: True if the database has at least one table, False otherwise.
    """
    conn = mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        port=config.MYSQL_PORT,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    cursor.close()
    conn.close()
    return len(tables) > 0


def import_sql_to_mysql(sql_file: str, db_name: str):
    """
    Import a .sql file into MySQL, creating the database if necessary.

    Args:
        sql_file (str): Path to the .sql file.
        db_name (str): Target database name.
    """
    conn = mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        port=config.MYSQL_PORT
    )
    cursor = conn.cursor()

    # Create database if not exists and use it
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.execute(f"USE {db_name}")

    # Read SQL file
    sql_text = Path(sql_file).read_text(encoding="utf-8")

    # Replace any existing USE statements in the SQL file
    sql_text = re.sub(r"USE\s+\w+;", f"USE {db_name};", sql_text, flags=re.IGNORECASE)

    # Execute statements
    statements = sql_text.split(';')
    for statement in statements:
        stmt = statement.strip()
        if stmt:
            print(f"▶️ Executing: {stmt[:60]}...")
            try:
                cursor.execute(stmt)
            except mysql.connector.Error as err:
                print(f"⚠️ Error: {err}")

    conn.commit()
    cursor.close()
    conn.close()
    print(f"🎉 SQL file '{sql_file}' imported into database '{db_name}'.")


def ensure_mysql_data(db_name: str, sql_file: str):
    """
    Ensure that the MySQL database exists and is populated.
    If it does not exist or is empty, import it from the provided .sql file.

    Args:
        db_name (str): Target database name.
        sql_file (str): Path to the .sql file.
    """
    if not database_exists(db_name):
        print(f"⚠️ Database '{db_name}' not found. Importing from '{sql_file}'...")
        import_sql_to_mysql(sql_file, db_name)
    elif not database_has_tables(db_name):
        print(f"⚠️ Database '{db_name}' is empty. Importing from '{sql_file}'...")
        import_sql_to_mysql(sql_file, db_name)
    else:
        print(f"✅ Database '{db_name}' already exists and has tables. No action needed.")
