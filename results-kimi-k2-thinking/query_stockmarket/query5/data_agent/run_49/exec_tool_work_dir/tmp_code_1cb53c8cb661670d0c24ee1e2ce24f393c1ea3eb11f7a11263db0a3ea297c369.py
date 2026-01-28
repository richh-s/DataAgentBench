code = """import json
import os
# Read the list of NASDAQ Capital Market stocks from the file path stored in var_functions.query_db:0
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    capital_market_stocks = json.load(f)
# Extract tickers
tickers = [rec['Symbol'] for rec in capital_market_stocks]
print('__RESULT__:')
print(json.dumps({'count': len(tickers), 'first_20': tickers[:20]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
