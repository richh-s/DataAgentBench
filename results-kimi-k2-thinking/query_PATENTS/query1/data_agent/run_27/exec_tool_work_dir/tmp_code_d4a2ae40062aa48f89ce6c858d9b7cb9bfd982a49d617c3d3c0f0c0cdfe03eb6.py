code = """import json
import pandas as pd
import re

# Load the data file
file_path = locals()['var_functions.query_db:50']
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
            records.append({'cpc_code': code, 'year': year})
    except:
        continue

# Create DataFrame
df = pd.DataFrame(records)
print(f"Total CPC records: {len(df)}")

# Filter for valid CPC level 5 codes (format: X99X99/99)
# Section (1 char) + Class (2 digits) + Subclass (1 char) + Main group (2+ digits) + Subgroup (2+ digits)
df_valid = df[df['cpc_code'].str.match(r'^[A-Z]\d{2}[A-Z]\d{2,}/\d{2,}$', na=False)].copy()
print(f"Valid level 5 CPC records: {len(df_valid)}")

# Count filings per CPC code per year
cpc_year_counts = df_valid.groupby(['cpc_code', 'year']).size().reset_index(name='count')
years = sorted(cpc_year_counts['year'].unique())
print(f"Years: {years}")
print(f"Unique CPC codes: {cpc_year_counts['cpc_code'].nunique()}")

# Calculate EMA for each CPC code
alpha = 0.2
cpc_best_year_2022 = []

# Process in batches to avoid timeout
batch_size = 1000
unique_cpcs = cpc_year_counts['cpc_code'].unique()
total_cpcs = len(unique_cpcs)

print(f"Processing {total_cpcs} CPC codes...")

for i, cpc_code in enumerate(unique_cpcs):
    if i % batch_size == 0:
        print(f"Processed {i}/{total_cpcs}...")
    
    df_cpc = cpc_year_counts[cpc_year_counts['cpc_code'] == cpc_code].copy()
    df_cpc = df_cpc.sort_values('year')
    
    # Fill missing years with 0
    years_range = list(range(df_cpc['year'].min(), df_cpc['year'].max() + 1))
    df_filled = pd.DataFrame({'year': years_range})
    df_filled = df_filled.merge(df_cpc[['year', 'count']], on='year', how='left')
    df_filled['count'] = df_filled['count'].fillna(0)
    
    # Calculate EMA
    if len(df_filled) == 0:
        continue
        
    ema_values = []
    ema = df_filled['count'].iloc[0]
    ema_values.append(ema)
    
    for j in range(1, len(df_filled)):
        ema = alpha * df_filled['count'].iloc[j] + (1 - alpha) * ema
        ema_values.append(ema)
    
    df_filled['ema'] = ema_values
    
    # Find year with max EMA
    max_idx = df_filled['ema'].idxmax()
    max_year = df_filled.loc[max_idx, 'year']
    
    if max_year == 2022:
        cpc_best_year_2022.append(cpc_code)

print(f"CPC codes with best year 2022: {len(cpc_best_year_2022)}")

# Save result
result = json.dumps(cpc_best_year_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': 'file_storage/functions.execute_python:44.json', 'var_functions.execute_python:48': 'file_storage/functions.execute_python:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
