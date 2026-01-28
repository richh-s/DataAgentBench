code = """import json
import pandas as pd
import re
from datetime import datetime

# Access the data file from the storage
pub_data_file = var_functions.query_db_48
print("Loading publication data from:", pub_data_file)

# Load the publication data
with open(pub_data_file, 'r') as f:
    pub_data = json.load(f)

print("Total publication records:", len(pub_data))

# Extract CPC codes and publication years
records = []
for item in pub_data:
    try:
        cpc_json = item['cpc']
        pub_date = item['publication_date']
        
        # Extract year from date string
        year_match = re.search(r'(\d{4})', pub_date)
        if not year_match:
            continue
        year = int(year_match.group(1))
        
        # Parse CPC JSON
        cpc_list = json.loads(cpc_json)
        
        for cpc_entry in cpc_list:
            code = cpc_entry.get('code', '')
            if len(code) >= 5:
                # Get level 5 group (first 5 characters)
                group_5 = code[:5]
                records.append({
                    'year': year,
                    'cpc_code': code,
                    'cpc_group_5': group_5
                })
    except Exception as e:
        continue

print("Parsed records:", len(records))

# Create DataFrame
df = pd.DataFrame(records)
print("Year range:", df['year'].min(), "to", df['year'].max())
print("Unique level 5 groups:", df['cpc_group_5'].nunique())

# Count filings per year for each group
yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')
print("Yearly counts shape:", yearly_counts.shape)
print("Available years:", sorted(yearly_counts['year'].unique()))

# Now calculate EMA for each group
groups = yearly_counts['cpc_group_5'].unique()
results = []

for group in groups:
    group_data = yearly_counts[yearly_counts['cpc_group_5'] == group].copy()
    group_data = group_data.sort_values('year')
    
    # Initialize EMA
    ema_values = []
    ema = None
    alpha = 0.2
    
    for _, row in group_data.iterrows():
        count = row['count']
        if ema is None:
            ema = count  # First value
        else:
            ema = alpha * count + (1 - alpha) * ema
        ema_values.append(ema)
    
    group_data['ema'] = ema_values
    
    # Find year with highest EMA
    best_idx = group_data['ema'].idxmax()
    best_year = group_data.loc[best_idx, 'year']
    best_ema = group_data.loc[best_idx, 'ema']
    
    results.append({
        'cpc_group_5': group,
        'best_year': int(best_year),
        'best_ema': float(best_ema),
        'total_years': len(group_data)
    })

results_df = pd.DataFrame(results)
print("Total groups analyzed:", len(results_df))

# Filter groups where best year is 2022
best_in_2022 = results_df[results_df['best_year'] == 2022]
print("Groups with best year 2022:", len(best_in_2022))

# Get CPC group codes (already have them as cpc_group_5)
final_codes = best_in_2022['cpc_group_5'].tolist()

# Save results
output = {
    'total_groups_analyzed': len(results_df),
    'groups_best_2022': len(best_in_2022),
    'cpc_codes_2022': sorted(final_codes)
}

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
