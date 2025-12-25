code = """import json

# Load ETF symbols
with open(locals()['var_function-call-4017956319566786658'], 'r') as f:
    etf_list = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_list)

# Load table names
with open(locals()['var_function-call-17745112889233166129'], 'r') as f:
    table_list = json.load(f)
table_names = set(table_list)

# Intersection
valid_symbols = list(etf_symbols.intersection(table_names))

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-5292189082820966608': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-4017956319566786658': 'file_storage/function-call-4017956319566786658.json', 'var_function-call-17745112889233166129': 'file_storage/function-call-17745112889233166129.json'}

exec(code, env_args)
