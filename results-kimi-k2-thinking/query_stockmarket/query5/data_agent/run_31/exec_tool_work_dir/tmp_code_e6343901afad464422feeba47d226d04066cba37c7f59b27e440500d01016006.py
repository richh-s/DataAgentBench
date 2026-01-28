code = """import json

# Get the results from storage
nasdaq_cap_data = locals()['var_functions.query_db:2']

# Load the data if it's a file path
if isinstance(nasdaq_cap_data, str) and nasdaq_cap_data.endswith('.json'):
    with open(nasdaq_cap_data, 'r') as f:
        nasdaq_cap_symbols = json.load(f)
else:
    nasdaq_cap_symbols = nasdaq_cap_data

# Extract symbols
symbols_list = [item['Symbol'] for item in nasdaq_cap_symbols]

print('__RESULT__:')
print(json.dumps(symbols_list))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
