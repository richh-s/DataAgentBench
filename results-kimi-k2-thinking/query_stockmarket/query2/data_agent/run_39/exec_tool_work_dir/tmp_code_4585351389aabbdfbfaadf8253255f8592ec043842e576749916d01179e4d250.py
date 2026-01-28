code = """import json
import os

# Read the list of symbols from the first query result
symbols_result = locals()['var_functions.query_db:0']

# Check if it's a file path (string) or direct data
if isinstance(symbols_result, str) and os.path.exists(symbols_result):
    with open(symbols_result, 'r') as f:
        symbols_data = json.load(f)
else:
    symbols_data = symbols_result

# Extract the symbols (it's a list of dictionaries with 'Symbol' key)
etf_symbols = [item['Symbol'] for item in symbols_data]

print('__RESULT__:')
print(json.dumps({'etf_symbols': etf_symbols, 'count': len(etf_symbols)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
