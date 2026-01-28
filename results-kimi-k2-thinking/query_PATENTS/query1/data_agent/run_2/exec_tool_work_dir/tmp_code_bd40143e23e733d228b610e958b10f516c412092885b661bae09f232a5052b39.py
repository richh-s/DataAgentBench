code = """import json
import os
import pandas as pd
import re

# Load the full data
filepath = var_functions.query_db:26
with open(filepath, 'r') as f:
    data = json.load(f)

print(f'Loaded {len(data)} records')

# Parse records and extract CPC codes with years
records = []
years_seen = set()

for item in data:
    try:
        pub_date = item.get('publication_date', '')
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            years_seen.add(year)
            
            cpc_str = item.get('cpc', '[]')
            cpc_list = json.loads(cpc_str)
            
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:  # Valid CPC format
                    # Level 5 is the full CPC code (e.g., H01M10/0525)
                    records.append({
                        'cpc_level5': code,
                        'year': year
                    })
    except Exception as e:
        continue

print(f'Parsed {len(records)} CPC records from {len(years_seen)} years: {sorted(years_seen)}')

# Create dataframe
df = pd.DataFrame(records)
if df.empty:
    print('No valid CPC data found')
else:
    print(f'Dataframe shape: {df.shape}, years range: {df["year"].min()}-{df["year"].max()}')
    
# Count patent filings per year for each CPC level 5 code
counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
print(f'Total CPC-year combinations: {len(counts)}')

# Calculate exponential moving average for each CPC code
alpha = 0.2
ema_results = []

for code in counts['cpc_level5'].unique():
    group = counts[counts['cpc_level5'] == code].copy()
    if len(group) < 2:  # Skip if only one year of data
        continue
    
    group = group.sort_values('year')
    
    # Initialize EMA with first value
    ema = group.iloc[0]['count']
    
    for _, row in group.iterrows():
        # If there's a gap in years, we still calculate EMA sequentially
        ema = alpha * row['count'] + (1 - alpha) * ema
        ema_results.append({
            'cpc_level5': code,
            'year': row['year'],
            'ema': round(ema, 2)
        })

ema_df = pd.DataFrame(ema_results)

# Find the year with maximum EMA for each CPC code
best_years_idx = ema_df.groupby('cpc_level5')['ema'].idxmax()
best_years = ema_df.loc[best_years_idx]

# Filter codes where the best year is 2022
best_2022 = best_years[best_years['year'] == 2022]

print(f'Found {len(best_2022)} CPC level 5 codes with best year 2022')

# Sort by EMA and get the codes
codes_2022 = best_2022.sort_values('ema', ascending=False)['cpc_level5'].tolist()

print('Top 10 codes:', codes_2022[:10])

result = codes_2022
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
