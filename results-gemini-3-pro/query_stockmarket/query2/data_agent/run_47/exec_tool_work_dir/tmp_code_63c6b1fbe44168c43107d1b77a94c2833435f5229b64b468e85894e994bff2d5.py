code = """import json

# Load ETF symbols
with open(locals()['var_function-call-2454856655276099395'], 'r') as f:
    etf_data = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_data)

# Load Table names
with open(locals()['var_function-call-6642693361376335155'], 'r') as f:
    tables = json.load(f)
table_names = set(tables)

# Intersection
valid_symbols = list(etf_symbols.intersection(table_names))
valid_symbols.sort()

print(f"Total ETFs: {len(etf_symbols)}")
print(f"Total Tables: {len(table_names)}")
print(f"Intersection Count: {len(valid_symbols)}")

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-7344486637286600100': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2454856655276099395': 'file_storage/function-call-2454856655276099395.json', 'var_function-call-6642693361376335155': 'file_storage/function-call-6642693361376335155.json'}

exec(code, env_args)
