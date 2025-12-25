code = """import json

stockinfo_file = locals()['var_function-call-15963372887811120509']
stocktrade_tables_file = locals()['var_function-call-11545474830056359161']

with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

with open(stocktrade_tables_file, 'r') as f:
    stocktrade_tables = set(json.load(f))

candidates = []
for item in stockinfo_data:
    sym = item['Symbol']
    if sym in stocktrade_tables:
        candidates.append(item)

# Output result
print("__RESULT__:")
print(json.dumps({'count': len(candidates), 'candidates': candidates}))"""

env_args = {'var_function-call-15963372887811120509': 'file_storage/function-call-15963372887811120509.json', 'var_function-call-11545474830056359161': 'file_storage/function-call-11545474830056359161.json'}

exec(code, env_args)
