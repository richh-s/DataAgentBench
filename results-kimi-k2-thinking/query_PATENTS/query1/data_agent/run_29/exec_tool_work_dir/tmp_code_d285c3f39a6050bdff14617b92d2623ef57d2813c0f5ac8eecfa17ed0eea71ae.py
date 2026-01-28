code = """import json
import pandas as pd
import numpy as np

# Load level 5 CPC symbols
level5_symbols_var = locals()['var_functions.query_db:24']
if isinstance(level5_symbols_var, str):
    with open(level5_symbols_var, 'r') as f:
        level5_symbols_data = json.load(f)
else:
    level5_symbols_data = level5_symbols_var

level5_symbols = [record['symbol'] for record in level5_symbols_data]
print('Loaded ' + str(len(level5_symbols)) + ' level 5 CPC symbols')

# Load CPC year counts data
cpc_analysis_var = locals()['var_functions.execute_python:22']
if isinstance(cpc_analysis_var, str):
    with open(cpc_analysis_var, 'r') as f:
        cpc_analysis = json.load(f)
else:
    cpc_analysis = cpc_analysis_var

cpc_year_counts_str = cpc_analysis['cpc_year_counts']
years = cpc_analysis['years']

print('Years available: ' + str(years))
print('Sample data from cpc_year_counts:')
count = 0
for key, val in cpc_year_counts_str.items():
    print('  ' + key + ': ' + str(val))
    count += 1
    if count >= 5:
        break

result = {
    'level5_symbols_count': len(level5_symbols),
    'years': years,
    'sample_cpc_counts': dict(list(cpc_year_counts_str.items())[:5])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.query_db:16': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
