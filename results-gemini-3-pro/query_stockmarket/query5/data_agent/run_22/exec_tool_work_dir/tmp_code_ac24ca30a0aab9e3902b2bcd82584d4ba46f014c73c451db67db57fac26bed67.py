code = """import json

# Load the results from the files
with open(locals()['var_function-call-1929074110490398114'], 'r') as f:
    stock_info = json.load(f)

with open(locals()['var_function-call-1929074110490396355'], 'r') as f:
    table_list = json.load(f)

# Extract symbols
nasdaq_capital_symbols = {item['Symbol']: item['Company Description'] for item in stock_info}
available_tables = set(table_list)

# Intersect
valid_symbols = [s for s in nasdaq_capital_symbols.keys() if s in available_tables]

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols}))"""

env_args = {'var_function-call-1929074110490398114': 'file_storage/function-call-1929074110490398114.json', 'var_function-call-1929074110490396355': 'file_storage/function-call-1929074110490396355.json'}

exec(code, env_args)
