code = """import json
import pandas as pd
import re
import os

# Get the file path from storage
file_path = locals()['var_functions.query_db:7']
print(f"Loading data from: {file_path}")

# Check if file exists and load it
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    print(f"Successfully loaded {len(data)} records")
else:
    print(f"File not found: {file_path}")
    exit()

# Parse CPC codes and extract years
records = []
for row in data:
    cpc_json = row['cpc']
    pub_date = row['publication_date']
    
    # Extract year from publication date
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON
    try:
        if isinstance(cpc_json, str):
            cpc_list = json.loads(cpc_json)
        else:
            cpc_list = cpc_json
            
        for cpc_entry in cpc_list:
            code = cpc_entry['code']
            records.append({
                'cpc_code': code,
                'year': year
            })
    except:
        continue

# Create DataFrame
df = pd.DataFrame(records)
print(f"Total CPC records: {len(df)}")
print(f"Year range: {df['year'].min()} to {df['year'].max()}")

# Filter for valid CPC codes at level 5
# CPC level 5 format: Section (1 char) + Class (2 digits) + Subclass (1 char) + Main group (2+ digits) + Subgroup (2+ digits)
# Example: G06F16/00, H01M10/05
df_valid = df[df['cpc_code'].str.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$', na=False)].copy()
print(f"Valid level 5 CPC records: {len(df_valid)}")

# Count filings per CPC code per year
cpc_year_counts = df_valid.groupby(['cpc_code', 'year']).size().reset_index(name='count')
print(f"Unique CPC codes: {cpc_year_counts['cpc_code'].nunique()}")
print(f"Year range in counts: {cpc_year_counts['year'].min()} to {cpc_year_counts['year'].max()}")

# For each CPC code, calculate EMA and find best year
alpha = 0.2
results = []

for cpc_code in cpc_year_counts['cpc_code'].unique():
    df_cpc = cpc_year_counts[cpc_year_counts['cpc_code'] == cpc_code].copy()
    df_cpc = df_cpc.sort_values('year')
    
    # Fill missing years with 0
    years = list(range(df_cpc['year'].min(), df_cpc['year'].max() + 1))
    df_filled = pd.DataFrame({'year': years})
    df_filled = df_filled.merge(df_cpc[['year', 'count']], on='year', how='left')
    df_filled['count'] = df_filled['count'].fillna(0)
    df_filled['cpc_code'] = cpc_code
    
    # Calculate EMA
    ema_values = []
    ema = df_filled['count'].iloc[0]
    ema_values.append(ema)
    
    for i in range(1, len(df_filled)):
        ema = alpha * df_filled['count'].iloc[i] + (1 - alpha) * ema
        ema_values.append(ema)
    
    df_filled['ema'] = ema_values
    
    # Find year with max EMA
    max_idx = df_filled['ema'].idxmax()
    max_year = df_filled.loc[max_idx, 'year']
    max_ema = df_filled.loc[max_idx, 'ema']
    
    results.append({
        'cpc_code': cpc_code,
        'best_year': max_year,
        'max_ema': max_ema
    })

df_results = pd.DataFrame(results)

# Filter for CPC codes where best year is 2022
df_best_2022 = df_results[df_results['best_year'] == 2022]
print(f"CPC codes with best year 2022: {len(df_best_2022)}")

if len(df_best_2022) > 0:
    # Sort by max_ema descending to get top ones
    df_best_2022 = df_best_2022.sort_values('max_ema', ascending=False)
    print("Top 10 CPC codes with best year 2022:")
    print(df_best_2022.head(10))
    
    cpc_codes_2022 = df_best_2022['cpc_code'].tolist()
    
    # Prepare final result
    final_result = {
        'cpc_codes_count': len(cpc_codes_2022),
        'cpc_codes': cpc_codes_2022
    }
    
    __RESULT__ = json.dumps(final_result)
else:
    __RESULT__ = json.dumps({'cpc_codes_count': 0, 'cpc_codes': []})"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
