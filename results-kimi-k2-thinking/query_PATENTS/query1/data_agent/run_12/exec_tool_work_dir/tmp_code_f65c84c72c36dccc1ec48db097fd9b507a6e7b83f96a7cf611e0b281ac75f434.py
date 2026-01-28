code = """import json
import pandas as pd
from datetime import datetime
import re
import os

# Get all available variables to see what's accessible
available_vars = [k for k in locals().keys() if 'var_functions' in k]
print('Available variables:', available_vars)

# Try different approaches to access the data
try:
    # Try to access the CPC level 5 data
    cpc_var = 'var_functions.query_db:8'
    if cpc_var in locals():
        cpc_file = locals()[cpc_var]
        print('Found CPC file:', cpc_file)
        with open(cpc_file, 'r') as f:
            cpc_data = json.load(f)
        print('CPC Level 5 symbols loaded:', len(cpc_data))
        level5_symbols = set(item['symbol'] for item in cpc_data)
        print('Sample symbols:', list(level5_symbols)[:10])
    else:
        print('CPC variable not in locals')
except Exception as e:
    print('Error with CPC data:', e)

try:
    # Try to access the publication data
    pub_var = 'var_functions.query_db:22'
    if pub_var in locals():
        pub_file = locals()[pub_var]
        print('Found publication file:', pub_file)
        with open(pub_file, 'r') as f:
            pub_data = json.load(f)
        print('Publication records loaded:', len(pub_data))
        print('Sample record keys:', list(pub_data[0].keys()) if pub_data else 'No data')
    else:
        print('Publication variable not in locals')
except Exception as e:
    print('Error with publication data:', e)

print('__RESULT__:')
print(json.dumps({'status': 'exploration complete'}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
