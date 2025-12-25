code = """import json

# Load symbols from step 1
with open('var_function-call-14799188465443802831.json', 'r') as f:
    etf_data = json.load(f)
    etf_symbols = set(item['Symbol'] for item in etf_data)

# Load tables from step 2
with open('var_function-call-8672756111804777550.json', 'r') as f:
    trade_tables = json.load(f)
    trade_tables_set = set(trade_tables)

# Intersection
valid_symbols = sorted(list(etf_symbols.intersection(trade_tables_set)))

print(f"Total ETF symbols on NYSE Arca: {len(etf_symbols)}")
print(f"Total tables in trade db: {len(trade_tables_set)}")
print(f"Intersection count: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-14799188465443802831': 'file_storage/function-call-14799188465443802831.json', 'var_function-call-8672756111804777550': 'file_storage/function-call-8672756111804777550.json'}

exec(code, env_args)
