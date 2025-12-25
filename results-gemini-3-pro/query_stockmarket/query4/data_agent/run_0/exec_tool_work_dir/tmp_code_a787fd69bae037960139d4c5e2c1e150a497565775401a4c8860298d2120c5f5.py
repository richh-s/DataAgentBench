code = """import json

# Load stockinfo result
with open(locals()['var_function-call-18147196658339150009'], 'r') as f:
    stockinfo_list = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-7489045623888971666'], 'r') as f:
    stocktrade_tables = json.load(f)

# Create a set of tables for fast lookup
stocktrade_tables_set = set(stocktrade_tables)

# Filter
relevant_stocks = []
for item in stockinfo_list:
    sym = item['Symbol']
    if sym in stocktrade_tables_set:
        relevant_stocks.append(item)

print(f"Total relevant stocks: {len(relevant_stocks)}")
print(f"First 10: {[s['Symbol'] for s in relevant_stocks[:10]]}")

print("__RESULT__:")
print(json.dumps(relevant_stocks))"""

env_args = {'var_function-call-3716719748068765207': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-18147196658339150009': 'file_storage/function-call-18147196658339150009.json', 'var_function-call-7489045623888971666': 'file_storage/function-call-7489045623888971666.json'}

exec(code, env_args)
