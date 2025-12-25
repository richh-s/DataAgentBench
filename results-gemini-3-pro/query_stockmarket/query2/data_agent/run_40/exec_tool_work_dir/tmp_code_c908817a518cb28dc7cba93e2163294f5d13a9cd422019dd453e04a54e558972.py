code = """import json

# Load ETFs
with open(locals()['var_function-call-8651100051121965824'], 'r') as f:
    etf_data = json.load(f)
etf_symbols = [item['Symbol'] for item in etf_data]

# Load Tables
with open(locals()['var_function-call-10552792860447953947'], 'r') as f:
    tables = json.load(f)

# Find intersection
valid_etfs = list(set(etf_symbols).intersection(set(tables)))

print("__RESULT__:")
print(json.dumps({"count": len(valid_etfs), "first_50": valid_etfs[:50]}))"""

env_args = {'var_function-call-8651100051121965824': 'file_storage/function-call-8651100051121965824.json', 'var_function-call-10552792860447953947': 'file_storage/function-call-10552792860447953947.json'}

exec(code, env_args)
