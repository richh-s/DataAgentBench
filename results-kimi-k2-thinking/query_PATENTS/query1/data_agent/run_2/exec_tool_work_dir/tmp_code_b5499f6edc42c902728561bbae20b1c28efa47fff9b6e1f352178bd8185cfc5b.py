code = """import json
import os
import pandas as pd
import re

# Load the data
filepath = locals()['var_functions.query_db:2']
with open(filepath, 'r') as f:
    raw_data = json.load(f)

print('Loaded data size:', len(raw_data))

# Parse CPC codes and dates
records = []
for item in raw_data:
    try:
        pub_date = item.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        cpc_str = item.get('cpc', '[]')
        cpc_list = json.loads(cpc_str)
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if code and '/' in code:
                records.append({
                    'code': code,
                    'year': year
                })
    except Exception as e:
        print(f'Error parsing record: {e}')
        continue

print('Parsed records:', len(records))

# Create dataframe
df = pd.DataFrame(records)
print('Year range:', df['year'].min(), '-', df['year'].max())

# Extract level 5 CPC codes (full codes)
def get_level5(code):
    return code if code and '/' in code else None

df['cpc_level5'] = df['code'].apply(get_level5)

# Count per year
counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
print('Total CPC-year combinations:', len(counts))

# Calculate EMA
def calc_ema(group, alpha=0.2):
    group = group.sort_values('year')
    ema = group.iloc[0]['count']
    results = [{'year': group.iloc[0]['year'], 'ema': ema}]
    
    for _, row in group.iloc[1:].iterrows():
        ema = alpha * row['count'] + (1 - alpha) * ema
        results.append({'year': row['year'], 'ema': ema})
    
    return pd.DataFrame(results)

# Process each CPC code
all_ema = []
for code in counts['cpc_level5'].unique():
    group = counts[counts['cpc_level5'] == code]
    if len(group) > 1:
        ema_df = calc_ema(group)
        ema_df['cpc_level5'] = code
        all_ema.append(ema_df)

if all_ema:
    ema_df = pd.concat(all_ema, ignore_index=True)
    
    # Find best year for each code
    best_years = ema_df.loc[ema_df.groupby('cpc_level5')['ema'].idxmax()]
    
    # Filter for 2022
    best_2022 = best_years[best_years['year'] == 2022]
    
    print('Codes with best year 2022:', len(best_2022))
    
    result = best_2022['cpc_level5'].tolist()
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}}

exec(code, env_args)
