code = """import json
import pandas as pd
import re
import os

# Check what variables are available
available_vars = [k for k in locals().keys() if 'query_db' in str(k)]
print('Available variables:', available_vars)

# Find the actual variable names for our data
var_10 = None
var_12 = None

for k, v in locals().items():
    if '10' in str(k) and 'query_db' in str(k):
        var_10 = k
    if '12' in str(k) and 'query_db' in str(k):
        var_12 = k

print(f'Publication file var: {var_10}')
print(f'CPC file var: {var_12}')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
