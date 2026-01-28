code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_var = locals()['var_functions.query_db:26']
level5_var = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_var)) if isinstance(cpc_var, str) else cpc_var
level5_data = json.load(open(level5_var)) if isinstance(level5_var, str) else level5_var

level5_symbols = set([item['symbol'] for item in level5_data])

print('Data loaded:', len(cpc_data), 'patents,', len(level5_symbols), 'level-5 codes')

# Parse CPC records
cpc_records = []
year_range = set()
for i, row in enumerate(cpc_data):
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
    year = None
    if isinstance(pub_date, str) and len(pub_date) > 10:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            year_range.add(year)
        except:
            pass
    
    # Parse CPC codes
    if isinstance(cpc_str, str) and len(cpc_str) > 10:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '') if isinstance(item, dict) else ''
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    cpc_records.append({'code': level5_code, 'year': year})
        except:
            pass

print('Parsed records:', len(cpc_records))
print('Year range:', min(year_range) if year_range else 'None', 'to', max(year_range) if year_range else 'None')

# Create DataFrame and filter
if cpc_records:
    df = pd.DataFrame(cpc_records)
    df = df.dropna(subset=['year', 'code'])
    
    # Count filings per year per code
    counts = df.groupby(['year', 'code']).size().reset_index(name='count')
    
    # Only keep codes that are level-5
    counts = counts[counts['code'].isin(level5_symbols)]
    
    print('Filtered counts:', len(counts))
    print('Unique codes:', counts['code'].nunique())
    print('Year range in counts:', counts['year'].min(), 'to', counts['year'].max())
    
    # Calculate EMA for each code
    def calc_ema(group):
        return group.ewm(alpha=0.2, adjust=False).mean()
    
    results = []
    for code in level5_symbols:
        code_data = counts[counts['code'] == code].sort_values('year')
        if len(code_data) >= 3:  # Need at least 3 years for meaningful EMA
            code_data['ema'] = calc_ema(code_data['count'])
            max_idx = code_data['ema'].idxmax()
            best_year = int(code_data.loc[max_idx, 'year'])
            
            results.append({
                'code': code,
                'best_year': best_year,
                'years_available': len(code_data)
            })
    
    if results:
        results_df = pd.DataFrame(results)
        print('Total codes analyzed:', len(results_df))
        print('Year distribution of best years:')
        print(results_df['best_year'].value_counts().sort_index())
        
        best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()
    else:
        best_2022_codes = []
else:
    best_2022_codes = []

print('Codes with best year 2022:', len(best_2022_codes))
result_str = json.dumps(best_2022_codes)

print("__RESULT__:")
print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
