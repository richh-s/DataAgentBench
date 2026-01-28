code = """import json
# load previous tool results from storage
with open(var_call_HU07LgpwYKt6DI2bxvoKFoaW, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_bp0oaTukSilXP0rpxGJ4KeOY, 'r') as f:
    tables = json.load(f)

# extract symbols from stockinfo
symbols = [r['Symbol'] for r in stockinfo]
# intersect with available tables
available = set(tables)
symbols_to_query = [s for s in symbols if s in available]

# output
print("__RESULT__:")
print(json.dumps(symbols_to_query))"""

env_args = {'var_call_HU07LgpwYKt6DI2bxvoKFoaW': 'file_storage/call_HU07LgpwYKt6DI2bxvoKFoaW.json', 'var_call_bp0oaTukSilXP0rpxGJ4KeOY': 'file_storage/call_bp0oaTukSilXP0rpxGJ4KeOY.json'}

exec(code, env_args)
