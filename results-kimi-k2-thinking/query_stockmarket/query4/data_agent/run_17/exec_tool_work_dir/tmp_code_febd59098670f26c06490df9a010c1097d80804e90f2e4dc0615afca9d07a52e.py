code = """import json

# Read the full results from file
with open('var_functions.query_db:18', 'r') as f:
    nyse_stocks = json.load(f)

print(f'Total NYSE non-ETF stocks: {len(nyse_stocks)}')
print('First 10 stocks:')
for i, stock in enumerate(nyse_stocks[:10]):
    print(f"  {i+1}. {stock['Symbol']}: {stock['Company Description'][:60]}...")

# Extract symbols
symbols = [s['Symbol'] for s in nyse_stocks]
print(f'\nExtracted {len(symbols)} symbols')

# Get first 20 symbols to work with
print('\nFirst 20 symbols:')
print(symbols[:20])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'symbols': [], 'metadata': []}, 'var_functions.query_db:14': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}, {'Symbol': 'AIV'}, {'Symbol': 'AIZP'}, {'Symbol': 'AJRD'}, {'Symbol': 'AL'}, {'Symbol': 'AMN'}, {'Symbol': 'AMP'}, {'Symbol': 'AMT'}, {'Symbol': 'ARD'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
