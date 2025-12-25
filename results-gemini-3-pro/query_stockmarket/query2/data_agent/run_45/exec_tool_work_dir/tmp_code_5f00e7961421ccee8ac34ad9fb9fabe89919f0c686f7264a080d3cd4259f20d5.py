code = """import json

# Load ETF symbols
with open('var_function-call-3501888639631551339.json', 'r') as f:
    etf_list = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_list)

# Load tables
with open('var_function-call-1897156142471319365.json', 'r') as f:
    tables = json.load(f)

# Intersect
valid_etfs = sorted(list(etf_symbols.intersection(set(tables))))

print(f"Total ETFs listed on NYSE Arca: {len(etf_symbols)}")
print(f"Total Tables in trade db: {len(tables)}")
print(f"Intersection count: {len(valid_etfs)}")
print("__RESULT__:")
print(json.dumps(valid_etfs))"""

env_args = {'var_function-call-3501888639631551339': 'file_storage/function-call-3501888639631551339.json', 'var_function-call-1897156142471319365': 'file_storage/function-call-1897156142471319365.json'}

exec(code, env_args)
