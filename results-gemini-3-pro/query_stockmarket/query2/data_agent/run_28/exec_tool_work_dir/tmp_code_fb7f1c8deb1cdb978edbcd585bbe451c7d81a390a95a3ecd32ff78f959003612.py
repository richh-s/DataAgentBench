code = """import json

with open('var_function-call-11805765579617057108.json', 'r') as f:
    stockinfo_data = json.load(f)

etf_symbols = set(item['Symbol'] for item in stockinfo_data)

with open('var_function-call-18208316545680584426.json', 'r') as f:
    table_names = json.load(f)

available_tables = set(table_names)
valid_symbols = list(etf_symbols.intersection(available_tables))
valid_symbols.sort()

# Just print the count and first few to check
print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "first_10": valid_symbols[:10]}))"""

env_args = {'var_function-call-11805765579617057108': 'file_storage/function-call-11805765579617057108.json', 'var_function-call-18208316545680584426': 'file_storage/function-call-18208316545680584426.json'}

exec(code, env_args)
