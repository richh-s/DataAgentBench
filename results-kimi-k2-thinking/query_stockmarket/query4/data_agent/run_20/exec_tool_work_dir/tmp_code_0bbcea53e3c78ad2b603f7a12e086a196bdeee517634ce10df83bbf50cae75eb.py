code = """import json

# Load the result from the previous query
with open('var_functions.query_db:2', 'r') as f:
    nyse_stocks = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'count': len(nyse_stocks),
    'first_10': nyse_stocks[:10],
    'symbols': [s['Symbol'] for s in nyse_stocks]
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
