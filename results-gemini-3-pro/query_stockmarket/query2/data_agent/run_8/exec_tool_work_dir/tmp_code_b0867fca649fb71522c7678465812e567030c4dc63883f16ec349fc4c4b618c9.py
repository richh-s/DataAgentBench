code = """import json

# Load ETFs list
with open(locals()['var_function-call-14532322368764427460'], 'r') as f:
    etfs_info = json.load(f)

# Load tables list
with open(locals()['var_function-call-8803107773511705717'], 'r') as f:
    tables_list = json.load(f)

# Extract symbols
etf_symbols = {item['Symbol'] for item in etfs_info}
table_set = set(tables_list)

# Intersection
valid_etfs = sorted(list(etf_symbols.intersection(table_set)))

print(f"Total ETFs on NYSE Arca: {len(etf_symbols)}")
print(f"Total Tables in DB: {len(table_set)}")
print(f"Intersection (Valid ETFs to check): {len(valid_etfs)}")

# Generate SQL query
# To avoid a query that is too large, let's see how many we have.
# If we have many, we might need to split.
print("__RESULT__:")
print(json.dumps(valid_etfs))"""

env_args = {'var_function-call-14532322368764427460': 'file_storage/function-call-14532322368764427460.json', 'var_function-call-8803107773511705717': 'file_storage/function-call-8803107773511705717.json'}

exec(code, env_args)
