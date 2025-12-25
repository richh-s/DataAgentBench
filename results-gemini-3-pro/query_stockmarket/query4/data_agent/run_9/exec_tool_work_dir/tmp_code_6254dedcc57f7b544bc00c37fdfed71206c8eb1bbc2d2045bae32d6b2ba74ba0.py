code = """import json

# Access the file paths from the variables
path_candidates = locals()['var_function-call-4623597435965185168']
path_tables = locals()['var_function-call-4623597435965183535']

# Load candidate stocks
with open(path_candidates, 'r') as f:
    candidates = json.load(f)

# Load table names
with open(path_tables, 'r') as f:
    tables = json.load(f)

# Extract symbols
candidate_symbols = {c['Symbol'] for c in candidates}
table_set = set(tables)

# Intersect
valid_symbols = list(candidate_symbols.intersection(table_set))

print(f"Number of candidates: {len(candidate_symbols)}")
print(f"Number of tables: {len(table_set)}")
print(f"Number of valid symbols: {len(valid_symbols)}")

# Save the valid symbols and mapping to company name for later
# We need the company names for the final answer
symbol_map = {c['Symbol']: c['Company Description'] for c in candidates if c['Symbol'] in table_set}

result = {
    "valid_symbols": valid_symbols,
    "symbol_map": symbol_map
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4623597435965185168': 'file_storage/function-call-4623597435965185168.json', 'var_function-call-4623597435965183535': 'file_storage/function-call-4623597435965183535.json'}

exec(code, env_args)
