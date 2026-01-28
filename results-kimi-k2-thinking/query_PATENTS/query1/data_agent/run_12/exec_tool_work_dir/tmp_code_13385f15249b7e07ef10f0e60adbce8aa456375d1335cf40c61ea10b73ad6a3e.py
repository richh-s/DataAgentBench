code = """import json
import pandas as pd
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print('Level 5 symbols (first 20):', sorted(list(level5_symbols))[:20])

# Load all publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

print('Processing', len(publication_data), 'records')

# Extract all unique CPC codes and their structures
all_main_groups = set()
all_subclass_groups = set()

for record in publication_data:
    cpc_str = record.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    for code in codes:
        # Split by / to get main part
        main_part = code.split('/')[0]
        all_main_groups.add(main_part)
        
        # Split by . to get subclass
        if '.' in main_part:
            subclass = main_part.split('.')[0]
            all_subclass_groups.add(subclass)

print('Unique main groups (first 20):', sorted(list(all_main_groups))[:20])
print('Unique subclass groups (first 20):', sorted(list(all_subclass_groups))[:20])

# Check if any subclass groups match level 5 symbols exactly
exact_matches = all_subclass_groups.intersection(level5_symbols)
print('Exact matches between subclass groups and level 5 symbols:', len(exact_matches))
print('Sample exact matches:', sorted(list(exact_matches))[:20])

# If no exact matches, check if level 5 symbols are prefixes of subclass groups
prefix_matches = []
for level5 in sorted(list(level5_symbols))[:100]:  # Sample first 100
    for subclass in sorted(list(all_subclass_groups)):
        if subclass.startswith(level5):
            prefix_matches.append((level5, subclass))

print('Prefix matches found:', len(prefix_matches))
print('Sample prefix matches:', prefix_matches[:10])

# Now let's process all records using prefix matching
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
        main_part = code.split('/')[0]
        if '.' in main_part:
            subclass = main_part.split('.')[0]
            # Check if this subclass starts with any level 5 symbol
            for level5 in level5_symbols:
                if subclass.startswith(level5):
                    cpc_years.append({'cpc_group': level5, 'year': year})

print('CPC-year pairs extracted:', len(cpc_years))

# Create DataFrame and continue with analysis
if cpc_years:
    df = pd.DataFrame(cpc_years)
    print('DataFrame shape:', df.shape)
    print('Unique CPC groups:', df['cpc_group'].nunique())
    
    # Get yearly counts
    yearly_counts = df.groupby(['cpc_group', 'year']).size().reset_index(name='count')
    print('Yearly counts rows:', len(yearly_counts))
    
    # Calculate EMA for each group
    results = []
    alpha = 0.2
    
    for cpc_group in yearly_counts['cpc_group'].unique():
        group_data = yearly_counts[yearly_counts['cpc_group'] == cpc_group].copy()
        group_data = group_data.sort_values('year')
        
        if len(group_data) > 0:
            ema = float(group_data.iloc[0]['count'])
            for i in range(1, len(group_data)):
                current = float(group_data.iloc[i]['count'])
                ema = alpha * current + (1 - alpha) * ema
            
            # Track year with max EMA
            max_ema = ema
            best_year = int(group_data.iloc[-1]['year'])
            
            # Actually need to track all EMA values to find max
            ema_values = [float(group_data.iloc[0]['count'])]
            for i in range(1, len(group_data)):
                current = float(group_data.iloc[i]['count'])
                ema = alpha * current + (1 - alpha) * ema_values[-1]
                ema_values.append(ema)
            
            max_idx = ema_values.index(max(ema_values))
            best_year = int(group_data.iloc[max_idx]['year'])
            
            results.append({'cpc_group': cpc_group, 'best_year': best_year})
    
    results_df = pd.DataFrame(results)
    best_2022 = results_df[results_df['best_year'] == 2022]
    final_groups = best_2022['cpc_group'].tolist()
    
    print('Groups with best year 2022:', len(final_groups))
    print('Sample results:', final_groups[:10])
else:
    final_groups = []
    print('No data extracted')

print('__RESULT__:')
print(json.dumps(final_groups))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}, 'var_functions.execute_python:54': []}

exec(code, env_args)
