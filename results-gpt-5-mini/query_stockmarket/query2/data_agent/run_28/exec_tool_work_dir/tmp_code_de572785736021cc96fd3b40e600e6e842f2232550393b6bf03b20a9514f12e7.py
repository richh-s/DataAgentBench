code = """import json
# var_call_h0FX10ktnmTjEkjxLPSsQRKX and var_call_3kri8bsiamHSoLhqT1OuIaBk are available from previous tool calls
# Load the results
with open(var_call_h0FX10ktnmTjEkjxLPSsQRKX, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_3kri8bsiamHSoLhqT1OuIaBk, 'r') as f:
    trade_tables = json.load(f)

# Extract symbols from stockinfo
symbols_stockinfo = [rec['Symbol'] for rec in stockinfo]
# trade_tables is list of table names (strings)

# Compute intersection (symbols present in both)
intersection = sorted(list(set(symbols_stockinfo).intersection(set(trade_tables))))

# Print result as JSON string
print("__RESULT__:")
print(json.dumps(intersection))"""

env_args = {'var_call_h0FX10ktnmTjEkjxLPSsQRKX': 'file_storage/call_h0FX10ktnmTjEkjxLPSsQRKX.json', 'var_call_3kri8bsiamHSoLhqT1OuIaBk': 'file_storage/call_3kri8bsiamHSoLhqT1OuIaBk.json'}

exec(code, env_args)
