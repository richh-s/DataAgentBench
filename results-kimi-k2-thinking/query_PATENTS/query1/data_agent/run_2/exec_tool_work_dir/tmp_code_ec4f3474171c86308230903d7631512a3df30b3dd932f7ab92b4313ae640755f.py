code = """import json
import os
import pandas as pd
import re

# Access the filepath from storage
filepath = locals()['var_functions.query_db:26']

with open(filepath, 'r') as f:
    data = json.load(f)

print('Loaded', len(data), 'records')

records = []
years_seen = set()
for item in data:
    pub_date = item.get('publication_date', '')
    year_match = re.search(r'(\d{4})', pub_date)
    if year_match:
        year = int(year_match.group(1))
        years_seen.add(year)
        
        cpc_str = item.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
            for cpc_entry in cpc_list:
                code = cpc_entry.get('code', '')
                if code and '/' in code:
                    records.append({
                        'cpc_level5': code,
                        'year': year
                    })
        except:
            pass

print('Years:', sorted(years_seen))

df = pd.DataFrame(records)
print('Records:', len(records))
print('DF shape:', df.shape)

if not df.empty:
    counts = df.groupby(['cpc_level5', 'year']).size().reset_index(name='count')
    print('Counts:', len(counts))
    
    alpha = 0.2
    ema_results = []
    
    for code in counts['cpc_level5'].unique():
        group = counts[counts['cpc_level5'] == code].copy()
        if len(group) < 2:
            continue
        
        group = group.sort_values('year')
        ema = group.iloc[0]['count']
        
        for _, row in group.iterrows():
            ema = alpha * row['count'] + (1 - alpha) * ema
            ema_results.append({
                'cpc_level5': code,
                'year': row['year'],
                'ema': round(ema, 2),
                'count': row['count']
            })
    
    ema_df = pd.DataFrame(ema_results)
    
    best_years_idx = ema_df.groupby('cpc_level5')['ema'].idxmax()
    best_years = ema_df.loc[best_years_idx]
    
    best_2022 = best_years[best_years['year'] == 2022]
    
    print('Best 2022 count:', len(best_2022))
    
    if not best_2022.empty:
        codes = best_2022.sort_values('ema', ascending=False)['cpc_level5'].tolist()
        result = codes
    else:
        result = []
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'available_keys': ['var_functions.list_db:0', 'var_functions.query_db:2', '__builtins__', 'json']}, 'var_functions.execute_python:22': [], 'var_functions.query_db:24': [{'total_records': '277813'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
