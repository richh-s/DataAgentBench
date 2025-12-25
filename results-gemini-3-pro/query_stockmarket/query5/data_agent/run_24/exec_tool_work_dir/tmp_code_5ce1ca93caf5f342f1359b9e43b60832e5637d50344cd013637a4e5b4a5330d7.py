code = """import json

# Load stockinfo result
with open(locals()['var_function-call-15485977422406242611'], 'r') as f:
    stockinfo_data = json.load(f)

# Load stocktrade tables
with open(locals()['var_function-call-15853782635533120481'], 'r') as f:
    stocktrade_tables = json.load(f)

# Extract symbols
nasdaq_cm_symbols = set(item['Symbol'] for item in stockinfo_data)
available_tables = set(stocktrade_tables)

# Intersect
target_symbols = list(nasdaq_cm_symbols.intersection(available_tables))

print("__RESULT__:")
print(json.dumps({"count": len(target_symbols), "symbols": target_symbols}))"""

env_args = {'var_function-call-15485977422406242611': 'file_storage/function-call-15485977422406242611.json', 'var_function-call-15853782635533120481': 'file_storage/function-call-15853782635533120481.json'}

exec(code, env_args)
