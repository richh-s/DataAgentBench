code = """import json

# Load ETF symbols
# Key: var_function-call-6298308308672748942
with open(locals()['var_function-call-6298308308672748942'], 'r') as f:
    etf_data = json.load(f)
etf_symbols = set(item['Symbol'] for item in etf_data)

# Load table names
# Key: var_function-call-7304166957241906547
with open(locals()['var_function-call-7304166957241906547'], 'r') as f:
    table_names = json.load(f)
table_names = set(table_names)

# Intersection
common_symbols = list(etf_symbols.intersection(table_names))

print('__RESULT__:')
print(json.dumps(common_symbols))"""

env_args = {'var_function-call-11011174398477336959': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-6298308308672748942': 'file_storage/function-call-6298308308672748942.json', 'var_function-call-7304166957241906547': 'file_storage/function-call-7304166957241906547.json'}

exec(code, env_args)
