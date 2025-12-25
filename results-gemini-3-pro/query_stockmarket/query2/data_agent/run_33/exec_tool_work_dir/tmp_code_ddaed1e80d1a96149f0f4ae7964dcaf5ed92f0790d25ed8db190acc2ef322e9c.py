code = """import json

# Load ETF symbols
with open('var_function-call-689800581831186980.json', 'r') as f:
    etf_list = json.load(f)

etf_symbols = set(item['Symbol'] for item in etf_list)

# Load table names
with open('var_function-call-10272020244024100123.json', 'r') as f:
    tables_list = json.load(f)

tables_set = set(tables_list)

# Intersection
common_symbols = sorted(list(etf_symbols.intersection(tables_set)))

print("__RESULT__:")
print(json.dumps({"count": len(common_symbols), "symbols": common_symbols}))"""

env_args = {'var_function-call-689800581831186980': 'file_storage/function-call-689800581831186980.json', 'var_function-call-10272020244024100123': 'file_storage/function-call-10272020244024100123.json'}

exec(code, env_args)
