code = """import json
import pandas as pd
from datetime import datetime
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print('Level 5 symbols count:', len(level5_symbols))

# Load all publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

print('Total records:', len(publication_data))

# Process records and debug
cpc_years = []
records_with_codes = 0
records_with_matches = 0

for i, record in enumerate(publication_data):
    # Extract year
    filing_date = record.get('filing_date', '')
    year_match = re.search(r'(\d{4})', str(filing_date))
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    records_with_codes += 1
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    
    for code in codes:
        main_group = code.split('/')[0].split()[0]
        if main_group in level5_symbols:
            cpc_years.append({'cpc_group': main_group, 'year': year})
            records_with_matches += 1

print(f'Records with CPC codes: {records_with_codes}')
print(f'Records with level 5 matches: {records_with_matches}')
print(f'Total CPC-year pairs: {len(cpc_years)}')

# Create DataFrame
if cpc_years:
    df = pd.DataFrame(cpc_years)
    print('DataFrame created, shape:', df.shape)
    print('Columns:', df.columns.tolist())
    print('Sample data:', df.head())
    
    # Check unique CPC groups
    unique_groups = df['cpc_group'].unique()
    print('Unique CPC groups found:', len(unique_groups))
    print('Sample groups:', unique_groups[:10])
    
    # Get yearly counts
    yearly_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
    print('Yearly counts shape:', yearly_counts.shape)
    
    # Calculate EMA
    results = []
    alpha = 0.2
    
    for cpc_group in yearly_counts['cpc_group'].unique():
        group_data = yearly_counts[yearly_counts['cpc_group'] == cpc_group].copy()
        group_data = group_data.sort_values('year')
        
        # Calculate EMA
        ema_values = []
        if len(group_data) > 0:
            ema = float(group_data.iloc[0]['count'])
            ema_values.append(ema)
            
            for i in range(1, len(group_data)):
                current_count = float(group_data.iloc[i]['count'])
                ema = alpha * current_count + (1 - alpha) * ema
                ema_values.append(ema)
        
        group_data['ema'] = ema_values
        max_ema_idx = group_data['ema'].idxmax()
        best_year = int(group_data.loc[max_ema_idx, 'year'])
        
        results.append({'cpc_group': cpc_group, 'best_year': best_year})
    
    results_df = pd.DataFrame(results)
    best_2022 = results_df[results_df['best_year'] == 2022]
    
    final_cpc_groups = best_2022['cpc_group'].tolist()
    print('Final result - CPC groups with best year 2022:', len(final_cpc_groups))
    print('Sample results:', final_cpc_groups[:10])
else:
    print('No CPC data extracted')
    final_cpc_groups = []

print('__RESULT__:')
print(json.dumps(final_cpc_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}}

exec(code, env_args)
