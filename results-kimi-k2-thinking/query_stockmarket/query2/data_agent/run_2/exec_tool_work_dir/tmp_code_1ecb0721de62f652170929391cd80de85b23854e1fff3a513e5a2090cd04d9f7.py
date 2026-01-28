code = """import json

# Access the result from the first query directly from locals using the key
etf_list = locals()['var_functions.query_db:0']

# Extract all ticker symbols
symbols = [etf['Symbol'] for etf in etf_list]
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
