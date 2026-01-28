code = """import json

# Access the stored result
etf_symbols_data = locals()['var_functions.query_db:0']

# Extract just the symbols
etf_symbols = [item['Symbol'] for item in etf_symbols_data]

print('__RESULT__:')
print(json.dumps(etf_symbols[:20]))  # Print first 20 to verify"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
