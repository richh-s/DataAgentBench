code = """import json
import pandas as pd
import numpy as np
import os

# Load CPC-year data
df_cpc_years = pd.read_json('/tmp/cpc_years_full.json')
print(f"Loaded {len(df_cpc_years)} records")

# Load level 5 symbols
storage_key = 'var_functions.query_db:14'
symbols_data = globals().get(storage_key) or locals().get(storage_key)

if isinstance(symbols_data, str) and os.path.exists(symbols_data):
    with open(symbols_data, 'r') as f:
        level5_list = json.load(f)
else:
    level5_list = symbols_data if isinstance(symbols_data, list) else []

level5_symbols = set(item['symbol'] for item in level5_list)
print(f"Level 5 symbols: {len(level5_symbols)}")

# Extract level 5 group codes
def get_level5_group(code):
    # Format: A01B33/00 -> A01B
    base = code.split('/')[0]
    return base[:4] if len(base) >= 4 else None

df_cpc_years['level5'] = df_cpc_years['cpc_code'].apply(get_level5_group)

# Filter for level 5 codes
df_filtered = df_cpc_years[df_cpc_years['level5'].isin(level5_symbols)]
print(f"Filtered records: {len(df_filtered)}")

# Count by group and year
grouped = df_filtered.groupby(['level5', 'year']).size().reset_index(name='count')

# Pivot to matrix
pivot = grouped.pivot(index='level5', columns='year', values='count').fillna(0)

print(f"Groups: {pivot.shape[0]}, Years: {pivot.shape[1]}")
print("Range:", pivot.columns.min(), "-", pivot.columns.max())

# Save
pivot.to_json('/tmp/group_matrix.json', orient='index')

result = {"groups": int(pivot.shape[0]), "years": int(pivot.shape[1])}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'records': 2141569, 'level5_symbols': 677}}

exec(code, env_args)
