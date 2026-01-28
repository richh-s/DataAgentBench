code = """import json

# Load NASDAQ Capital Market stocks from the query result
nasdaq_cap_file = var_functions.query_db:32
with open(nasdaq_cap_file, 'r') as f:
    nasdaq_cap_stocks = json.load(f)

# Extract symbols and company descriptions
nasdaq_symbols = [stock['Symbol'] for stock in nasdaq_cap_stocks]
company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_cap_stocks}

print('Total NASDAQ Capital Market stocks loaded:', len(nasdaq_symbols))
print('First 10 symbols:', nasdaq_symbols[:10])
print('__RESULT__:')
print(json.dumps(nasdaq_symbols[:50]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.list_db:7': ['stockinfo'], 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.list_db:24': 'file_storage/functions.list_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
