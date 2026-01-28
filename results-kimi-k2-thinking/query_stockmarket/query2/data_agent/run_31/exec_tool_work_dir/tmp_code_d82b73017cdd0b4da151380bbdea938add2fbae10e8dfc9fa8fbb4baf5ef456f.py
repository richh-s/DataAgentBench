code = """import json

# Access the result from the previous query using the storage key
etf_symbols = locals()['var_functions.query_db:8']

# Extract just the symbols into a list
symbols = [etf['Symbol'] for etf in etf_symbols]

print('__RESULT__:')
print(json.dumps({'total_symbols': len(symbols), 'sample_symbols': symbols[:20]}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
