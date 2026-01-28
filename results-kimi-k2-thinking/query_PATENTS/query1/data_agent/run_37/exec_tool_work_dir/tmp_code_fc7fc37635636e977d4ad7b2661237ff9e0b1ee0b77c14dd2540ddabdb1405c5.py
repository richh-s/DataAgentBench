code = """import json
import pandas as pd
import re
from datetime import datetime

# Read the data from the file
file_path = 'file_storage/functions.query_db:6.json'
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Loaded {len(data)} records")

# Parse CPC codes and extract year
cpc_records = []
for record in data:
    cpc_data = record.get('cpc', '')
    pub_date = record.get('publication_date', '')
    
    if not cpc_data or not pub_date:
        continue
    
    # Parse date
    try:
        date_match = re.search(r'(\w+)\s+\d+(?:st|nd|rd|th)?,?\s+(\d{4})', pub_date)
        if date_match:
            month_str, year_str = date_match.groups()
            year = int(year_str)
        else:
            continue
    except:
        continue
    
    # Parse CPC codes
    try:
        if isinstance(cpc_data, str):
            cpc_list = json.loads(cpc_data)
        else:
            cpc_list = cpc_data
    except:
        continue
    
    if isinstance(cpc_list, list):
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                if '/' in code:
                    group_code = code.split('/')[0]
                    # Level 5 CPC codes have exactly 5 characters in the group
                    if len(group_code) == 5:
                        cpc_records.append({
                            'group_code': group_code,
                            'year': year
                        })

# Create DataFrame
df = pd.DataFrame(cpc_records)
print(f"Extracted {len(df)} level 5 CPC records")

# Count filings per year for each group code
group_year_counts = df.groupby(['group_code', 'year']).size().reset_index(name='count')

# Calculate exponential moving average for each group
alpha = 0.2
results = []

for group_code in group_year_counts['group_code'].unique():
    group_data = group_year_counts[group_year_counts['group_code'] == group_code].copy()
    if len(group_data) < 2:  # Need at least 2 years for meaningful EMA
        continue
    
    # Fill missing years with 0
    years = range(group_data['year'].min(), group_data['year'].max() + 1)
    full_years = pd.DataFrame({'year': years})
    group_data = full_years.merge(group_data, on='year', how='left').fillna(0)
    
    # Calculate EMA
    ema = group_data['count'].iloc[0]
    max_ema = ema
    best_year = group_data['year'].iloc[0]
    
    for i in range(1, len(group_data)):
        ema = alpha * group_data['count'].iloc[i] + (1 - alpha) * ema
        if ema > max_ema:
            max_ema = ema
            best_year = group_data['year'].iloc[i]
    
    results.append({
        'group_code': group_code,
        'best_year': best_year,
        'best_ema': max_ema
    })

results_df = pd.DataFrame(results)

# Get groups with best year 2022
best_2022 = results_df[results_df['best_year'] == 2022]

# Prepare output
output = {
    'total_groups_analyzed': len(results_df),
    'groups_with_best_year_2022': len(best_2022),
    'cpc_group_codes_best_2022': best_2022['group_code'].tolist()
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:20': {'file_path': 'file_storage/functions.query_db:6.json', 'type': "<class 'str'>"}}

exec(code, env_args)
