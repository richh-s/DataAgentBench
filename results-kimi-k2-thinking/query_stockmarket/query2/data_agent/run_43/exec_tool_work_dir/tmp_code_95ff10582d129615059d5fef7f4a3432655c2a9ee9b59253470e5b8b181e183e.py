code = """import json

# Access the stored result directly using the variable name
etf_symbols = locals()['var_functions.query_db:0']

# Extract just the symbols
symbols = [item['Symbol'] for item in etf_symbols]
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
