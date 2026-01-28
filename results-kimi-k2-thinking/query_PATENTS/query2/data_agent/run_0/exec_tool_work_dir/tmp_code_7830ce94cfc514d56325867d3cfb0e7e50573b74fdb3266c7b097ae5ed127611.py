code = """import pandas as pd
import json

# Load the query result from the JSON file file_path = var_functions.query_db:2"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
