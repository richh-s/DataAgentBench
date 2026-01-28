code = """import json

# Read the full result from the first query using locals()
result_key = 'var_functions.query_db:0'
result_file = locals()[result_key]

with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

# Extract symbols and company descriptions
symbols_info = {}
for stock in nasdaq_capital_stocks:
    symbols_info[stock['Symbol']] = stock['Company Description']

# Output the results
print('__RESULT__:')
print(json.dumps({
    'num_symbols': len(symbols_info),
    'sample_symbols': list(symbols_info.items())[:5]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
