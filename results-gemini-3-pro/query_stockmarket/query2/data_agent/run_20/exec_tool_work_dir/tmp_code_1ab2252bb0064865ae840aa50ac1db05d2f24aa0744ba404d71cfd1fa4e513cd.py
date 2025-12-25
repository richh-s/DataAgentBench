code = """import json

# Load stockinfo results
with open(locals()['var_function-call-8581251308861529440']) as f:
    stock_info_list = json.load(f)

target_symbols = set(item['Symbol'] for item in stock_info_list)

# Load stocktrade tables
with open(locals()['var_function-call-1676637049727952223']) as f:
    trade_tables = set(json.load(f))

# Intersection
valid_symbols = sorted(list(target_symbols.intersection(trade_tables)))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols}))"""

env_args = {'var_function-call-8581251308861529440': 'file_storage/function-call-8581251308861529440.json', 'var_function-call-1676637049727952223': 'file_storage/function-call-1676637049727952223.json'}

exec(code, env_args)
