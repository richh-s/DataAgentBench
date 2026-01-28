code = """import json
import pandas as pd
import re

# Get the file path from storage
query_key = 'var_functions.query_db:16'
file_path = locals()[query_key]

# Load the data
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse CPC codes and extract years
records = []
for row in data:
    cpc_json = row['cpc']
    pub_date = row['publication_date']
    
    # Extract year
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
            records.append({'cpc_code': code, 'year': year})
    except:
        continue

# Create DataFrame
df = pd.DataFrame(records)

# Filter for valid level 5 CPC codes
df_valid = df[df['cpc_code'].str.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$', na=False)].copy()

# Count per CPC code per year
cpc_year_counts = df_valid.groupby(['cpc_code', 'year']).size().reset_index(name='count')

# Get CPC codes in 2022
cpc_in_2022 = cpc_year_counts[cpc_year_counts['year'] == 2022]['cpc_code'].unique()

# Calculate EMA for each CPC code
alpha = 0.2
results = []

for cpc_code in cpc_in_2022:
    df_cpc = cpc_year_counts[cpc_year_counts['cpc_code'] == cpc_code].copy()
    df_cpc = df_cpc.sort_values('year')
    
    # Fill missing years
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
    
    # Find max EMA year
    max_idx = df_filled['ema'].idxmax()
    max_year = df_filled.loc[max_idx, 'year']
    
    if max_year == 2022:
        results.append(cpc_code)

# Output result
output = {'cpc_codes': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
