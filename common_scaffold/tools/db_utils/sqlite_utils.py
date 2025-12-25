import sqlite3
import pandas as pd
from common_scaffold.tools.BaseTool import FatalError
from common_scaffold.tools.db_utils.db_config import serialize

"""
Sqlite config:
- db_type
- db_path
"""

def check_db_exists(db_path):
    try:
        with sqlite3.connect(db_path) as conn:
            # Simple query to check if the database is accessible
            conn.execute("SELECT 1;")
            return True
    except Exception as e:
        raise FatalError(f"SQLite existence check error ({type(e).__name__}): {str(e)}")

class SqliteQueryDBTool:
    @staticmethod
    def check_args(db_client, query):
        if 'db_path' not in db_client:
            raise FatalError(f"Missing `db_path` for sqlite db_client: {db_client}")
        
        return {
            "db_path": db_client["db_path"],
            "sql": query
        }
    
    @staticmethod
    def exec(db_path, sql):
        uri = f"file:{db_path}?mode=ro"
        with sqlite3.connect(uri, uri=True) as conn:
            try:
                result_df = pd.read_sql_query(sql, conn)
            except Exception as e:
                raise ValueError(f"SQLite query execution error ({type(e).__name__}): {str(e)}")
        return serialize(result_df)
            

class SqliteListDBTool:
    @staticmethod
    def check_args(db_client):
        if 'db_path' not in db_client:
            raise FatalError(f"Missing `db_path` for sqlite db_client: {db_client}")
        
        return {
            "db_path": db_client["db_path"],
            "query": """SELECT name FROM sqlite_master WHERE type='table';"""
        }
    
    @staticmethod
    def exec(db_path, query):
        uri = f"file:{db_path}?mode=ro"
        with sqlite3.connect(uri, uri=True) as conn:
            try:
                result_df = pd.read_sql_query(query, conn)
                return result_df.iloc[:, 0].tolist()
            except Exception as e:
                raise FatalError(f"SQLite list tables execution error ({type(e).__name__}): {str(e)}")