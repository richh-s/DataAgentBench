code = """import json

# Load stockinfo results
with open(locals()['var_function-call-12883889055046152323'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade tables
with open(locals()['var_function-call-4688559592186676218'], 'r') as f:
    trade_tables = set(json.load(f))

# Filter symbols
target_symbols = []
symbol_map = {}

for entry in stock_info:
    sym = entry['Symbol']
    if sym in trade_tables:
        target_symbols.append(sym)
        symbol_map[sym] = entry['Company Description']

print("__RESULT__:")
print(json.dumps({"count": len(target_symbols), "symbols": target_symbols}))"""

env_args = {'var_function-call-12883889055046152323': 'file_storage/function-call-12883889055046152323.json', 'var_function-call-4688559592186676218': 'file_storage/function-call-4688559592186676218.json'}

exec(code, env_args)
