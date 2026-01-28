code = """import os, json

# Get file path from variable
f1 = str(var_functions.query_db:0)
print('Funding file path:', f1)

# List files in current directory to check paths
print('Current files:', os.listdir('.'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
