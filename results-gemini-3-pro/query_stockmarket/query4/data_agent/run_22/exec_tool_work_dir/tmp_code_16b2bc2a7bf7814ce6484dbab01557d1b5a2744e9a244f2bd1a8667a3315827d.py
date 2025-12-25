code = """import json

# Load symbols from step 1
with open(locals()['var_function-call-1631025954943238764'], 'r') as f:
    stock_info = json.load(f)

# Load tables from step 2
with open(locals()['var_function-call-4060108603261474737'], 'r') as f:
    tables = set(json.load(f))

# Filter
target_stocks = []
for item in stock_info:
    sym = item['Symbol']
    if sym in tables:
        target_stocks.append(item)

print(f"Total matching stocks: {len(target_stocks)}")
print("__RESULT__:")
print(json.dumps(target_stocks)) # Print all to pass to next step if manageable"""

env_args = {'var_function-call-16810398710687085223': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-1631025954943238764': 'file_storage/function-call-1631025954943238764.json', 'var_function-call-4060108603261474737': 'file_storage/function-call-4060108603261474737.json'}

exec(code, env_args)
