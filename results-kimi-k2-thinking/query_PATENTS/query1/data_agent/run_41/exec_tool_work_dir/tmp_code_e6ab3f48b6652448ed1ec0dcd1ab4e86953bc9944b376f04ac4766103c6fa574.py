code = """import json
import pandas as pd
import numpy as np
import re
from collections import defaultdict

# Load publication data
pub_file = locals()['var_functions.query_db:12']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print(f'Processing {len(pub_data)} publication records...')

# Process CPC codes and extract years
cpc_year_counts = defaultdict(lambda: defaultdict(int))
year_cpc_counts = defaultdict(lambda: defaultdict(int))
processed = 0

for item in pub_data[:100000]:  # Process first 100k to speed up
    try:
        # Extract year
        pub_date = item.get('publication_date', '')
        if not pub_date:
            continue
            
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        if year < 2000 or year > 2023:  # Filter reasonable years
            continue
        
        # Parse CPC codes
        cpc_str = item.get('cpc', '[]')
        if not cpc_str or cpc_str == '[]':
            continue
            
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if not code:
                    continue
                # Extract group code (part before slash)
                group = code.split('/')[0]
                if len(group) == 4:  # Level 5 groups are 4 chars like C01B
                    cpc_year_counts[group][year] += 1
                    year_cpc_counts[year][group] += 1
                    
        except:
            continue
            
        processed += 1
        
    except:
        continue

print(f'Processed {processed} records')
print(f'CPC groups found: {len(cpc_year_counts)}')

# Get all CPC groups and years
all_groups = sorted(cpc_year_counts.keys())
all_years = sorted(set(year for group in cpc_year_counts.values() for year in group.keys()))
print(f'Years: {all_years}')

# Create count matrix (groups x years)
matrix = []
for group in all_groups:
    row = [cpc_year_counts[group].get(year, 0) for year in all_years]
    matrix.append(row)

matrix_df = pd.DataFrame(matrix, index=all_groups, columns=all_years)
print(f'Matrix shape: {matrix_df.shape}')

# Calculate EMA (Exponential Moving Average) with factor 0.2
α = 0.2
ema_matrix = []
for group in all_groups:
    values = matrix_df.loc[group].values
    ema_values = []
    if len(values) > 0:
        ema_prev = values[0]
        for i, val in enumerate(values):
            if i == 0:
                ema_values.append(ema_prev)
            else:
                ema_current = α * val + (1-α) * ema_prev
                ema_values.append(ema_current)
                ema_prev = ema_current
    ema_matrix.append(ema_values)

ema_df = pd.DataFrame(ema_matrix, index=all_groups, columns=all_years)

# For each year, find top 10% groups by EMA
top_groups_per_year = {}
for year in all_years:
    year_ema = ema_df[year].sort_values(ascending=False)
    top_n = max(1, int(len(year_ema) * 0.1))
    top_groups = set(year_ema.head(top_n).index.tolist())
    top_groups_per_year[year] = top_groups

# Find groups whose best year is 2022 and were top performers that year
groups_best_2022 = []
for group in all_groups:
    group_ema = ema_df.loc[group]
    best_year = group_ema.idxmax()
    if best_year == 2022 and group in top_groups_per_year[2022]:
        groups_best_2022.append(group)

print(f'Groups with best year 2022: {len(groups_best_2022)}')

# Load level 5 CPC definitions to verify
level5_file = locals()['var_functions.query_db:18']
with open(level5_file, 'r') as f:
    level5_list = json.load(f)
level5_symbols = set(item['symbol'] for item in level5_list)

# Filter to only valid level 5 groups
valid_groups_best_2022 = [g for g in groups_best_2022 if g in level5_symbols]

result = {
    'count': len(valid_groups_best_2022),
    'groups': sorted(valid_groups_best_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
