code = """import json

# Load ETFs
with open('var_function-call-3498236825446053099.json', 'r') as f:
    etfs_data = json.load(f)
etf_symbols = set(item['Symbol'] for item in etfs_data)

# Load Tables
with open('var_function-call-17765899317089105745.json', 'r') as f:
    tables = json.load(f)
table_names = set(tables)

# Intersection
relevant_etfs = sorted(list(etf_symbols.intersection(table_names)))

print("__RESULT__:")
print(json.dumps({"count": len(relevant_etfs), "etfs": relevant_etfs}))"""

env_args = {'var_function-call-3498236825446053099': 'file_storage/function-call-3498236825446053099.json', 'var_function-call-17765899317089105745': 'file_storage/function-call-17765899317089105745.json'}

exec(code, env_args)
