code = """import json

# Load symbols from stockinfo
with open(locals()['var_function-call-12823899382906122625'], 'r') as f:
    stock_info = json.load(f)

# Load tables from stocktrade
with open(locals()['var_function-call-15795794129974371923'], 'r') as f:
    tables = json.load(f)

# Create a set of tables
tables_set = set(tables)

# Filter stock_info for symbols that have a table
valid_stocks = []
for entry in stock_info:
    sym = entry['Symbol']
    if sym in tables_set:
        valid_stocks.append(entry)

print(f"Total symbols found: {len(valid_stocks)}")
print(f"First 10 symbols: {[s['Symbol'] for s in valid_stocks[:10]]}")
print("__RESULT__:")
print(json.dumps(valid_stocks))"""

env_args = {'var_function-call-12823899382906122625': 'file_storage/function-call-12823899382906122625.json', 'var_function-call-15795794129974371923': 'file_storage/function-call-15795794129974371923.json'}

exec(code, env_args)
