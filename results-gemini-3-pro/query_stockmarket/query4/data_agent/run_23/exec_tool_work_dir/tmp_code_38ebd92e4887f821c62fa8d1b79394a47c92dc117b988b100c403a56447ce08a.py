code = """import json

# Load stockinfo result
with open(locals()['var_function-call-12422574718348653119'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade tables result
with open(locals()['var_function-call-7361097673943553959'], 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
info_symbols = set([item['Symbol'] for item in stock_info])
trade_symbols = set(trade_tables)

# Intersection
relevant_symbols = list(info_symbols.intersection(trade_symbols))

print(f"DEBUG: Found {len(relevant_symbols)} relevant symbols.")
print(f"DEBUG: First 10: {relevant_symbols[:10]}")

print("__RESULT__:")
print(json.dumps(relevant_symbols))"""

env_args = {'var_function-call-13162311836547151521': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-12422574718348653119': 'file_storage/function-call-12422574718348653119.json', 'var_function-call-7361097673943553959': 'file_storage/function-call-7361097673943553959.json'}

exec(code, env_args)
