code = """import json

# Load stockinfo results
with open(locals()['var_function-call-17490755573003883636'], 'r') as f:
    stock_info_list = json.load(f)

# Load stocktrade tables
with open(locals()['var_function-call-8209134030405193310'], 'r') as f:
    table_list = json.load(f)

# Filter
valid_stocks = []
tables_set = set(table_list)

for stock in stock_info_list:
    symbol = stock['Symbol']
    if symbol in tables_set:
        valid_stocks.append(stock)

print(f"Total potential stocks: {len(stock_info_list)}")
print(f"Stocks with data tables: {len(valid_stocks)}")
print("__RESULT__:")
print(json.dumps(valid_stocks))"""

env_args = {'var_function-call-17490755573003883636': 'file_storage/function-call-17490755573003883636.json', 'var_function-call-8209134030405193310': 'file_storage/function-call-8209134030405193310.json'}

exec(code, env_args)
