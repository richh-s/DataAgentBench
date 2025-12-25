from common_scaffold.tools.BaseTool import FatalError
from common_scaffold.tools.db_utils.db_config import serialize
import duckdb

"""
DuckDB config:
- db_type
- db_path
"""

def check_db_exists(db_path):
    try:
        with duckdb.connect(database=str(db_path), read_only=True) as conn:
            # Simple query to check if the database is accessible
            conn.execute("SELECT 1;")
            return True
    except Exception as e:
        raise FatalError(f"DuckDB existence check error ({type(e).__name__}): {str(e)}")

class DuckdbQueryDBTool:
    @staticmethod
    def check_args(db_client, query):
        if 'db_path' not in db_client:
            raise FatalError(f"Missing `db_path` for duckdb db_client: {db_client}")
        
        return {
            "db_path": db_client["db_path"],
            "sql": query
        }

    @staticmethod
    def exec(db_path, sql):
        with duckdb.connect(database=str(db_path), read_only=True) as conn:
            try:
                result_df = conn.execute(sql).fetchdf()
            except Exception as e:
                raise ValueError(f"DuckDB query execution error ({type(e).__name__}): {str(e)}")
        return serialize(result_df)
            

class DuckdbListDBTool:
    @staticmethod
    def check_args(db_client):
        if 'db_path' not in db_client:
            raise FatalError(f"Missing `db_path` for duckdb db_client: {db_client}")
        
        return {
            "db_path": db_client["db_path"],
            "query": """SELECT table_name\nFROM information_schema.tables\nWHERE table_schema = 'main';\n"""
        }
    

    @staticmethod
    def exec(db_path, query):
        with duckdb.connect(database=str(db_path), read_only=True) as conn:
            try:
                result_df = conn.execute(query).fetchdf()
                return result_df.iloc[:, 0].tolist()
            except Exception as e:
                raise FatalError(f"DuckDB list tables execution error ({type(e).__name__}): {str(e)}")