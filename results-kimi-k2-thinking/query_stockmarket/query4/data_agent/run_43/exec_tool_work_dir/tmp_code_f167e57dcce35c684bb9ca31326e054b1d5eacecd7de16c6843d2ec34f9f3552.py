code = """import json
import os

# Load NYSE stocks
nyse_file = locals()['var_functions.query_db:0']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create a dictionary mapping symbols to company descriptions
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Get all available tables
all_tables_file = locals()['var_functions.list_db:2']
with open(all_tables_file, 'r') as f:
    all_tables = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'message': 'Data loaded successfully',
    'sample_symbols': list(symbol_to_company.keys())[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:8': {'total_nyse_stocks': 234, 'available_tables': 2753, 'common_symbols': 234}}

exec(code, env_args)
