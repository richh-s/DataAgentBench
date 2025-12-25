code = """import json

# Load ETF list
with open('var_function-call-7475560093060171147.json', 'r') as f:
    etf_data = json.load(f)

etf_symbols = set(item['Symbol'] for item in etf_data)

# Load table list
with open('var_function-call-11135752326348972247.json', 'r') as f:
    tables = json.load(f)

table_set = set(tables)

# Intersect
valid_etfs = sorted(list(etf_symbols.intersection(table_set)))

print("__RESULT__:")
print(json.dumps(valid_etfs))"""

env_args = {'var_function-call-7475560093060171147': 'file_storage/function-call-7475560093060171147.json', 'var_function-call-11135752326348972247': 'file_storage/function-call-11135752326348972247.json'}

exec(code, env_args)
