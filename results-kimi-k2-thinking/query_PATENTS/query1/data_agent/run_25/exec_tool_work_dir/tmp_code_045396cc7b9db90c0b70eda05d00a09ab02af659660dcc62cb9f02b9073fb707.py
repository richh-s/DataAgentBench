code = """import json
import pandas as pd
import numpy as np
from collections import defaultdict

# Load the data and compute EMAs for each CPC code
file_key = 'var_functions.query_db:2'
file_path = locals()[file_key]

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract counts per CPC code per year
patent_counts = defaultdict(lambda: defaultdict(int))

for record in data:
    pub_date = record.get('publication_date', '')
    cpc_data = record.get('cpc', '')
    
    if pub_date and cpc_data and str(pub_date) != 'None':
        year_match = re.search(r'(\d{4})', str(pub_date))
        if year_match:
            year = int(year_match.group(1))
            
            try:
                cpc_list = json.loads(cpc_data)
                for cpc_entry in cpc_list:
                    if isinstance(cpc_entry, dict) and 'code' in cpc_entry:
                        code = str(cpc_entry['code'])
                        if '/' in code:
                            patent_counts[code][year] += 1
            except:
                continue

# Convert to DataFrame
records = []
for code, years in patent_counts.items():
    for year, count in years.items():
        records.append({'cpc_code': code, 'year': year, 'count': count})

df = pd.DataFrame(records)

# Focus on recent years (2010-2024) for meaningful EMA analysis
df_recent = df[df['year'] >= 2010].copy()

# Calculate EMA (smoothing factor = 0.2) for each CPC code
ema_results = []
alpha = 0.2

for cpc_code in df_recent['cpc_code'].unique():
    cpc_data = df_recent[df_recent['cpc_code'] == cpc_code].copy()
    cpc_data = cpc_data.sort_values('year')
    
    if len(cpc_data) > 1:  # Need at least 2 years of data
        # Initialize EMA with first year's count
        ema_values = []
        first_count = cpc_data.iloc[0]['count']
        ema_prev = first_count
        
        for _, row in cpc_data.iterrows():
            year = row['year']
            count = row['count']
            # EMA formula: EMA_t = α * value_t + (1-α) * EMA_{t-1}
            ema_current = alpha * count + (1 - alpha) * ema_prev
            ema_values.append({
                'cpc_code': cpc_code,
                'year': year,
                'count': count,
                'ema': ema_current
            })
            ema_prev = ema_current
        
        ema_results.extend(ema_values)

ema_df = pd.DataFrame(ema_results)

# Find CPC code with highest EMA for each year
best_per_year = []
for year in ema_df['year'].unique():
    year_data = ema_df[ema_df['year'] == year]
    if not year_data.empty:
        max_ema_row = year_data.loc[year_data['ema'].idxmax()]
        best_per_year.append({
            'year': year,
            'best_cpc_code': max_ema_row['cpc_code'],
            'max_ema': max_ema_row['ema'],
            'count_at_max': max_ema_row['count']
        })

best_per_year_df = pd.DataFrame(best_per_year)

# For each CPC code that appears as best in any year, find its best year
cpc_best_years = []
for cpc_code in best_per_year_df['best_cpc_code'].unique():
    cpc_best_data = best_per_year_df[best_per_year_df['best_cpc_code'] == cpc_code]
    best_row = cpc_best_data.loc[cpc_best_data['max_ema'].idxmax()]
    cpc_best_years.append({
        'cpc_code': cpc_code,
        'best_year': best_row['year'],
        'best_ema': best_row['max_ema'],
        'best_count': best_row['count_at_max']
    })

cpc_best_years_df = pd.DataFrame(cpc_best_years)

# Filter for CPC codes whose best year is 2022
cpc_2022_best = cpc_best_years_df[cpc_best_years_df['best_year'] == 2022]

result_summary = {
    'total_cpc_codes_analyzed': len(df_recent['cpc_code'].unique()),
    'years_analyzed': f"{df_recent['year'].min()} to {df_recent['year'].max()}",
    'codes_with_best_year_2022': len(cpc_2022_best),
    'best_codes_2022': cpc_2022_best['cpc_code'].tolist()
}

print('__RESULT__:')
print(json.dumps(result_summary, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 250551, 'unique_cpc_codes': 97719, 'year_range': '1837 to 2024', 'sample_cpc_codes': ['C01B33/00', 'C01B35/00', 'H01M10/0565', 'H01M10/0562', 'C01G45/006', 'H01M10/0566', 'H01M10/052', 'C01P2002/76', 'Y02E60/10', 'H01M10/0525'], 'has_2022': True}}

exec(code, env_args)
