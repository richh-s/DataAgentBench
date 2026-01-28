code = """import json
import pandas as pd
import re

# Load the data from the file
file_path = locals()['var_functions.query_db:16']
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Processing {len(data)} records...")

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
df_valid = df[df['cpc_code'].str.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$', na=False)].copy()
print(f"Valid level 5 CPC records: {len(df_valid)}")

# Count filings per CPC code per year
cpc_year_counts = df_valid.groupby(['cpc_code', 'year']).size().reset_index(name='count')
print(f"Unique CPC codes: {cpc_year_counts['cpc_code'].nunique()}")
print(f"Year range: {cpc_year_counts['year'].min()} to {cpc_year_counts['year'].max()}")

# Get CPC codes that appear in 2022
cpc_in_2022 = cpc_year_counts[cpc_year_counts['year'] == 2022]['cpc_code'].unique()
print(f"CPC codes appearing in 2022: {len(cpc_in_2022)}")

# Calculate EMA for each CPC code that appears in 2022
alpha = 0.2
results = []

for cpc_code in cpc_in_2022[:100]:  # Process first 100 to avoid timeout
    df_cpc = cpc_year_counts[cpc_year_counts['cpc_code'] == cpc_code].copy()
    df_cpc = df_cpc.sort_values('year')
    
    # Fill missing years with 0
    years = list(range(df_cpc['year'].min(), df_cpc['year'].max() + 1))
    df_filled = pd.DataFrame({'year': years})
    df_filled = df_filled.merge(df_cpc[['year', 'count']], on='year', how='left')
    df_filled['count'] = df_filled['count'].fillna(0)
    
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
    
    if max_year == 2022:
        results.append({
            'cpc_code': cpc_code,
            'best_year': max_year,
            'max_ema': max_ema,
            'count_2022': df_filled[df_filled['year'] == 2022]['count'].iloc[0]
        })

df_results = pd.DataFrame(results)
print(f"CPC codes with best year 2022: {len(df_results)}")

if len(df_results) > 0:
    df_results = df_results.sort_values('max_ema', ascending=False)
    print("Top 10:")
    print(df_results.head(10))
    
    cpc_codes_2022 = df_results['cpc_code'].tolist()
    
    # Prepare final result
    final_result = {
        'cpc_codes_count': len(cpc_codes_2022),
        'cpc_codes': cpc_codes_2022
    }
    
    __RESULT__ = json.dumps(final_result)
else:
    __RESULT__ = json.dumps({'cpc_codes_count': 0, 'cpc_codes': []})

print(__RESULT__)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
