code = """import json

# Load NYSE stocks data
file_path = var_functions.query_db:7
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Extract symbols
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(nyse_symbols),
    'sample_symbols': nyse_symbols[:10]
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.execute_python:5': 2753, 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
