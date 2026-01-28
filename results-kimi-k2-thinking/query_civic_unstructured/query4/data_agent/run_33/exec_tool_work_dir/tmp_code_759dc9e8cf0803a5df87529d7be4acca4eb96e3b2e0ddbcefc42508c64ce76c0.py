code = """import json
import pandas as pd

# Try direct file access
funding_path = 'var_functions.query_db_12_json'
civic_path = 'var_functions.query_db_20_json'

print('Checking file format...')

# Check which files we have
import os
print('Files in working directory:', os.listdir('.'))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:26': ['civic_docs']}

exec(code, env_args)
