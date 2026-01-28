code = """import json
import os

# Read the full result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    etf_list = json.load(f)

# Extract symbols
symbols = [etf['Symbol'] for etf in etf_list]
print('__RESULT__:')
print(json.dumps({
    'symbol_count': len(symbols),
    'first_10_symbols': symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
