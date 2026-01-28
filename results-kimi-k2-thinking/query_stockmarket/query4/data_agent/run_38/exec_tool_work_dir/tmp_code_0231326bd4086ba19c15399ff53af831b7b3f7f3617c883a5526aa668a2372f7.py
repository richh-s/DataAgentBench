code = """import json

# Read the result from the previous query
with open('var_functions.query_db:0', 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'count': len(symbols),
    'sample_symbols': symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
