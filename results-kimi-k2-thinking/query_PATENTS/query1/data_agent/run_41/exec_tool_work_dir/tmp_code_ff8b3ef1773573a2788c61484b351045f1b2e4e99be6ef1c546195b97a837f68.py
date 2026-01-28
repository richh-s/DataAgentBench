code = """import json
import pandas as pd
import numpy as np
import re
from collections import defaultdict

# Load level 5 CPC symbols
level5_file = locals()['var_functions.query_db:18']
with open(level5_file, 'r') as f:
    level5_symbols = json.load(f)

level5_set = set(item['symbol'] for item in level5_symbols)
print(f'Number of level 5 CPC symbols: {len(level5_set)}')
print('Sample level 5 symbols:', list(level5_set)[:20])

# Load publication data
pub_file = locals()['var_functions.query_db:12']
with open(pub_file, 'r') as f:
    pub_data = json.load(f)

print(f'Processing {len(pub_data)} publication records...')

# Process CPC codes and extract level 5 groups
cpc_year_counts = defaultdict(lambda: defaultdict(int))
processed = 0
errors = 0

for item in pub_data:
    try:
        # Extract year from publication_date
        pub_date = item.get('publication_date', '')
        if not pub_date:
            continue
            
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            continue
            
        year = int(year_match.group(1))
        
        # Parse CPC codes
        cpc_str = item.get('cpc', '[]')
        if not cpc_str or cpc_str == '[]':
            continue
            
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_entry in cpc_list:
                cpc_code = cpc_entry.get('code', '')
                if not cpc_code:
                    continue
                    
                # Extract level 5 group (part before slash, truncated to 4 chars)
                # Format is typically like "C01B33/00" where "C01B" is the group
                group_code = cpc_code.split('/')[0][:4]
                
                # Only count if it's a valid level 5 code
                if group_code in level5_set:
                    cpc_year_counts[group_code][year] += 1
                    
        except json.JSONDecodeError:
            errors += 1
            continue
            
        processed += 1
        
    except Exception as e:
        errors += 1
        continue

print(f'Processed {processed} records, {errors} errors')
print(f'Found {len(cpc_year_counts)} level 5 CPC groups with filings')

# Get all years
all_years = sorted(set(year for cpc in cpc_year_counts.values() for year in cpc.keys()))
print(f'Years range: {all_years}')

# Create matrix of counts per CPC group per year
cpc_groups = sorted(cpc_year_counts.keys())
matrix = []
for group in cpc_groups:
    row = [cpc_year_counts[group].get(year, 0) for year in all_years]
    matrix.append(row)

matrix_df = pd.DataFrame(matrix, index=cpc_groups, columns=all_years)
print(f'Count matrix shape: {matrix_df.shape}')

# Calculate EMA for each group
α = 0.2
ema_matrix = []

for idx, group in enumerate(cpc_groups):
    values = matrix_df.loc[group].values
    ema_values = []
    ema_prev = values[0] if len(values) > 0 else 0
    
    for i, val in enumerate(values):
        if i == 0:
            ema_values.append(ema_prev)
        else:
            ema_current = α * val + (1-α) * ema_prev
            ema_values.append(ema_current)
            ema_prev = ema_current
    
    ema_matrix.append(ema_values)

ema_df = pd.DataFrame(ema_matrix, index=cpc_groups, columns=all_years)
print(f'EMA matrix shape: {ema_df.shape}')

# For each year, find groups with highest EMA (top 10%)
yearly_top_groups = {}
for year in all_years:
    year_ema = ema_df[year].sort_values(ascending=False)
    top_n = max(1, int(len(year_ema) * 0.1))  # Top 10%
    top_groups = year_ema.head(top_n).index.tolist()
    yearly_top_groups[year] = set(top_groups)

print('Top groups per year:')
for year in sorted(yearly_top_groups.keys())[-5:]:
    print(f'{year}: {len(yearly_top_groups[year])} groups')

# Find groups whose best year (highest EMA) is 2022
groups_best_year_2022 = []
for group in cpc_groups:
    group_ema = ema_df.loc[group]
    max_ema = group_ema.max()
    best_year = group_ema.idxmax()
    
    # Check if best year is 2022 and if it was in top performers for 2022
    if best_year == 2022 and group in yearly_top_groups[2022]:
        groups_best_year_2022.append(group)

print(f'\nGroups with best year 2022: {len(groups_best_year_2022)}')
print('Sample groups:', groups_best_year_2022[:20])

# Save results
result = {
    'total_level5_groups': len(level5_set),
    'groups_with_filings': len(cpc_groups),
    'year_range': all_years,
    'groups_best_year_2022': sorted(groups_best_year_2022),
    'count_best_year_2022': len(groups_best_year_2022)
}

with open('/tmp/final_results.json', 'w') as f:
    json.dump(result, f, indent=2)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:11': ['cpc_definition'], 'var_functions.query_db:10': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 277813, 'cpc_year_records': 2681388, 'unique_cpcs': 175852, 'sample_cpcs': ['Y10T29/23', 'B08B9/093', 'H03B5/30', 'F25B2313/0315', 'G05B9/02', 'A61C17/10', 'A23V2400/157', 'C02F11/06', 'G11C17/14', 'F23D2900/03081']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
