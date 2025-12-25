code = """import json

# Load ETF symbols
with open(locals()['var_function-call-10780135608603359427'], 'r') as f:
    etf_data = json.load(f)
    etf_symbols = set(item['Symbol'] for item in etf_data)

# Load table names
with open(locals()['var_function-call-12146310968865699605'], 'r') as f:
    table_names = set(json.load(f))

# Intersection
valid_symbols = sorted(list(etf_symbols.intersection(table_names)))

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-4976631640626439833': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-10780135608603359427': 'file_storage/function-call-10780135608603359427.json', 'var_function-call-12146310968865699605': 'file_storage/function-call-12146310968865699605.json'}

exec(code, env_args)
