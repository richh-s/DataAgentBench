code = """import json

# Load ETF symbols
with open(locals()['var_function-call-9156895254517831471'], 'r') as f:
    etf_data = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_data)

# Load Table names
with open(locals()['var_function-call-7507699247137649927'], 'r') as f:
    table_names = set(json.load(f))

# Intersection
valid_symbols = list(etf_symbols.intersection(table_names))
valid_symbols.sort()

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-352515498678611110': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-9156895254517831471': 'file_storage/function-call-9156895254517831471.json', 'var_function-call-7507699247137649927': 'file_storage/function-call-7507699247137649927.json'}

exec(code, env_args)
