code = """import json

# Load candidate symbols from stockinfo
with open(locals()['var_function-call-2090132530202969507'], 'r') as f:
    candidates_data = json.load(f)

# Extract symbols
candidate_symbols = set(item['Symbol'] for item in candidates_data)

# Load available tables in stocktrade
with open(locals()['var_function-call-2090132530202970712'], 'r') as f:
    available_tables = json.load(f)

# The tables are named after ticker symbols.
available_tables_set = set(available_tables)

# Intersection
valid_symbols = list(candidate_symbols.intersection(available_tables_set))
valid_symbols.sort()

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-2090132530202969507': 'file_storage/function-call-2090132530202969507.json', 'var_function-call-2090132530202970712': 'file_storage/function-call-2090132530202970712.json'}

exec(code, env_args)
