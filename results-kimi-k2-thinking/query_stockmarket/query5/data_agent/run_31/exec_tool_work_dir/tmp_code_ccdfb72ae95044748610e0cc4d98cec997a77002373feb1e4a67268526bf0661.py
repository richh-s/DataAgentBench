code = """import json

# Load the query results from the previous step
nasdaq_cap_stocks = []
result_file_path = var_functions.query_db:2

if isinstance(result_file_path, str):
    # If it's a file path, read the file
    with open(result_file_path, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    # If it's already loaded
    nasdaq_cap_stocks = result_file_path

# Extract symbols and company names
symbols_info = {}
for stock in nasdaq_cap_stocks:
    symbols_info[stock['Symbol']] = stock['Company Description']

print('__RESULT__:')
print(json.dumps(symbols_info))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
