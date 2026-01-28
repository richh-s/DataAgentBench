code = """import json

# Read the list of tables from stocktrade database
result_file = locals()['var_functions.list_db:2']
with open(result_file, 'r') as f:
    all_tables = json.load(f)

# Read NYSE stocks
nyse_file = locals()['var_functions.query_db:0']
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
nyse_symbols = set([stock['Symbol'] for stock in nyse_stocks])
available_tables = set(all_tables)

# Find intersection
common_symbols = nyse_symbols.intersection(available_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'available_tables': len(available_tables),
    'common_symbols': len(common_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 234, 'first_10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
