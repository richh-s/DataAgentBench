code = """import json

# Load candidate stocks
with open('var_function-call-4623597435965185168.json', 'r') as f:
    candidates = json.load(f)

# Load table names
with open('var_function-call-4623597435965183535.json', 'r') as f:
    tables = json.load(f)

# Extract symbols
candidate_symbols = {c['Symbol'] for c in candidates}
table_set = set(tables)

# Intersect
valid_symbols = candidate_symbols.intersection(table_set)

print(f"Number of candidates: {len(candidate_symbols)}")
print(f"Number of tables: {len(table_set)}")
print(f"Number of valid symbols: {len(valid_symbols)}")

# List the first few valid symbols to verify
print(f"Sample valid symbols: {list(valid_symbols)[:10]}")

print("__RESULT__:")
print(json.dumps(list(valid_symbols)))"""

env_args = {'var_function-call-4623597435965185168': 'file_storage/function-call-4623597435965185168.json', 'var_function-call-4623597435965183535': 'file_storage/function-call-4623597435965183535.json'}

exec(code, env_args)
