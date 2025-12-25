code = """import json

# Load stockinfo result
with open('var_function-call-8671132249438032894.json', 'r') as f:
    stock_info = json.load(f)

# Load stocktrade table list
with open('var_function-call-8671132249438035785.json', 'r') as f:
    trade_tables = json.load(f)

# Create a set of trade tables for fast lookup
trade_tables_set = set(trade_tables)

# Filter stock_info for those that have a table in stocktrade
relevant_stocks = []
for item in stock_info:
    if item['Symbol'] in trade_tables_set:
        relevant_stocks.append(item)

print(f"Total relevant stocks: {len(relevant_stocks)}")
print("__RESULT__:")
print(json.dumps(relevant_stocks[:10])) # Just print first 10 to check structure"""

env_args = {'var_function-call-9844452746948468047': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8671132249438032894': 'file_storage/function-call-8671132249438032894.json', 'var_function-call-8671132249438035785': 'file_storage/function-call-8671132249438035785.json'}

exec(code, env_args)
