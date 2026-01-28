code = """import json
import pandas as pd
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)

# Load all publication data  
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

# Build dataset of CPC groups at level 5
cpc_years = []
for record in publication_data:
    filing_date = record.get('filing_date', '')
    year_match = re.search(r'(\d{4})', str(filing_date))
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    cpc_str = record.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    
    for code in codes:
        # Extract first 4 characters as potential level 5 symbol
        main_part = code.split('/')[0].replace(' ', '')
        if len(main_part) >= 4:
            potential_level5 = main_part[:4]
            if potential_level5 in level5_symbols:
                cpc_years.append({'cpc_group': potential_level5, 'year': year})

# Analyze data
if cpc_years:
    df = pd.DataFrame(cpc_years)
    
    # Get yearly counts
    yearly_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
    
    # Calculate EMA for each CPC group
    results = []
    alpha = 0.2
    
    for cpc_group in yearly_counts['cpc_group'].unique():
        group_data = yearly_counts[yearly_counts['cpc_group'] == cpc_group].copy()
        group_data = group_data.sort_values('year')
        
        if len(group_data) > 0:
            # Calculate EMA values
            ema_values = [float(group_data.iloc[0]['count'])]
            
            for i in range(1, len(group_data)):
                current_count = float(group_data.iloc[i]['count'])
                ema = alpha * current_count + (1 - alpha) * ema_values[-1]
                ema_values.append(ema)
            
            # Find year with maximum EMA
            max_idx = ema_values.index(max(ema_values))
            best_year = int(group_data.iloc[max_idx]['year'])
            
            results.append({'cpc_group': cpc_group, 'best_year': best_year})
    
    results_df = pd.DataFrame(results)
    
    # Filter for best year 2022
    best_2022 = results_df[results_df['best_year'] == 2022]
    final_cpc_groups = sorted(best_2022['cpc_group'].tolist())
else:
    final_cpc_groups = []

print('__RESULT__:')
print(json.dumps(final_cpc_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}, 'var_functions.execute_python:54': [], 'var_functions.execute_python:58': []}

exec(code, env_args)
