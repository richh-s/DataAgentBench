code = """import pandas as pd
import json
import re
from datetime import datetime

# Access the query result file
result_file = var_functions.query_db:6

# Read the JSON data from file
with open(result_file, 'r') as f:
    data = json.load(f)

cpc_date_records = []

for record in data:
    cpc_json_str = record['cpc']
    publication_date_str = record['publication_date']
    
    if not cpc_json_str or not publication_date_str:
        continue
    
    # Parse CPC JSON
    try:
        if isinstance(cpc_json_str, str):
            cpc_list = json.loads(cpc_json_str)
        else:
            cpc_list = cpc_json_str
    except:
        continue
    
    # Parse date
    try:
        date_match = re.search(r'(\w+)\s+\d+(?:st|nd|rd|th)?,?\s+(\d{4})', publication_date_str)
        if date_match:
            month_str, year_str = date_match.groups()
            month_num = datetime.strptime(month_str[:3], '%b').month
            year = int(year_str)
        else:
            continue
    except:
        continue
    
    # Extract CPC codes
    if isinstance(cpc_list, list):
        for cpc_item in cpc_list:
            if isinstance(cpc_item, dict) and 'code' in cpc_item:
                code = cpc_item['code']
                if '/' in code:
                    group_code = code.split('/')[0]
                    cpc_date_records.append({
                        'full_code': code,
                        'group_code': group_code,
                        'year': year
                    })

# Create DataFrame
df = pd.DataFrame(cpc_date_records)

# Count filings per year for each group code
group_year_counts = df.groupby(['group_code', 'year']).size().reset_index(name='count')

# Get level 5 CPC codes (format: X##X##/## - we want the part before / which should be 5 characters)
# Actually level 5 means the group has 5 characters like A01BX, but let's check the CPC definition table
level_5_groups = set()
for code in df['group_code'].unique():
    if len(code) == 5:
        level_5_groups.add(code)

# Filter for level 5 groups
level_5_df = group_year_counts[group_year_counts['group_code'].isin(level_5_groups)]

# Calculate exponential moving average for each group
results = []
alpha = 0.2

for group_code in level_5_groups:
    group_data = level_5_df[level_5_df['group_code'] == group_code].copy()
    if len(group_data) == 0:
        continue
    
    # Fill missing years with 0
    years = range(group_data['year'].min(), group_data['year'].max() + 1)
    full_years = pd.DataFrame({'year': years})
    group_data = full_years.merge(group_data, on='year', how='left').fillna(0)
    
    # Calculate EMA
    ema = group_data['count'].iloc[0]
    ema_values = [ema]
    
    for i in range(1, len(group_data)):
        ema = alpha * group_data['count'].iloc[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    group_data['ema'] = ema_values
    
    # Find best year (highest EMA)
    best_idx = group_data['ema'].idxmax()
    best_year = group_data.loc[best_idx, 'year']
    best_ema = group_data.loc[best_idx, 'ema']
    
    results.append({
        'group_code': group_code,
        'best_year': best_year,
        'best_ema': best_ema
    })

results_df = pd.DataFrame(results)

# Get groups with best year 2022
best_2022 = results_df[results_df['best_year'] == 2022]

# Sort by EMA descending
best_2022_sorted = best_2022.sort_values('best_ema', ascending=False)

output = {
    'total_level_5_groups': len(level_5_groups),
    'groups_with_best_year_2022': len(best_2022_sorted),
    'group_codes_2022': best_2022_sorted['group_code'].tolist()
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
