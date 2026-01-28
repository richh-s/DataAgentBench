code = """import json

# Get list of NASDAQ Capital Market stocks from previous query
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

# Get list of available tables from stocktrade_database
result_file2 = var_functions.list_db:6
with open(result_file2, 'r') as f:
    all_tables = json.load(f)

# Find intersection
available_symbols = [sym for sym in nasdaq_cap_symbols if sym in all_tables]

print(f"Total NASDAQ Capital Market stocks: {len(nasdaq_cap_symbols)}")
print(f"Available in stocktrade_database: {len(available_symbols)}")
print(f"Sample available symbols: {available_symbols[:20]}")

# Store results
print('__RESULT__:')
print(json.dumps({
    'nasdaq_cap_symbols': nasdaq_cap_symbols,
    'available_symbols': available_symbols,
    'all_tables': all_tables,
    'count_available': len(available_symbols),
    'count_total': len(nasdaq_cap_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
