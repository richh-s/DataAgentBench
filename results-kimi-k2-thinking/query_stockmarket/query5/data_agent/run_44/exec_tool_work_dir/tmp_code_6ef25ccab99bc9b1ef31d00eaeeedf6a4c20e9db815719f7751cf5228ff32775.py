code = """import json
import os

# Read the file paths from storage
stockinfo_file = var_functions.query_db_2
stocktrade_file = var_functions.list_db_0

# Load the data
with open(stockinfo_file, 'r') as f:
    stockinfo_result = json.load(f)

with open(stocktrade_file, 'r') as f:
    trade_tables = json.load(f)

# Extract tickers from stockinfo
nasdaq_cap_tickers = [row['Symbol'] for row in stockinfo_result]

# Filter for tickers that exist as tables in stocktrade_database
valid_tickers = [ticker for ticker in nasdaq_cap_tickers if ticker in trade_tables]

print(f'Found {len(valid_tickers)} NASDAQ Capital Market tickers with trade data')
print('__RESULT__:')
print(json.dumps(valid_tickers[:20]))  # Print first 20 for inspection"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
