code = """import json
import pandas as pd
import re

# Load publication data from the correct storage key
data_file = var_functions.query_db_48
print("Data file path:", data_file)

with open(data_file, 'r') as f:
    pub_data = json.load(f)

print("Total records loaded:", len(pub_data))

# Extract CPC codes and years
records = []
for item in pub_data:
    try:
        cpc_json = item['cpc']
        pub_date = item['publication_date']
        
        # Extract year
        year_match = re.search(r'(\d{4})', pub_date)
        if year_match:
            year = int(year_match.group(1))
            
            # Parse CPC codes
            cpc_list = json.loads(cpc_json)
            for entry in cpc_list:
                code = entry.get('code', '')
                if len(code) >= 5:
                    group_5 = code[:5]  # Level 5 group code
                    records.append({
                        'year': year,
                        'cpc_group_5': group_5
                    })
    except:
        continue

print("Extracted records:", len(records))

# Create DataFrame and count filings
df = pd.DataFrame(records)
years = sorted(df['year'].unique())
print("Year range:", years[0], "to", years[-1])
print("Unique groups:", df['cpc_group_5'].nunique())

# Group by year and CPC group
yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')

# Calculate EMA for each group
groups = yearly_counts['cpc_group_5'].unique()
print("Total groups to analyze:", len(groups))

results = []
for group in groups:
    group_data = yearly_counts[yearly_counts['cpc_group_5'] == group].copy()
    group_data = group_data.sort_values('year')
    
    # Calculate EMA with alpha=0.2
    ema = None
    alpha = 0.2
    best_ema = 0
    best_year = None
    
    for _, row in group_data.iterrows():
        count = row['count']
        year = row['year']
        
        if ema is None:
            ema = count
        else:
            ema = alpha * count + (1 - alpha) * ema
        
        # Track best year
        if ema > best_ema:
            best_ema = ema
            best_year = year
    
    if best_year is not None:
        results.append({
            'cpc_group_5': group,
            'best_year': int(best_year),
            'best_ema': float(best_ema)
        })

results_df = pd.DataFrame(results)

# Filter for groups whose best year is 2022
best_2022 = results_df[results_df['best_year'] == 2022]
final_codes = sorted(best_2022['cpc_group_5'].tolist())

print("Groups with best year 2022:", len(final_codes))
print("First 20 codes:", final_codes[:20])

result = {
    'total_groups': len(groups),
    'best_in_2022': len(final_codes),
    'cpc_codes': final_codes
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:51': []}

exec(code, env_args)
