code = """import json

# Load the lists
with open(locals()['var_function-call-8397547898646766086'], 'r') as f:
    stock_info = json.load(f)
    
with open(locals()['var_function-call-15189621055493639909'], 'r') as f:
    trade_tables = json.load(f)

# Create a set of trade tables for fast lookup
trade_tables_set = set(trade_tables)

# Filter stock_info
valid_stocks = []
for stock in stock_info:
    sym = stock['Symbol']
    if sym in trade_tables_set:
        valid_stocks.append(stock)

print(f"Total valid stocks: {len(valid_stocks)}")
print("__RESULT__:")
print(json.dumps(valid_stocks))"""

env_args = {'var_function-call-8397547898646766086': 'file_storage/function-call-8397547898646766086.json', 'var_function-call-15189621055493639909': 'file_storage/function-call-15189621055493639909.json'}

exec(code, env_args)
