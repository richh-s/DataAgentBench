code = """import json

# Load stockinfo results
with open(locals()['var_function-call-163400815979210692'], 'r') as f:
    stock_info_list = json.load(f)

# Load stocktrade tables list
with open(locals()['var_function-call-13733617375482942009'], 'r') as f:
    trade_tables_list = json.load(f)

# Create a set of available tables for faster lookup
available_tables = set(trade_tables_list)

# Filter stock info for those that have a corresponding table
valid_symbols = []
for entry in stock_info_list:
    sym = entry['Symbol']
    if sym in available_tables:
        valid_symbols.append(sym)

print(f"Total valid symbols: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-163400815979210692': 'file_storage/function-call-163400815979210692.json', 'var_function-call-13733617375482942009': 'file_storage/function-call-13733617375482942009.json'}

exec(code, env_args)
