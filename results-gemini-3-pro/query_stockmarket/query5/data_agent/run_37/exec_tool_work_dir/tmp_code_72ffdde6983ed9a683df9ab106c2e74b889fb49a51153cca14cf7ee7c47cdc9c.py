code = """import json

# Load result from call-1 (Stock Info)
with open(locals()['var_function-call-15906074317050011412'], 'r') as f:
    stock_info = json.load(f)

# Load result from call-2 (Stock Trade Tables)
with open(locals()['var_function-call-13696343153078358647'], 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
info_symbols = {item['Symbol']: item['Company Description'] for item in stock_info}
trade_symbols = set(trade_tables)

# Intersect
valid_symbols = [s for s in info_symbols.keys() if s in trade_symbols]

print(f"Number of valid symbols: {len(valid_symbols)}")
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-15906074317050011412': 'file_storage/function-call-15906074317050011412.json', 'var_function-call-13696343153078358647': 'file_storage/function-call-13696343153078358647.json'}

exec(code, env_args)
