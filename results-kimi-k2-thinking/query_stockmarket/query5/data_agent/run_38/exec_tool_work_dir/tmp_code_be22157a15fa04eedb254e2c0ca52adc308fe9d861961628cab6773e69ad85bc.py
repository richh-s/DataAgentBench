code = """import json
import re

# Read the stock info data
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

# Extract tickers from NASDAQ Capital Market
tickers_capital = set([item['Symbol'] for item in stockinfo_data])

# Read the table names from stocktrade database
trade_tables_path = locals()['var_functions.list_db:6']
with open(trade_tables_path, 'r') as f:
    trade_tables = json.load(f)

# Convert to set for intersection
trade_tickers = set(trade_tables)

# Find intersection - tickers that exist in both databases
common_tickers = list(tickers_capital.intersection(trade_tickers))

print('__RESULT__:')
print(json.dumps({
    'total_capital_market': len(tickers_capital),
    'total_trade_tables': len(trade_tickers),
    'common_tickers_count': len(common_tickers),
    'sample_common': common_tickers[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
