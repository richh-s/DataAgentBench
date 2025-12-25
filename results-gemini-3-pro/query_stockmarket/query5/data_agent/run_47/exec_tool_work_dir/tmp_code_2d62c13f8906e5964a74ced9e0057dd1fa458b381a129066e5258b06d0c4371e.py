code = """import json

# Load stockinfo result
with open(locals()['var_function-call-14158479634354559369'], 'r') as f:
    stock_info = json.load(f)

# Load table list
with open(locals()['var_function-call-8638126572495910571'], 'r') as f:
    table_list = json.load(f)

# Convert table_list to set for fast lookup
table_set = set(table_list)

# Filter stock_info for symbols that have a table
valid_stocks = []
for stock in stock_info:
    sym = stock['Symbol']
    if sym in table_set:
        valid_stocks.append(stock)

print(f"Total 'S' market category stocks: {len(stock_info)}")
print(f"Stocks with tables in DuckDB: {len(valid_stocks)}")

# If number is reasonable, we can proceed with UNION ALL query generation.
# Print first 5 to verify.
print("__RESULT__:")
print(json.dumps(valid_stocks[:5]))"""

env_args = {'var_function-call-14158479634354559369': 'file_storage/function-call-14158479634354559369.json', 'var_function-call-8638126572495910571': 'file_storage/function-call-8638126572495910571.json'}

exec(code, env_args)
