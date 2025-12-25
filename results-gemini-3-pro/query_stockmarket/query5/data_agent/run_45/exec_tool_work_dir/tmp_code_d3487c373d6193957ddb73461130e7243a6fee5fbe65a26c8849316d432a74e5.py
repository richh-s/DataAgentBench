code = """import json
import pandas as pd

# Load stockinfo results
with open('var_function-call-752038609392442353.json', 'r') as f:
    stock_info = json.load(f)

# Load stocktrade tables list
with open('var_function-call-16254905597670293192.json', 'r') as f:
    trade_tables = json.load(f)

# Extract symbols
target_symbols = [item['Symbol'] for item in stock_info]
available_tables = set(trade_tables)

# Intersect
valid_symbols = [s for s in target_symbols if s in available_tables]

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-752038609392442353': 'file_storage/function-call-752038609392442353.json', 'var_function-call-16254905597670293192': 'file_storage/function-call-16254905597670293192.json'}

exec(code, env_args)
