code = """import json

# Read the full result from the first query
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({'count': len(symbols), 'first_10': symbols[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json'}

exec(code, env_args)
