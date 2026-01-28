code = """import json
# Read the list of NYSE non-ETF symbols
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    stock_data = json.load(f)

symbols = [stock['Symbol'] for stock in stock_data]
print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'count': len(symbols)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:4': {'count': 234}}

exec(code, env_args)
