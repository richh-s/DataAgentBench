code = """import json

# Read the potential symbols from stockinfo
with open('var_function-call-305604398678755186.json', 'r') as f:
    stock_info = json.load(f)

# Read the table names from stocktrade
with open('var_function-call-2255113569688009603.json', 'r') as f:
    table_names = json.load(f)

# Create a set of table names for fast lookup
table_set = set(table_names)

# Filter stock_info for symbols that have a table
valid_stocks = []
for entry in stock_info:
    sym = entry['Symbol']
    if sym in table_set:
        valid_stocks.append(entry)

print(f"Total potential stocks: {len(stock_info)}")
print(f"Stocks with data: {len(valid_stocks)}")
print(f"Example valid stocks: {valid_stocks[:5]}")

print('__RESULT__:')
print(json.dumps(valid_stocks))"""

env_args = {'var_function-call-305604398678755186': 'file_storage/function-call-305604398678755186.json', 'var_function-call-2255113569688009603': 'file_storage/function-call-2255113569688009603.json'}

exec(code, env_args)
