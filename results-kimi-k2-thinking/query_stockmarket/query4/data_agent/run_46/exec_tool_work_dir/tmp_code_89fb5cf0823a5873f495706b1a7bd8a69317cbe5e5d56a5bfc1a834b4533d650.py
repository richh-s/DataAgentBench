code = """import json

# Read the results from the file
file_path = 'file_storage/functions.query_db:0.json'
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Extract the symbols and company descriptions
symbols = [stock['Symbol'] for stock in nyse_stocks]
company_names = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

print('__RESULT__:')
print(json.dumps({
    'total_nyse_stocks': len(symbols),
    'first_10_stocks': symbols[:10],
    'sample_company_names': {symbols[i]: company_names[symbols[i]] for i in range(3)}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.execute_python:12': {'file_path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}}

exec(code, env_args)
