code = """import json
import os

# Find the data files
tmp_dir = '/tmp'
files = os.listdir(tmp_dir)
print('Files in /tmp:', files)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
