code = """import json

# Load ETFs
with open(var_function_call_1439893960657579719, 'r') as f:
    etfs_data = json.load(f)
etf_symbols = set(item['Symbol'] for item in etfs_data)

# Load tables
with open(var_function_call_8649986010323061245, 'r') as f:
    tables_list = json.load(f)
tables_set = set(tables_list)

# Intersection
candidates = list(etf_symbols.intersection(tables_set))
candidates.sort()

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-1439893960657579719': 'file_storage/function-call-1439893960657579719.json', 'var_function-call-8649986010323061245': 'file_storage/function-call-8649986010323061245.json'}

exec(code, env_args)
