code = """import json

# Get file paths from variables
etf_file_path = locals()['var_function-call-2414525597051241979']
tables_file_path = locals()['var_function-call-18281756366382191037']

# Load ETF symbols
with open(etf_file_path, 'r') as f:
    etf_symbols = [item['Symbol'] for item in json.load(f)]

# Load DB tables
with open(tables_file_path, 'r') as f:
    db_tables = set(json.load(f))

# Intersection
valid_symbols = [s for s in etf_symbols if s in db_tables]

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "first_100": valid_symbols[:100]}))"""

env_args = {'var_function-call-9862830328002497441': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2414525597051241979': 'file_storage/function-call-2414525597051241979.json', 'var_function-call-18281756366382191037': 'file_storage/function-call-18281756366382191037.json'}

exec(code, env_args)
