code = """import json

# Load stockinfo candidates
with open(locals()['var_function-call-16619216267788933502'], 'r') as f:
    candidates = json.load(f)

# Load stocktrade table names
with open(locals()['var_function-call-7766385081012407064'], 'r') as f:
    tables = json.load(f)

# Create a set of table names for fast lookup
table_set = set(tables)

# Filter candidates
valid_symbols = []
for c in candidates:
    sym = c['Symbol']
    # Check if symbol exists in tables (case sensitive? usually yes, but let's assume exact match)
    if sym in table_set:
        valid_symbols.append(c)

print("__RESULT__:")
print(len(valid_symbols))"""

env_args = {'var_function-call-16619216267788933502': 'file_storage/function-call-16619216267788933502.json', 'var_function-call-7766385081012407064': 'file_storage/function-call-7766385081012407064.json'}

exec(code, env_args)
