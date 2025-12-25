code = """import json

# Load stockinfo results
with open(locals()['var_function-call-3331009659719671433'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-9922039288022969350'], 'r') as f:
    trade_tables = json.load(f)

# Create a set of trade tables for fast lookup
trade_tables_set = set(trade_tables)

# Filter stocks
valid_stocks = []
for item in stock_info:
    symbol = item['Symbol']
    if symbol in trade_tables_set:
        valid_stocks.append(item)

print(f"Total NYSE Non-ETF stocks found: {len(stock_info)}")
print(f"Stocks with data tables: {len(valid_stocks)}")

# If the number is not too huge, we can proceed.
# Let's print the first few valid stocks to verify.
print("__RESULT__:")
print(json.dumps(valid_stocks[:10]))"""

env_args = {'var_function-call-3331009659719671433': 'file_storage/function-call-3331009659719671433.json', 'var_function-call-9922039288022969350': 'file_storage/function-call-9922039288022969350.json'}

exec(code, env_args)
