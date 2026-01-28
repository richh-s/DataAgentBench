code = """import json

# Read the query result from the file path stored in the variable
file_path = var_functions.query_db:0

with open(file_path, 'r') as f:
    nyse_stockinfo = json.load(f)

# Extract symbols and company descriptions
symbols = [stock['Symbol'] for stock in nyse_stockinfo]
company_descriptions = {stock['Symbol']: stock['Company Description'] for stock in nyse_stockinfo}

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(symbols),
    'first_10_symbols': symbols[:10],
    'sample_descriptions': {symbols[i]: company_descriptions[symbols[i]] for i in range(3)}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo']}

exec(code, env_args)
