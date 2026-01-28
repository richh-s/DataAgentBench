code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC data
cpc_path = var_functions.query_db_26
cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path

# Load level 5 codes
level5_path = var_functions.query_db_28
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path
level5_symbols = [item['symbol'] for item in level5_data]

print('Records:', len(cpc_data), 'Level-5 codes:', len(level5_symbols))

# Parse data
cpc_records = []
for row in cpc_data:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            pass
    
    # Parse CPC codes
    if cpc_str and cpc_str != '[]':
        try:
            codes_list = json.loads(cpc_str)
            for item in codes_list:
                code = item.get('code', '')
                if code:
                    cpc_records.append({'code': code, 'year': year})
        except:
            pass

# Create DataFrame
df = pd.DataFrame(cpc_records)
if df.empty:
    print('No data parsed')
else:
    # Extract level 5 group codes
df['level5'] = df['code'].apply(lambda x: x.split('/')[0][:4] if pd.notna(x) and '/' in x else (x[:4] if pd.notna(x) else None))
    level5_df = df[df['level5'].isin(level5_symbols)]
    
    # Count by year and code
    counts = level5_df.groupby(['year', 'level5']).size().reset_index(name='count')
    
    # Calculate EMA
    def calc_ema(group, alpha=0.2):
        return group.ewm(alpha=alpha, adjust=False).mean()
    
    results = []
    for code in level5_symbols:
        code_data = counts[counts['level5'] == code].sort_values('year')
        if not code_data.empty:
            code_data['ema'] = calc_ema(code_data['count'])
            best_idx = code_data['ema'].idxmax()
            best_row = code_data.loc[best_idx]
            results.append({
                'code': code,
                'best_year': int(best_row['year']),
                'best_ema': float(best_row['ema'])
            })
    
    results_df = pd.DataFrame(results)
    best_2022 = results_df[results_df['best_year'] == 2022]['code'].tolist()
    
    print('Codes with best year 2022:', len(best_2022))
    
    result_str = json.dumps(best_2022)
    print('__RESULT__:')
    print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
