code = """import json

# Load the NASDAQ Capital Market symbols from previous query
result_file = var_functions.query_db:2

# Since the previous query might be a file path, handle both cases
nasdaq_cap_symbols = []

if isinstance(result_file, str):
    # It's a file path
    try:
        with open(result_file, 'r') as f:
            nasdaq_cap_symbols = json.load(f)
    except Exception as e:
        print(f"Error loading file: {e}")
else:
    # It's already a list
    nasdaq_cap_symbols = result_file

# Extract symbols and company names
symbols_list = []
for item in nasdaq_cap_symbols:
    if isinstance(item, dict):
        symbols_list.append(item['Symbol'])

print('__RESULT__:')
print(json.dumps(symbols_list[:100]))  # Print first 100 to verify"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
