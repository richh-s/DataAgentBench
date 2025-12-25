code = """import json

# Load stockinfo result
with open(locals()['var_function-call-14828481588465670158'], 'r') as f:
    stock_info = json.load(f)

# Load list_db result
with open(locals()['var_function-call-6181491610374641516'], 'r') as f:
    tables = json.load(f)

# Extract symbols
# stock_info is a list of dicts: [{"Symbol": "AGMH", "Company Description": ...}, ...]
# tables is a list of strings: ["AAAU", ...]

nasdaq_cm_symbols = {item['Symbol'] for item in stock_info}
available_tables = set(tables)

# Intersection
valid_symbols = list(nasdaq_cm_symbols.intersection(available_tables))
valid_symbols.sort()

# Create a mapping from symbol to company name for later
symbol_to_name = {item['Symbol']: item['Company Description'] for item in stock_info if item['Symbol'] in valid_symbols}

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols, "mapping": symbol_to_name}))"""

env_args = {'var_function-call-14828481588465670158': 'file_storage/function-call-14828481588465670158.json', 'var_function-call-6181491610374641516': 'file_storage/function-call-6181491610374641516.json'}

exec(code, env_args)
