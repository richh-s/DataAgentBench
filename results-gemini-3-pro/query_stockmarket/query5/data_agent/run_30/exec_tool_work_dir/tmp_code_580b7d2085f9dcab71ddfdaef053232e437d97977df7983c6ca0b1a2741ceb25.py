code = """import json
import pandas as pd

# Load stockinfo result
with open(locals()['var_function-call-13857162753557015436'], 'r') as f:
    stock_info = json.load(f)

# Load stocktrade tables list
with open(locals()['var_function-call-4722066765567143582'], 'r') as f:
    tables = json.load(f)

# Convert tables to a set for fast lookup
tables_set = set(tables)

# Filter stock info for symbols present in tables
valid_stocks = [s for s in stock_info if s['Symbol'] in tables_set]

print(f"Total symbols in stockinfo: {len(stock_info)}")
print(f"Total tables: {len(tables)}")
print(f"Valid overlapping symbols: {len(valid_stocks)}")

# If valid_stocks is small enough (e.g. < 100), we can just build the query.
# If it's larger, we might need batching.
# Let's verify the list of symbols.
print("__RESULT__:")
print(json.dumps([s['Symbol'] for s in valid_stocks]))"""

env_args = {'var_function-call-13857162753557015436': 'file_storage/function-call-13857162753557015436.json', 'var_function-call-4722066765567143582': 'file_storage/function-call-4722066765567143582.json'}

exec(code, env_args)
