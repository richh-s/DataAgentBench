code = """import json

# Load the query result from the first database
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

# Process the data to extract symbols and descriptions
nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
nyse_descriptions = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

result = {
    'count': len(nyse_stocks),
    'symbols': nyse_symbols[:10],  # First 10 symbols
    'descriptions_sample': {k: v for k, v in list(nyse_descriptions.items())[:3]}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
