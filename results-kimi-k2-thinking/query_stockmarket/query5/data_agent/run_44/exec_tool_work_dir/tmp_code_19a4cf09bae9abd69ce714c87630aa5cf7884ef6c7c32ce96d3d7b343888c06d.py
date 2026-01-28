code = """import json
import os

# Read the list of tickers from stockinfo_database
with open('/tmp/stockinfo_stocks.json', 'r') as f:
    stockinfo_result = json.load(f)

# Read the list of table names from stocktrade_database
with open('/tmp/stocktrade_tables.json', 'r') as f:
    trade_tables = json.load(f)

# Extract tickers from stockinfo
nasdaq_cap_tickers = [row['Symbol'] for row in stockinfo_result]

# Filter for tickers that exist as tables in stocktrade_database
valid_tickers = [ticker for ticker in nasdaq_cap_tickers if ticker in trade_tables]

print('__RESULT__:')
print(json.dumps(valid_tickers[:10]))  # Print first 10 for inspection"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
