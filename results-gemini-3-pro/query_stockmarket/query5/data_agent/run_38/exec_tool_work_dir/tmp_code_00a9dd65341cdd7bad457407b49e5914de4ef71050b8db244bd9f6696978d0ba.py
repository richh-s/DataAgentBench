code = """import json

# Load symbols from the first result
with open(locals()['var_function-call-403440647070611719'], 'r') as f:
    stock_info = json.load(f)

# Load table names from the second result
with open(locals()['var_function-call-403440647070612544'], 'r') as f:
    tables = json.load(f)

# Extract symbols
target_symbols = set(item['Symbol'] for item in stock_info)
available_tables = set(tables)

# Find intersection
matching_symbols = list(target_symbols.intersection(available_tables))

# Prepare map for later use (Symbol -> Company Name)
symbol_to_name = {item['Symbol']: item['Company Description'] for item in stock_info if item['Symbol'] in matching_symbols}

print(f"Total matching symbols: {len(matching_symbols)}")
print("__RESULT__:")
print(json.dumps({"matching_symbols": matching_symbols, "symbol_to_name": symbol_to_name}))"""

env_args = {'var_function-call-403440647070611719': 'file_storage/function-call-403440647070611719.json', 'var_function-call-403440647070612544': 'file_storage/function-call-403440647070612544.json'}

exec(code, env_args)
