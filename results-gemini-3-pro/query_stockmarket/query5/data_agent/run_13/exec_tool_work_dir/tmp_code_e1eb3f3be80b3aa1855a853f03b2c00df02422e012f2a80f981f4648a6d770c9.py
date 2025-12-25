code = """import json

# Load symbols from stockinfo
with open('var_function-call-7798081154467211843', 'r') as f:
    stockinfo_list = json.load(f)

# Load tables from stocktrade_database
with open('var_function-call-7798081154467211922', 'r') as f:
    tables_list = json.load(f)

# Extract symbols
target_symbols = set(item['Symbol'] for item in stockinfo_list)
available_tables = set(tables_list)

# Find intersection
valid_symbols = list(target_symbols.intersection(available_tables))
valid_symbols.sort()

print(f"Total target symbols: {len(target_symbols)}")
print(f"Total available tables: {len(available_tables)}")
print(f"Matching symbols: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-7798081154467211843': 'file_storage/function-call-7798081154467211843.json', 'var_function-call-7798081154467211922': 'file_storage/function-call-7798081154467211922.json'}

exec(code, env_args)
