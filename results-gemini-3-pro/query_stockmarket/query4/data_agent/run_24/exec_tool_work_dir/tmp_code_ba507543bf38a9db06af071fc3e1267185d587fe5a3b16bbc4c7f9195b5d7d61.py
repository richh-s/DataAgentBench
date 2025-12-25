code = """import json

# Load stockinfo result
with open(locals()['var_function-call-505177984360171283'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade tables list
with open(locals()['var_function-call-13180068455188980204'], 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
target_stocks = []
trade_tables_set = set(trade_tables)

for item in stock_info:
    symbol = item['Symbol']
    if symbol in trade_tables_set:
        target_stocks.append(item)

print(f"Count of matching stocks: {len(target_stocks)}")
print("__RESULT__:")
print(json.dumps(target_stocks))"""

env_args = {'var_function-call-6147490569046073636': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-505177984360171283': 'file_storage/function-call-505177984360171283.json', 'var_function-call-13180068455188980204': 'file_storage/function-call-13180068455188980204.json'}

exec(code, env_args)
