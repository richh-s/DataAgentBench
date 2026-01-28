code = """import json
import pandas as pd
import numpy as np
import os
from collections import defaultdict

# Load the CPC-year data
print("Loading CPC-year data...")
df_cpc_years = pd.read_json('/tmp/cpc_years_full.json')
print(f"Total records: {len(df_cpc_years)}")

# Load level 5 CPC symbols
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
print(f"Level 5 symbols: {len(level5_symbols)}")

# Filter to only include level 5 CPC codes
# CPC format: section (1 char), class (2 digits), subclass (1 letter), group (1-4 digits), 
# then optional subgroup after /
# Level 5 appears to be the group level (e.g., A01B, B29C)

def extract_level5_code(cpc_code):
    """Extract level 5 code from full CPC code"""
    # Remove subgroup part after slash if present
    code = cpc_code.split('/')[0]
    # Extract first 4-5 characters depending on format
    # Level 5 codes in the data look like A01B, B29C, etc (4 chars)
    if len(code) >= 4:
        return code[:4]
    return None

# Add level 5 group column
df_cpc_years['level5_group'] = df_cpc_years['cpc_code'].apply(extract_level5_code)

# Filter to only keep level 5 groups
df_filtered = df_cpc_years[df_cpc_years['level5_group'].isin(level5_symbols)]
print(f"Records with level 5 codes: {len(df_filtered)}")

# Count filings per year for each level 5 group
group_counts = df_filtered.groupby(['level5_group', 'year']).size().reset_index(name='count')
print("Sample group counts:")
print(group_counts.head())

# Pivot to get years as columns
group_pivot = group_counts.pivot(index='level5_group', columns='year', values='count')
# Fill missing years with 0
group_pivot = group_pivot.fillna(0)

print(f"Matrix shape: {group_pivot.shape}")
print(f"Groups: {group_pivot.shape[0]}, Years: {group_pivot.shape[1]}")
print("Year range from", group_pivot.columns.min(), "to", group_pivot.columns.max())

# Save processed data
group_pivot.to_json('/tmp/group_counts_matrix.json', orient='index')
group_counts.to_json('/tmp/group_counts_list.json', orient='records')

print("__RESULT__:")
print(json.dumps({"status": "processed", "groups": group_pivot.shape[0], "years": group_pivot.shape[1]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': 'Processed 2141569 records, years 1837-2024', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'records': 2141569, 'level5_symbols': 677}}

exec(code, env_args)
