code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC patent data
cpc_path = locals()['var_functions.query_db:50']
cpc_raw = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path

# Load level-5 CPC codes
level5_path = locals()['var_functions.query_db:28']
level5_raw = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_raw])

# Parse CPC codes and years
cpc_records = []
for row in cpc_raw:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
    year = None
    if pub_date and isinstance(pub_date, str):
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            pass
    
    # Parse CPC codes
    if cpc_str and isinstance(cpc_str, str) and len(cpc_str) > 10:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                if isinstance(item, dict):
                    code = item.get('code', '')
                    if code and len(code) >= 4:
                        level5_code = code[0:4]
                        if level5_code in level5_symbols:
                            cpc_records.append({'code': level5_code, 'year': year})
        except:
            pass

# Create DataFrame
df = pd.DataFrame(cpc_records)
print('Parsed', len(df), 'records')

# Count filings per year per code
counts = df.groupby(['year', 'code']).size().reset_index(name='count')

# Calculate EMA for each code
results = []
for code in level5_symbols:
    code_data = counts[counts['code'] == code].copy()
    if len(code_data) >= 3:
        year_range = range(int(code_data['year'].min()), int(code_data['year'].max()) + 1)
        full_years = pd.DataFrame({'year': list(year_range)})
        code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
        code_full = code_full.sort_values('year')
        code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
        
        max_idx = code_full['ema'].idxmax()
        best_year = int(code_full.loc[max_idx, 'year'])
        
        results.append({'code': code, 'best_year': best_year})

results_df = pd.DataFrame(results)
best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()

print('Found', len(best_2022_codes), 'codes with best year 2022')

result_str = json.dumps(best_2022_codes)
print('__RESULT__:', result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
