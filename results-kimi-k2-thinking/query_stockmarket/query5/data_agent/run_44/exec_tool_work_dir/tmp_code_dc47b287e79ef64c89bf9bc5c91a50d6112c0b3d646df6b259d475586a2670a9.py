code = """import json

# Access the stored results
stocktrade_result = locals()['var_functions.list_db:0']
stockinfo_result = locals()['var_functions.query_db:2']

# If results are file paths (strings), load them
if isinstance(stocktrade_result, str) and stocktrade_result.endswith('.json'):
    with open(stocktrade_result, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = stocktrade_result

if isinstance(stockinfo_result, str) and stockinfo_result.endswith('.json'):
    with open(stockinfo_result, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = stockinfo_result

# Extract tickers from NASDAQ Capital Market stocks
nasdaq_cap_tickers = [row['Symbol'] for row in stockinfo_data]

# Filter for tickers that exist as tables in stocktrade_database
valid_tickers = [ticker for ticker in nasdaq_cap_tickers if ticker in trade_tables]

print(f'Found {len(valid_tickers)} NASDAQ Capital Market tickers with trade data')
print('__RESULT__:')
print(json.dumps(valid_tickers[:20]))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
