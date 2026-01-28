code = """import json
import re

# Debug: Check what variables are available
available_vars = []
for key in dir():
    if 'functions.query_db' in str(key):
        available_vars.append(str(key))
print('Available vars: ' + str(available_vars[:10]))

# Try to access the data from the storage keys
try:
    civic_docs = var_functions.query_db:16
    print('Loaded civic docs directly, count: ' + str(len(civic_docs)))
except:
    print('Could not load civic docs directly')

try:
    funding_data = var_functions.query_db:17
    print('Loaded funding data directly, count: ' + str(len(funding_data)))
except:
    print('Could not load funding data directly')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
