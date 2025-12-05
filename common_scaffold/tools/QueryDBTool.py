from common_scaffold.tools.BaseTool import BaseTool, FatalError
import common_scaffold.tools.db_utils.duckdb_utils as duckdb_utils
import common_scaffold.tools.db_utils.mongo_utils as mongo_utils
import common_scaffold.tools.db_utils.postgres_utils as postgres_utils
import common_scaffold.tools.db_utils.sqlite_utils as sqlite_utils
from common_scaffold.tools.db_utils.db_config import load_db_clients
import logging

class QueryDBTool(BaseTool):
    def __init__(self, log_path, name, db_config_path, check_load=True):
        super().__init__(log_path, name)
        self.logger = logging.getLogger(__name__)
        self.db_config_path = db_config_path
        self.db_clients = load_db_clients(db_config_path)
        self.logger.info(f"\tdb_config:")
        for db_name, db_client in self.db_clients.items():
            db_type = db_client['db_type']
            self.logger.info(f"\t\t{db_name} ({db_type})")
        # Load DBs
        if check_load:
            for db_client in self.db_clients.values():
                db_type = db_client['db_type']
                if db_type == "mongo":
                    mongo_utils.load_db(db_client['dump_folder'], db_client['db_name'])
                elif db_type == "postgres":
                    postgres_utils.load_db(db_client['sql_file'], db_client['db_name'])
    
    def to_dict(self):
        return super().to_dict().update({
            "db_clients": self.db_clients,
            "db_config_path": self.db_config_path,
        })

    def get_spec(self):
        spec = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Execute a query (SQL or MongoDB query) on a specific database and return the result as a list of records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "db_name": {
                            "type": "string",
                            "description": "Logical name of the database you want to query."
                        },
                        "query": {
                            "type": "string",
                            "description": "The query to execute. For SQL databases, provide a SQL query string. For MongoDB, provide a JSON string representing the query, including `collection` field, and optional `filter`, `projection`, and `limit` fields."
                        }
                    },
                    "required": ["db_name", "query"]
                }
            }
        }
        return spec

    def clean_up(self):
        super().clean_up()
        for db_client in self.db_clients.values():
            db_type = db_client['db_type']
            if db_type == "mongo":
                mongo_utils.clean_up(db_client['db_name'])
            elif db_type == "postgres":
                postgres_utils.clean_up(db_client['db_name'])
        return

    def _check_args(self, args: dict):
        args = super()._check_args(args)
        # required: db_name, query
        if "db_name" not in args:
            raise ValueError("Missing required argument: `db_name`")
        if not isinstance(args["db_name"], str):
            raise ValueError(f"`db_name` must be a string, got {type(args['db_name']).__name__}")
        db_name = args["db_name"]
        if db_name not in self.db_clients:
            raise ValueError(f"Unknown `db_name`: {db_name}")
        
        if "query" not in args:
            raise ValueError("Missing required argument: `query`")
        if not isinstance(args["query"], str):
            raise ValueError(f"`query` must be a string, got {type(args['query']).__name__}")
        

        db_client = self.db_clients[db_name]
        query = args["query"]

        if db_client['db_type'] == "duckdb":
            exec_args = duckdb_utils.DuckdbQueryDBTool.check_args(db_client, query)
        elif db_client['db_type'] == "mongo":
            exec_args = mongo_utils.MongoQueryDBTool.check_args(db_client, query)
        elif db_client['db_type'] == "sqlite":
            exec_args = sqlite_utils.SqliteQueryDBTool.check_args(db_client, query)
        elif db_client['db_type'] == "postgres":
            exec_args = postgres_utils.PostgresQueryDBTool.check_args(db_client, query)
        else:
            raise FatalError(f"Unsupported db_type: {db_client['db_type']}")
        
        return {
            "db_type": db_client['db_type'],
            "exec_args": exec_args
        }
    
    def _exec(self, args):
        db_type = args["db_type"]
        exec_args = args["exec_args"]
        super()._exec(exec_args)
        if db_type == "duckdb":
            return duckdb_utils.DuckdbQueryDBTool.exec(**exec_args)
        elif db_type == "mongo":
            return mongo_utils.MongoQueryDBTool.exec(**exec_args)
        elif db_type == "sqlite":
            return sqlite_utils.SqliteQueryDBTool.exec(**exec_args)
        elif db_type == "postgres":
            return postgres_utils.PostgresQueryDBTool.exec(**exec_args)
        else:
            raise FatalError(f"Unsupported db_type: {db_type}")