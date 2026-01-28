code = """import json
import os

# First, let's get all the NASDAQ Capital Market symbols and their company descriptions
symbols_result = locals()['var_functions.query_db:0']

# If it's a file path, read it
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    nasdaq_cap_stocks = symbols_result

# Create a dictionary mapping symbol to company description
symbol_to_company = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_stocks}

print('__RESULT__:')
print(json.dumps(list(symbol_to_company.items())[:10]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
