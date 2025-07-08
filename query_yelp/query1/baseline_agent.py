"""
MongoDB + DuckDB baseline agent.
This script ensures both databases are ready, lists collections/tables,
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
    Handles MongoDB & DuckDB:
      - Ensures MongoDB is ready
      - Lists MongoDB collections
      - Queries sample data from MongoDB
      - Lists DuckDB tables
      - Queries sample data from DuckDB
    """
    # Configure pandas display options
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_rows', 20)

    # === MongoDB ===
    db_name_mongo = "yelp_db"
    dump_folder = "../query_dataset/yelp_business"

    print("\n=== MongoDB: Ensuring database is initialized ===")
    ensure_db(
        db_type="mongo",
        db_name=db_name_mongo,
        dump_folder=dump_folder
    )

    print("\n=== MongoDB: Listing collections ===")
    collections = list_entities(
        db_type="mongo",
        db_name=db_name_mongo
    )
    print(collections)

    for collection in collections:
        print(f"\n=== MongoDB: Preview of collection: {collection} ===")
        df_sample = query_db(
            db_type="mongo",
            db_name=db_name_mongo,
            collection=collection,
            query={},   # Empty filter
            limit=5
        )
        print(df_sample)

    # === DuckDB ===
    db_path_duckdb = "../query_dataset/yelp_user.db"

    print("\n=== DuckDB: Listing tables ===")
    df_tables = list_entities(
        db_type="duckdb",
        db_path=db_path_duckdb
    )
    print(df_tables)

    for table in df_tables["table_name"]:
        print(f"\n=== DuckDB: Preview of table: {table} ===")
        df_sample = query_db(
            db_type="duckdb",
            db_path=db_path_duckdb,
            sql=f"SELECT * FROM {table} LIMIT 5;"
        )
        print(df_sample)


if __name__ == "__main__":
    main()
