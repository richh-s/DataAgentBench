code = """import json
import os

# Get the file path from the storage variable
funding_file_path = var_functions.query_db:2
civic_docs_file_path = var_functions.query_db:8

# Check if files exist
print('Funding file exists:', os.path.exists(funding_file_path))
print('Civic docs file exists:', os.path.exists(civic_docs_file_path))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
