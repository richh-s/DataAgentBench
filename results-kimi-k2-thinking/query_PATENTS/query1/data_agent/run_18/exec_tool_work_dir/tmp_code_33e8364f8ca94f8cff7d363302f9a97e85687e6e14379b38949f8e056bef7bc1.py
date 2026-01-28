code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data from the stored file paths
# CPC Level 5 data
cpc_level5_file = var_functions_query_db__12
cpc_level5_data = json.load(open(cpc_level5_file))
level5_symbols = set(item['symbol'] for item in cpc_level5_data)

# Publication data
publication_file = var_functions_query_db__10
publication_data = json.load(open(publication_file))

print(f"Processing {len(publication_data)} publications with {len(cpc_level5_data)} CPC level 5 symbols")

# Process publication data to extract CPC codes and years
patent_counts = {}

for record in publication_data:
    # Extract year from publication date
    pub_date = record.get('publication_date', '')
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
    else:
        continue
    
    if year < 2000 or year > 2023:
        continue
    
    # Parse CPC codes
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str) if isinstance(cpc_str, str) else cpc_str
    except:
        continue
    
    for cpc_item in cpc_list:
        code = cpc_item.get('code', '')
        # For level 5, we need the exact symbol match
        # CPC symbols can look like: A41D, A41D1/00, A41D1/02, etc.
        # Level 5 is the group level (4 characters like A41D)
        group_code = code[:4] if len(code) >= 4 else code
        
        if group_code in level5_symbols:
            key = (group_code, year)
            patent_counts[key] = patent_counts.get(key, 0) + 1

print(f"Found {len(patent_counts)} CPC group-year combinations")

# Create DataFrame with counts
if patent_counts:
    df_counts = pd.DataFrame([(k[0], k[1], v) for k, v in patent_counts.items()], 
                             columns=['cpc_group', 'year', 'count'])
    
    # Pivot to have years as columns
    df_pivot = df_counts.pivot(index='cpc_group', columns='year', values='count').fillna(0)
    
    # Calculate exponential moving average for each CPC group
    alpha = 0.2
    ema_results = []
    
    for cpc_group in df_pivot.index:
        # Get sorted years and values
        years = sorted(df_pivot.columns)
        values = [df_pivot.loc[cpc_group, year] for year in years]
        
        # Calculate EMA
        ema_values = []
        ema_prev = values[0] if values else 0
        
        for i, val in enumerate(values):
            if i == 0:
                ema = val
            else:
                ema = alpha * val + (1 - alpha) * ema_prev
            ema_values.append(ema)
            ema_prev = ema
        
        # Find year with highest EMA
        max_ema = max(ema_values)
        best_year = years[ema_values.index(max_ema)]
        
        ema_results.append({
            'cpc_group': cpc_group,
            'best_year': best_year,
            'max_ema': max_ema
        })
    
    df_ema = pd.DataFrame(ema_results)
    
    # Filter for best_year = 2022
    result_2022 = df_ema[df_ema['best_year'] == 2022]['cpc_group'].tolist()
    
    # Get top 20 for context
    df_ema_sorted = df_ema.sort_values('max_ema', ascending=False)
    top_groups = df_ema_sorted.head(20)
    
    output = {
        'total_level5_groups': len(cpc_level5_data),
        'groups_with_data': len(df_pivot),
        'groups_best_year_2022': result_2022,
        'count_best_year_2022': len(result_2022),
        'top_groups_all_years': top_groups.to_dict('records')
    }
else:
    output = {
        'total_level5_groups': len(cpc_level5_data),
        'groups_with_data': 0,
        'groups_best_year_2022': [],
        'count_best_year_2022': 0,
        'top_groups_all_years': []
    }

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.list_db:1': ['cpc_definition'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'total_records': '277813'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
