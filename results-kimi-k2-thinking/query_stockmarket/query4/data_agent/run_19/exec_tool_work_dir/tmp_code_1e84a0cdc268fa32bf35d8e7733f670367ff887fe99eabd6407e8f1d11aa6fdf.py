code = """import json
import os

# Read the file containing NYSE non-ETF stocks
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols and company names
stock_symbols = [(stock['Symbol'], stock['Company Description']) for stock in nyse_stocks]
print('__RESULT__:')
print(json.dumps({
    'count': len(stock_symbols),
    'first_10': stock_symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
