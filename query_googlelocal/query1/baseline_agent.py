"""
MySQL + SQLite baseline agent.
Ensures both databases are ready, lists tables,
and previews the first few records from each.
"""

import sys
import pandas as pd
from pathlib import Path

# Add common_scaffold to Python path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from common_scaffold.db_utils.loader import (
    ensure_db,
    list_entities,
    query_db
)


def main():
    """
    Main execution function.
    Handles MySQL & SQLite:
      - Ensures MySQL is ready
      - Lists MySQL tables
      - Queries sample data from MySQL
      - Lists SQLite tables
      - Queries sample data from SQLite
    """
    # Configure pandas display options
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_rows', 20)

    # === MySQL ===
    db_name_mysql = "googlelocal_db"
    sql_file_mysql = "../query_dataset/business_description.sql"

    print("\n=== MySQL: Ensuring database is initialized ===")
    ensure_db(
        db_type="mysql",
        db_name=db_name_mysql,
        sql_file=sql_file_mysql
    )

    print("\n=== MySQL: Listing tables ===")
    df_tables_mysql = list_entities(
        db_type="mysql",
        db=db_name_mysql
    )
    if df_tables_mysql.empty:
        print("⚠️ MySQL database has no tables!")
    else:
        print(df_tables_mysql)

    # Preview each MySQL table
    for table in df_tables_mysql.iloc[:, 0]:
        print(f"\n=== MySQL: Preview of table: {table} ===")
        df_sample = query_db(
            db_type="mysql",
            db=db_name_mysql,
            sql=f"SELECT * FROM {table} LIMIT 5;"
        )
        print(df_sample)

    # === SQLite ===
    db_path_sqlite = "../query_dataset/review_query.db"

    print("\n=== SQLite: Listing tables ===")
    df_tables_sqlite = list_entities(
        db_type="sqlite",
        db_path=db_path_sqlite
    )
    if df_tables_sqlite.empty:
        print("⚠️ SQLite database has no tables!")
    else:
        print(df_tables_sqlite)

    # Preview each SQLite table
    for table in df_tables_sqlite["name"]:
        print(f"\n=== SQLite: Preview of table: {table} ===")
        df_sample = query_db(
            db_type="sqlite",
            db_path=db_path_sqlite,
            sql=f"SELECT * FROM {table} LIMIT 5;"
        )
        print(df_sample)


if __name__ == "__main__":
    main()
