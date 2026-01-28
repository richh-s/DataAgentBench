code = """import json

# Read the stockinfo data
with open('var_functions.query_db:2', 'r') as f:
    stock_list = json.load(f)

print(f"Total NYSE non-ETF stocks found: {len(stock_list)}")
print(f"Sample: {stock_list[:3]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
