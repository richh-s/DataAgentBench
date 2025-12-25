code = """import json

# Get file paths from variables
path_stock_info = locals()['var_function-call-8671132249438032894']
path_trade_tables = locals()['var_function-call-8671132249438035785']

# Load stockinfo result
with open(path_stock_info, 'r') as f:
    stock_info = json.load(f)

# Load stocktrade table list
with open(path_trade_tables, 'r') as f:
    trade_tables = json.load(f)

# Create a set of trade tables for fast lookup
trade_tables_set = set(trade_tables)

# Filter stock_info for those that have a table in stocktrade
relevant_stocks = []
for item in stock_info:
    if item['Symbol'] in trade_tables_set:
        relevant_stocks.append(item)

# Output count and preview
result = {
    "count": len(relevant_stocks),
    "preview": relevant_stocks[:10],
    "all_symbols": [s['Symbol'] for s in relevant_stocks]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9844452746948468047': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-8671132249438032894': 'file_storage/function-call-8671132249438032894.json', 'var_function-call-8671132249438035785': 'file_storage/function-call-8671132249438035785.json'}

exec(code, env_args)
