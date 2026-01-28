code = """import json

# Get the results from storage using the provided keys
# Note: The variables are already available in the Python environment
# Let's check what's available
print("Checking variables...")
print([name for name in globals().keys() if name.startswith('var')])

# Try to access the variables directly
nasdaq_cap_stocks = var_functions.query_db_0
all_tables = var_functions.list_db_6

nasdaq_cap_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]

# Find intersection
available_symbols = [sym for sym in nasdaq_cap_symbols if sym in all_tables]

print(f"Total NASDAQ Capital Market stocks: {len(nasdaq_cap_symbols)}")
print(f"Available in stocktrade_database: {len(available_symbols)}")
print(f"Sample available symbols: {available_symbols[:20]}")

# Store results
result = {
    'nasdaq_cap_symbols': nasdaq_cap_symbols,
    'available_symbols': available_symbols,
    'company_names': {stock['Symbol']: stock.get('Company Description', '') for stock in nasdaq_cap_stocks},
    'count_available': len(available_symbols),
    'count_total': len(nasdaq_cap_symbols)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
