code = """import json

# Access the result from storage (it's a file path)
result_key = 'var_functions.query_db:0'
result_file = locals()[result_key]

# Read the full result from the file
with open(result_file, 'r') as f:
    etf_list = json.load(f)

# Extract symbols
symbols = [etf['Symbol'] for etf in etf_list]

# Print result in required format
print('__RESULT__:')
print(json.dumps({
    'symbol_count': len(symbols),
    'first_10_symbols': symbols[:10],
    'all_symbols': symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
