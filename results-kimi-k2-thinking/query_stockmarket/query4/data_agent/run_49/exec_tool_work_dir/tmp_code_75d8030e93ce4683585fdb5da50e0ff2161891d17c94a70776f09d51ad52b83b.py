code = """import json
import os

nyse_file = 'var_functions.query_db:22'
tickers_file = 'var_functions.list_db:6'

# Debug: check file size
print(f'NYSE file size: {os.path.getsize(nyse_file)} bytes')
print(f'Tickers file size: {os.path.getsize(tickers_file)} bytes')

# Read NYSE data
nyse_stocks = []
with open(nyse_file, 'r') as f:
    for line in f:
        nyse_stocks.append(json.loads(line.strip()))

# Read available tickers  
available_tickers = []
with open(tickers_file, 'r') as f:
    for line in f:
        available_tickers.append(json.loads(line.strip()))

print(f'Loaded {len(nyse_stocks)} NYSE stocks')
print(f'Loaded {len(available_tickers)} available tickers')

# Convert to sets for comparison
nyse_symbols = {stock['Symbol'] for stock in nyse_stocks}
available_set = set(available_tickers)

# Find intersection
common_symbols = nyse_symbols.intersection(available_set)
print(f'Common symbols: {len(common_symbols)}')

# Show first 10
ticker_to_desc = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
first_10 = sorted(list(common_symbols))[:10]
print('\nFirst 10 common stocks:')
for i, sym in enumerate(first_10, 1):
    desc = ticker_to_desc[sym]
    print(f'{i}. {sym}: {desc[:60]}...')

# Output results
print('\n__RESULT__:')
print(json.dumps({
    'common_count': len(common_symbols),
    'common_symbols': list(common_symbols),
    'ticker_to_desc': ticker_to_desc
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
