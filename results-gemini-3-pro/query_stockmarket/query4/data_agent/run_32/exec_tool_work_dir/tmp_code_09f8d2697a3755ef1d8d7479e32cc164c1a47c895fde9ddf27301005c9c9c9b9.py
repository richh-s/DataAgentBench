code = """import json

# Load symbols from stockinfo result
with open(locals()['var_function-call-8321990054734025246'], 'r') as f:
    stockinfo_list = json.load(f)

# Load tables from stocktrade result
with open(locals()['var_function-call-10055054036662575247'], 'r') as f:
    table_list = json.load(f)

# Create a set of table names for fast lookup
table_set = set(table_list)

# Filter stocks that are in table_set
# We also keep the Company Description for the final answer
valid_stocks = []
for item in stockinfo_list:
    sym = item['Symbol']
    if sym in table_set:
        valid_stocks.append(item)

print(f"Total NYSE non-ETF stocks: {len(stockinfo_list)}")
print(f"Stocks with trade data: {len(valid_stocks)}")

# Let's verify the first few valid stocks
print("First 10 valid stocks:", valid_stocks[:10])

print("__RESULT__:")
print(json.dumps(valid_stocks))"""

env_args = {'var_function-call-13183360315961424541': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8321990054734025246': 'file_storage/function-call-8321990054734025246.json', 'var_function-call-10055054036662575247': 'file_storage/function-call-10055054036662575247.json'}

exec(code, env_args)
