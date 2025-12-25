code = """import json
import pandas as pd

# Load stockinfo result
with open('var_function-call-14301945511223140359.json', 'r') as f:
    etf_list = json.load(f)

# Load stocktrade result
with open('var_function-call-6882633768806362112.json', 'r') as f:
    table_list = json.load(f)

# Extract symbols
etf_symbols = set([item['Symbol'] for item in etf_list])
available_tables = set(table_list)

# Intersection
valid_symbols = list(etf_symbols.intersection(available_tables))

print("__RESULT__:")
print(json.dumps({"count": len(valid_symbols), "preview": valid_symbols[:10]}))"""

env_args = {'var_function-call-14301945511223140359': 'file_storage/function-call-14301945511223140359.json', 'var_function-call-6882633768806362112': 'file_storage/function-call-6882633768806362112.json'}

exec(code, env_args)
