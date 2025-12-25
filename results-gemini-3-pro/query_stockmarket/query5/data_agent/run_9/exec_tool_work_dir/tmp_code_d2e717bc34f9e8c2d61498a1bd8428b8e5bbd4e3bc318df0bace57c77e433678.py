code = """import json

# Get file paths from variables
file_path_info = locals()['var_function-call-5715290877284323167']
file_path_tables = locals()['var_function-call-18378532918632794193']

# Load the results from the files
with open(file_path_info, 'r') as f:
    stock_info = json.load(f)

with open(file_path_tables, 'r') as f:
    table_list = json.load(f)

# Extract symbols
nasdaq_capital_symbols = set(item['Symbol'] for item in stock_info)
available_tables = set(table_list)

# Intersection
target_symbols = list(nasdaq_capital_symbols.intersection(available_tables))
target_symbols.sort()

# Create map
symbol_to_name = {item['Symbol']: item['Company Description'] for item in stock_info if item['Symbol'] in target_symbols}

print("__RESULT__:")
print(json.dumps({
    "target_symbols": target_symbols,
    "symbol_to_name": symbol_to_name
}))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json'}

exec(code, env_args)
