code = """import json
import pandas as pd

# Load stockinfo results
with open(locals()['var_function-call-14483470659460654413'], 'r') as f:
    stock_info = json.load(f)

# Load table names
with open(locals()['var_function-call-14483470659460654526'], 'r') as f:
    tables = json.load(f)

# Extract symbols from stock_info
# stock_info is a list of dicts: [{"Symbol": "...", "Company Description": "..."}]
target_symbols = [item['Symbol'] for item in stock_info]

# Find intersection
valid_symbols = set(target_symbols).intersection(set(tables))

print(f"Total target symbols: {len(target_symbols)}")
print(f"Total available tables: {len(tables)}")
print(f"Intersection count: {len(valid_symbols)}")

# Store valid symbols map for later use
valid_symbols_list = list(valid_symbols)
valid_symbols_map = {item['Symbol']: item['Company Description'] for item in stock_info if item['Symbol'] in valid_symbols}

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "first_10": valid_symbols_list[:10]}))"""

env_args = {'var_function-call-14483470659460654413': 'file_storage/function-call-14483470659460654413.json', 'var_function-call-14483470659460654526': 'file_storage/function-call-14483470659460654526.json'}

exec(code, env_args)
