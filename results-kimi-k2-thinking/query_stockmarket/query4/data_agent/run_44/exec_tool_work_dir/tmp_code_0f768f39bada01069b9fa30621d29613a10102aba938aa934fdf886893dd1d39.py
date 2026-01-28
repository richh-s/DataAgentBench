code = """import json

# Read NYSE symbols
nyse_path = locals()['var_functions.query_db:2']
with open(nyse_path, 'r') as f:
    nyse_stocks = json.load(f)

symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
nyse_symbols = set(symbol_to_company.keys())

# Read all tables from stocktrade_database
all_tables_path = locals()['var_functions.list_db:8']
with open(all_tables_path, 'r') as f:
    all_tables = json.load(f)

# Find intersection
available_symbols = nyse_symbols.intersection(set(all_tables))
print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'available_in_trade_db': len(available_symbols),
    'sample_available': list(available_symbols)[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 234, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': {'symbol_count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
