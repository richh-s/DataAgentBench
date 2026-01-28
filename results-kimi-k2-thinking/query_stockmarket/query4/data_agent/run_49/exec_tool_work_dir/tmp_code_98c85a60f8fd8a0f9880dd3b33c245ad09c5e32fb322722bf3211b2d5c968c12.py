code = """import json
import os

# Read files
with open('var_functions.query_db:10', 'r') as f:
    nyse_data = json.load(f)

with open('var_functions.list_db:6', 'r') as f:
    available_tickers = json.load(f)

# Create lookup dictionaries
nyse_symbols = {item['Symbol'] for item in nyse_data}
available_set = set(available_tickers)

# Find intersection
common_symbols = nyse_symbols.intersection(available_set)
print(f'Total NYSE non-ETF stocks: {len(nyse_data)}')
print(f'Total available tickers: {len(available_tickers)}')
print(f'Common stocks: {len(common_symbols)}')

# Show first 10 common stocks
symbol_to_description = {item['Symbol']: item['Company Description'] for item in nyse_data}
print('\nFirst 10 common stocks:')
count = 0
for sym in sorted(list(common_symbols))[:10]:
    count += 1
    desc = symbol_to_description[sym]
    print(f'{count}. {sym}: {desc[:60]}...')

# Output results as JSON
print('\n__RESULT__:')
print(json.dumps({
    'common_symbols': list(common_symbols),
    'symbol_to_description': symbol_to_description
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
