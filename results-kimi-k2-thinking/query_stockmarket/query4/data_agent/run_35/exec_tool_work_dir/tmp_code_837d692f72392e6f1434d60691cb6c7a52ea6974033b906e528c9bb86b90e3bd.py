code = """import json
import os

# Load the stockinfo results
stockinfo_var = locals().get('var_functions.query_db:0')
if isinstance(stockinfo_var, str) and stockinfo_var.endswith('.json'):
    with open(stockinfo_var, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = stockinfo_var if isinstance(stockinfo_var, list) else []

# Load the tables list
tables_var = locals().get('var_functions.list_db:2')
if isinstance(tables_var, str) and tables_var.endswith('.json'):
    with open(tables_var, 'r') as f:
        tables_data = json.load(f)
else:
    tables_data = tables_var if isinstance(tables_var, list) else []

# Get NYSE non-ETF stock symbols
nyse_symbols = [stock['Symbol'] for stock in stockinfo_data]
tables_set = set(tables_data)

# Find which NYSE stocks have trading data
available_stocks = [sym for sym in nyse_symbols if sym in tables_set]

result = {
    'nyse_count': len(nyse_symbols),
    'available_count': len(available_stocks),
    'sample_symbols': nyse_symbols[:10],
    'sample_available': available_stocks[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
