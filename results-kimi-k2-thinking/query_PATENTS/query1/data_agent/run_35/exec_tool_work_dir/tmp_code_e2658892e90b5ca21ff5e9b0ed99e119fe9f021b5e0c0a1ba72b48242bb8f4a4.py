code = """import json
import pandas as pd
import numpy as np
import os

# Access the CPC-year data file
print("Loading CPC-year data...")
if os.path.exists('/tmp/cpc_years_full.json'):
    df_cpc_years = pd.read_json('/tmp/cpc_years_full.json')
    print(f"Loaded {len(df_cpc_years)} records")
    print(f"Years: {df_cpc_years['year'].min()} to {df_cpc_years['year'].max()}")
    print(f"Unique CPC codes: {df_cpc_years['cpc_code'].nunique()}")
else:
    print("File not found")
    df_cpc_years = pd.DataFrame(columns=['cpc_code', 'year'])

# Access level 5 symbols from storage
storage_key = 'var_functions.query_db:14'
if storage_key in globals():
    symbols_data = globals()[storage_key]
elif storage_key in locals():
    symbols_data = locals()[storage_key]
else:
    symbols_data = []

if isinstance(symbols_data, str) and os.path.exists(symbols_data):
    with open(symbols_data, 'r') as f:
        level5_list = json.load(f)
elif isinstance(symbols_data, list):
    level5_list = symbols_data
else:
    level5_list = []

level5_symbols = set(item['symbol'] for item in level5_list)
print(f"Loaded {len(level5_symbols)} level 5 CPC symbols")

print("__RESULT__:")
print(json.dumps({"records": len(df_cpc_years), "level5_symbols": len(level5_symbols)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
