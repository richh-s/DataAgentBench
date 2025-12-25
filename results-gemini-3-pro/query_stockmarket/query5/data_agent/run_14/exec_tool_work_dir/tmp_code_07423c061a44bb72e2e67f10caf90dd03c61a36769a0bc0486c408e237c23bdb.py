code = """import json

# Load the result from the first query (stockinfo)
with open('var_function-call-13634932259963143763.json', 'r') as f:
    stock_info_list = json.load(f)

# Load the result from the second query (list_db)
with open('var_function-call-13634932259963145996.json', 'r') as f:
    table_list = json.load(f)

# Extract symbols from stock info
# Ensure symbols match table names (DuckDB table names are usually case sensitive or match what was listed)
# The list_db output shows uppercase symbols, stockinfo symbols are also uppercase.

target_tickers = []
ticker_to_desc = {}

table_set = set(table_list)

for item in stock_info_list:
    sym = item['Symbol']
    if sym in table_set:
        target_tickers.append(sym)
        ticker_to_desc[sym] = item['Company Description']

print("__RESULT__:")
print(json.dumps({"count": len(target_tickers), "tickers": target_tickers, "descriptions": ticker_to_desc}))"""

env_args = {'var_function-call-13634932259963143763': 'file_storage/function-call-13634932259963143763.json', 'var_function-call-13634932259963145996': 'file_storage/function-call-13634932259963145996.json'}

exec(code, env_args)
