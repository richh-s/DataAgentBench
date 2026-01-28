code = """import json

# Read the full result from the previous query
with open('var_functions.query_db:8.json', 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols and company descriptions
symbols = [stock['Symbol'] for stock in nyse_stocks]
company_names = [stock['Company Description'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'count': len(symbols),
    'first_symbols': symbols[:10],
    'total_symbols': len(symbols)
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
