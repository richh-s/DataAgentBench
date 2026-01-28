code = """import json
import pandas as pd
from datetime import datetime

# Get the processed data from previous step
result_key = 'var_functions.execute_python:16'
result_summary = locals()[result_key]

# We need to reconstruct the DataFrame from the summary information
# Actually, let's reload and reprocess more efficiently
result_key = 'var_functions.query_db:6'
result_file = locals()[result_key]

if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        publications = json.load(f)
else:
    publications = result_file

print('Reprocessing data for EMA calculation...')

# Parse CPC codes and extract years
cpc_year_data = []
for pub in publications:
    cpc_str = pub.get('cpc', '')
    pub_date_str = pub.get('publication_date', '')
    
    if not cpc_str or not pub_date_str:
        continue
    
    # Extract year from publication date
    year_match = re.search(r',\s*(\d{4})', pub_date_str)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    # Parse CPC JSON string
    try:
        cleaned_cpc = cpc_str.strip()
        if cleaned_cpc.startswith('['):
            cpc_list = json.loads(cleaned_cpc)
        else:
            continue
    except:
        continue
    
    if not isinstance(cpc_list, list):
        continue
    
    for cpc_item in cpc_list:
        if isinstance(cpc_item, dict) and 'code' in cpc_item:
            code = cpc_item['code']
            # Extract group (first part before /)
            if '/' in code:
                group = code.split('/')[0]
            else:
                group = code
            
            cpc_year_data.append({
                'full_code': code,
                'group_code': group,
                'year': year
            })

# Convert to DataFrame
df = pd.DataFrame(cpc_year_data)

# Get CPC level 5 symbols from CPCDefinition_database
cpc_level5_key = 'var_functions.query_db:5'
cpc_level5_data = locals()[cpc_level5_key]
cpc_level5_symbols = [item['symbol'] for item in cpc_level5_data]

print('Total CPC level 5 symbols found: ' + str(len(cpc_level5_symbols)))
print('Sample level 5 symbols: ' + str(cpc_level5_symbols[:10]))

# Filter our data to only include CPC groups that are at level 5
df_level5 = df[df['group_code'].isin(cpc_level5_symbols)].copy()

print('Level 5 entries found: ' + str(len(df_level5)))
print('Unique level 5 groups: ' + str(len(df_level5['group_code'].unique())))

if len(df_level5) == 0:
    print('No Level 5 CPC data found - checking data sample:')
    print('Sample group codes from data: ' + str(df['group_code'].unique()[:20]))
    print('Sample level 5 symbols: ' + str(cpc_level5_symbols[:20]))
    # Check for matches
    matches = set(df['group_code'].unique()) & set(cpc_level5_symbols)
    print('Matching symbols: ' + str(list(matches)[:20]))
    print('Match count: ' + str(len(matches)))

# Store basic info
basic_info = {
    'total_level5_entries': len(df_level5),
    'unique_level5_groups': len(df_level5['group_code'].unique()) if len(df_level5) > 0 else 0,
    'year_range': str(df_level5['year'].min()) + ' to ' + str(df_level5['year'].max()) if len(df_level5) > 0 else 'No data',
    'years_available': sorted(df_level5['year'].unique()) if len(df_level5) > 0 else []
}

print('__RESULT__:')
print(json.dumps(basic_info))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'total_publications': 277813, 'cpc_entries': 1333969, 'dataframe_shape': [1333969, 5], 'columns': ['full_code', 'group_code', 'year', 'inventive', 'first']}}

exec(code, env_args)
