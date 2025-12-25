code = """import json

# Get file paths from variables
file_path_info = locals()['var_function-call-7798081154467211843']
file_path_tables = locals()['var_function-call-7798081154467211922']

# Load symbols from stockinfo
with open(file_path_info, 'r') as f:
    stockinfo_list = json.load(f)

# Load tables from stocktrade_database
with open(file_path_tables, 'r') as f:
    tables_list = json.load(f)

# Extract symbols
target_symbols = set(item['Symbol'] for item in stockinfo_list)
available_tables = set(tables_list)

# Find intersection
valid_symbols = list(target_symbols.intersection(available_tables))
valid_symbols.sort()

# Also create a mapping from Symbol to Company Description for the final answer
symbol_to_name = {item['Symbol']: item['Company Description'] for item in stockinfo_list if item['Symbol'] in valid_symbols}

print(f"Total target symbols: {len(target_symbols)}")
print(f"Total available tables: {len(available_tables)}")
print(f"Matching symbols: {len(valid_symbols)}")

# Limit the result size just in case, but we need the count to decide strategy.
print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols, "mapping": symbol_to_name}))"""

env_args = {'var_function-call-7798081154467211843': 'file_storage/function-call-7798081154467211843.json', 'var_function-call-7798081154467211922': 'file_storage/function-call-7798081154467211922.json'}

exec(code, env_args)
