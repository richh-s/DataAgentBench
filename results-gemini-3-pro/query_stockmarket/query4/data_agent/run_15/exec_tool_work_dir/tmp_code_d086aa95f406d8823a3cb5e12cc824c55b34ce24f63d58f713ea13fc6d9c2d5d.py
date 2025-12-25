code = """import json

# Load stock info
with open(locals()['var_function-call-8629880559091051052'], 'r') as f:
    stock_info = json.load(f)

# Load table list
with open(locals()['var_function-call-8629880559091050687'], 'r') as f:
    tables = json.load(f)

# Create a set of available tables
tables_set = set(tables)

# Filter stock info for those that have a table
# stock_info is a list of dicts: {"Symbol": "...", "Company Description": "..."}
# We need to preserve the company description for the final answer.
target_stocks = []
for item in stock_info:
    sym = item['Symbol']
    if sym in tables_set:
        target_stocks.append(item)

print("__RESULT__:")
print(len(target_stocks))
print(json.dumps(target_stocks[:5])) # Print a few to check
print(json.dumps([s['Symbol'] for s in target_stocks])) # Print all symbols to construct query"""

env_args = {'var_function-call-8629880559091051052': 'file_storage/function-call-8629880559091051052.json', 'var_function-call-8629880559091050687': 'file_storage/function-call-8629880559091050687.json'}

exec(code, env_args)
