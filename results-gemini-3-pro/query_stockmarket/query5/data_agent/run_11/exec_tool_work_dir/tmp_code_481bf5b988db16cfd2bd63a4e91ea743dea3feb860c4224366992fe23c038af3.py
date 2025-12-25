code = """import json
import pandas as pd

# Load stockinfo results
with open(locals()['var_function-call-9914396351492829632'], 'r') as f:
    stock_info = json.load(f)

# Load trade tables list
with open(locals()['var_function-call-9914396351492832197'], 'r') as f:
    trade_tables = json.load(f)
    trade_tables_set = set(trade_tables)

# Filter symbols
valid_symbols = []
for entry in stock_info:
    sym = entry['Symbol']
    if sym in trade_tables_set:
        valid_symbols.append(entry)

print(f"Total valid symbols: {len(valid_symbols)}")

# If number is manageable, we can generate a query.
# Let's print the first few to check.
print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-9914396351492829632': 'file_storage/function-call-9914396351492829632.json', 'var_function-call-9914396351492832197': 'file_storage/function-call-9914396351492832197.json'}

exec(code, env_args)
