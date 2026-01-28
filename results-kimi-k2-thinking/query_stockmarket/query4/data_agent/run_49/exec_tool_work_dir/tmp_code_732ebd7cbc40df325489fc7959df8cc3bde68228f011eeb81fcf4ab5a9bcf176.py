code = """import json
import os

# Read file paths
nyse_file = 'var_functions.query_db:16'
available_tickers_file = 'var_functions.list_db:6'

# Debug: check if files exist
print(f"NYSE file exists: {os.path.exists(nyse_file)}")
print(f"Tickers file exists: {os.path.exists(available_tickers_file)}")

# Load and process data
with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

with open(available_tickers_file, 'r') as f:
    available_tickers = json.load(f)

print(f"Loaded {len(nyse_stocks)} NYSE non-ETF stocks")
print(f"Loaded {len(available_tickers)} available tickers")

# Find intersection
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}
print(f"NYSE symbols (sample): {list(nyse_symbols)[:5]}")
print(f"Available tickers (sample): {available_tickers[:5]}")

common_stocks = nyse_symbols.intersection(available_tickers)
print(f"Found {len(common_stocks)} common stocks that exist in both databases")

# Create lookup for descriptions
symbol_to_desc = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Store results as JSON
result = {
    'common_stocks': list(common_stocks),
    'symbol_to_desc': symbol_to_desc,
    'count': len(common_stocks)
}

print('\n__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
