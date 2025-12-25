code = """import json
import pandas as pd
import os

# Get file paths from local variables
stockinfo_path = locals()['var_function-call-4097608082559162712']
stocktrade_path = locals()['var_function-call-14328794898966256946']

# Load stockinfo result
with open(stockinfo_path, 'r') as f:
    stockinfo_data = json.load(f)

stockinfo_df = pd.DataFrame(stockinfo_data)
target_symbols = stockinfo_df['Symbol'].tolist()
print(f"Found {len(target_symbols)} symbols in NASDAQ Capital Market.")

# Load stocktrade tables result
with open(stocktrade_path, 'r') as f:
    stocktrade_tables = json.load(f)

print(f"Found {len(stocktrade_tables)} tables in stocktrade_database.")

# Find intersection
common_symbols = sorted(list(set(target_symbols) & set(stocktrade_tables)))
print(f"Found {len(common_symbols)} common symbols.")

print("__RESULT__:")
print(json.dumps(common_symbols))"""

env_args = {'var_function-call-4097608082559162712': 'file_storage/function-call-4097608082559162712.json', 'var_function-call-14328794898966256946': 'file_storage/function-call-14328794898966256946.json'}

exec(code, env_args)
