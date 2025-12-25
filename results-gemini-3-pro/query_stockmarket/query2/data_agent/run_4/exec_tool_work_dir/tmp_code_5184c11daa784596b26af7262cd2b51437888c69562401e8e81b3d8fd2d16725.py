code = """import json

# Load ETF list
with open('var_function-call-5039856018528113346.json', 'r') as f:
    etf_list = json.load(f)

# Load Table list
with open('var_function-call-11443630550213120568.json', 'r') as f:
    table_list = json.load(f)

# Extract symbols
etf_symbols = set(item['Symbol'] for item in etf_list)
available_tables = set(table_list)

# Intersect
valid_symbols = sorted(list(etf_symbols.intersection(available_tables)))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols}))"""

env_args = {'var_function-call-5039856018528113346': 'file_storage/function-call-5039856018528113346.json', 'var_function-call-11443630550213120568': 'file_storage/function-call-11443630550213120568.json'}

exec(code, env_args)
