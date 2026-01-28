code = """import json
import pandas as pd
import re

# Access the correct variable name with colon
key = "var_functions.query_db:48"

if key in globals():
    pub_file = globals()[key]
    print("Success! Found file:", pub_file)
    
    # Load the data
    with open(pub_file, 'r') as f:
        pub_data = json.load(f)
    
    print("Loaded", len(pub_data), "publication records")
    
    # Process to extract CPC codes and years
    records = []
    for item in pub_data:
        try:
            cpc_json = item.get('cpc', '[]')
            pub_date = item.get('publication_date', '')
            
            year_match = re.search(r'(\d{4})', pub_date)
            if year_match:
                year = int(year_match.group(1))
                
                cpc_list = json.loads(cpc_json)
                for entry in cpc_list:
                    code = entry.get('code', '')
                    if len(code) >= 5:
                        group_5 = code[:5]
                        records.append({
                            'year': year,
                            'cpc_group_5': group_5
                        })
        except:
            continue
    
    # Create dataframe
    df = pd.DataFrame(records)
    print("Extracted", len(df), "CPC records")
    print("Year range:", df['year'].min(), "to", df['year'].max())
    print("Unique level-5 groups:", df['cpc_group_5'].nunique())
    
    # Count filings per year per group
    yearly_counts = df.groupby(['year', 'cpc_group_5']).size().reset_index(name='count')
    
    # Calculate EMA for each group
    groups = yearly_counts['cpc_group_5'].unique()
    results = []
    alpha = 0.2
    
    for group in groups:
        group_data = yearly_counts[yearly_counts['cpc_group_5'] == group].copy()
        group_data = group_data.sort_values('year')
        
        ema = None
        best_year = None
        best_ema = -1
        
        for _, row in group_data.iterrows():
            count = row['count']
            year = row['year']
            
            if ema is None:
                ema = count
            else:
                ema = alpha * count + (1 - alpha) * ema
            
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
    
    # Filter for groups with best year 2022
    best_2022 = results_df[results_df['best_year'] == 2022]
    final_codes = sorted(best_2022['cpc_group_5'].tolist())
    
    print("Groups with best year 2022:", len(final_codes))
    
    result = {
        'total_technology_areas': len(groups),
        'areas_best_year_2022': len(final_codes),
        'cpc_group_codes': final_codes
    }
else:
    result = {'error': 'Key not found', 'attempted_key': key}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'has_pub_data': False, 'has_cpc_symbols': False, 'pub_records_count': 0, 'cpc_symbols_count': 0}, 'var_functions.execute_python:38': {'pub_records': 0, 'cpc_symbols': 0, 'sample_pub': None, 'sample_cpc': None}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:51': [], 'var_functions.execute_python:58': {'error': 'File not found', 'available_keys': ['var_functions.query_db:10', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:24', 'var_functions.query_db:48', 'var_functions.query_db:5', 'var_functions.query_db:51', 'var_functions.query_db:6']}}

exec(code, env_args)
