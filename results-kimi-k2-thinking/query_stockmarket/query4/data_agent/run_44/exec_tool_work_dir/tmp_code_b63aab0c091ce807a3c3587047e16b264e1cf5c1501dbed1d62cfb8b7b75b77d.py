code = """import json

# Read the full result from the JSON file
result_path = locals()['var_functions.query_db:2']
with open(result_path, 'r') as f:
    nyse_stocks = json.load(f)

# Create a dictionary mapping symbols to company names
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
symbols = list(symbol_to_company.keys())

print('__RESULT__:')
print(json.dumps({'symbol_count': len(symbols), 'sample_symbols': symbols[:10]}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 234, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
