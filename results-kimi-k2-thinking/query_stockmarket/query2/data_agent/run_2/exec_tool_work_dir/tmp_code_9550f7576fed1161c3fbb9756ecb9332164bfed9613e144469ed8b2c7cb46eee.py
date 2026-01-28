code = """import json
import os

# Read the ETF list from the file
filepath = 'file_storage/functions.query_db:0.json'
with open(filepath, 'r') as f:
    etf_list = json.load(f)

# Extract symbols
symbols = [etf['Symbol'] for etf in etf_list]
print('First 10 symbols:', symbols[:10])
print(f'Total symbols: {len(symbols)}')

print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
