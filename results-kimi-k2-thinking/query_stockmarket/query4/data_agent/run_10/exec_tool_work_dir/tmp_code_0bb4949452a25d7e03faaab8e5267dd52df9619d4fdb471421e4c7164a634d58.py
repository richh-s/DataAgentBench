code = """import json
import os

# Load actual data from the JSON files
nyse_stocks_file = locals()['var_functions.query_db:0']
available_tables_file = locals()['var_functions.list_db:2']

with open(nyse_stocks_file, 'r') as f:
    nyse_stocks = json.load(f)

with open(available_tables_file, 'r') as f:
    available_tables = json.load(f)

# Extract symbols from NYSE stocks
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}

# Find intersection - stocks that are both NYSE non-ETF and have data available
common_stocks = nyse_symbols.intersection(available_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_stocks),
    'total_available_tables': len(available_tables),
    'common_stocks_count': len(common_stocks),
    'sample_common_stocks': sorted(list(common_stocks))[:20]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
