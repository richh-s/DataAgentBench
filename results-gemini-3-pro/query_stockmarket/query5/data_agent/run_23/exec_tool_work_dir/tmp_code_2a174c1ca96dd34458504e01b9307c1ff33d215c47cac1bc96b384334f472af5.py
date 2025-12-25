code = """import json

# Get file paths from local variables
path_candidates = locals()['var_function-call-10214436996742013991']
path_tables = locals()['var_function-call-16037217244110734326']

# Load stockinfo result
with open(path_candidates, 'r') as f:
    candidates = json.load(f)

# Load stocktrade tables
with open(path_tables, 'r') as f:
    tables = json.load(f)

# Extract symbols
candidate_symbols = {c['Symbol'] for c in candidates}
table_set = set(tables)

# Intersection
valid_symbols = list(candidate_symbols.intersection(table_set))
valid_symbols.sort()

# Also keep a map of Symbol -> Company Name
sym_to_name = {c['Symbol']: c['Company Description'] for c in candidates if c['Symbol'] in valid_symbols}

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols, "mapping": sym_to_name}))"""

env_args = {'var_function-call-10214436996742013991': 'file_storage/function-call-10214436996742013991.json', 'var_function-call-16037217244110734326': 'file_storage/function-call-16037217244110734326.json'}

exec(code, env_args)
