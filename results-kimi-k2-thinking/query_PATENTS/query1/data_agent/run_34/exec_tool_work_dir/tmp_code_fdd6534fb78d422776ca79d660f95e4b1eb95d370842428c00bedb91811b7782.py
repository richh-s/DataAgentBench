code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC patent data and level-5 codes
cpc_data = json.load(open(locals()['var_functions.query_db:66']))
level5_data = json.load(open(locals()['var_functions.query_db:28']))

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC records
cpc_records = []
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    try:
        clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
        date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
        year = date_obj.year
    except:
        pass
    
    cpc_str = row.get('cpc', '')
    try:
        codes = json.loads(cpc_str)
        for item in codes:
            code = item.get('code', '')
            if code and len(code) >= 4:
                level5_code = code[:4]
                if level5_code in level5_symbols:
                    cpc_records.append({'code': level5_code, 'year': year})
    except:
        pass

# Create DataFrame and count filings
df = pd.DataFrame(cpc_records)
counts = df.groupby(['year', 'code']).size().reset_index(name='count')

# Analyze best years for each code
best_years = []
for code in counts['code'].unique():
    code_data = counts[counts['code'] == code].sort_values('year')
    if len(code_data) >= 2:
        year_range = range(int(code_data['year'].min()), int(code_data['year'].max()) + 1)
        full_years = pd.DataFrame({'year': list(year_range)})
        code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
        code_full = code_full.sort_values('year')
        code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
        
        best_year = int(code_full.loc[code_full['ema'].idxmax(), 'year'])
        best_ema = float(code_full.loc[code_full['ema'].idxmax(), 'ema'])
        
        best_years.append({'code': code, 'best_year': best_year, 'best_ema': best_ema})

# Create DataFrame of results
results_df = pd.DataFrame(best_years)

print('=== ANALYSIS RESULTS ===')
print(f'Total level-5 codes analyzed: {len(results_df)}')

if len(results_df) > 0:
    print('\n=== DISTRIBUTION OF BEST YEARS ===')
    year_distribution = results_df['best_year'].value_counts().sort_index()
    print(year_distribution)
    
    print('\n=== CODES WITH BEST YEAR 2022 ===')
    codes_2022 = results_df[results_df['best_year'] == 2022]
    print(f'Count: {len(codes_2022)}')
    if len(codes_2022) > 0:
        print('Sample codes:')
        print(codes_2022.head())
    
    result_codes = codes_2022['code'].tolist()
else:
    print('No data to analyze')
    result_codes = []

result = json.dumps(result_codes)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
