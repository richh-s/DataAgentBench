code = """import json
import pandas as pd
import numpy as np
import os

# Load the CPC-year data from publication database
print("Loading CPC-year data...")
cpc_years_file = '/tmp/cpc_years_full.json'
if os.path.exists(cpc_years_file):
    df_cpc_years = pd.read_json(cpc_years_file)
    print(f"Loaded {len(df_cpc_years)} CPC-year records")
    print("Year range:", df_cpc_years['year'].min(), "to", df_cpc_years['year'].max())
else:
    print("CPC-year file not found")
    df_cpc_years = pd.DataFrame()

# Load level 5 CPC symbols from CPC definition database
print("\nLoading level 5 CPC symbols...")
storage_key = 'var_functions.query_db:14'
file_path = globals().get(storage_key) or locals().get(storage_key)

if isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        level5_symbols = json.load(f)
elif isinstance(file_path, list):
    level5_symbols = file_path
else:
    level5_symbols = []

print(f"Loaded {len(level5_symbols)} level 5 CPC symbols")

# Create a set of level 5 symbols for fast lookup
level5_set = set(item['symbol'] for item in level5_symbols)
print("Sample level 5 symbols:", list(level5_set)[:10])

print("__RESULT__:")
print(json.dumps(f"Data loaded: {len(df_cpc_years)} records, {len(level5_set)} level 5 CPC symbols"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
