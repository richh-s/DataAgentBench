code = """import json
import pandas as pd
import re
from datetime import datetime

# Load CPC patent data
cpc_var = locals()['var_functions.query_db:66']
if isinstance(cpc_var, str) and '.json' in cpc_var:
    with open(cpc_var, 'r') as f:
        cpc_data = json.load(f)
else:
    cpc_data = cpc_var

# Load level-5 CPC codes
level5_var = locals()['var_functions.query_db:28']
if isinstance(level5_var, str) and '.json' in level5_var:
    with open(level5_var, 'r') as f:
        level5_data = json.load(f)
else:
    level5_data = level5_var

level5_symbols = set([item['symbol'] for item in level5_data])

print('Data loaded:', len(cpc_data), 'patents,', len(level5_symbols), 'level-5 codes')

# Parse CPC records
records = []
years_seen = set()
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            years_seen.add(year)
        except:
            pass
    
    cpc_str = row.get('cpc', '')
    if cpc_str:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    if level5_code in level5_symbols:
                        records.append({'code': level5_code, 'year': year})
        except:
            pass

print('Parsed records:', len(records))
print('Years found:', sorted(years_seen) if years_seen else 'None')

# Create DataFrame and count
df = pd.DataFrame(records)
print('DataFrame shape:', df.shape)

if len(df) > 0:
    print('Year range:', df['year'].min(), 'to', df['year'].max())
    print('Unique codes:', df['code'].nunique())
    
    counts = df.groupby(['year', 'code']).size().reset_index(name='count')
    print('Year-code combinations:', len(counts))
    
    # Debug: check 2022 data specifically
    df_2022 = counts[counts['year'] == 2022]
    print('\n2022 data points:', len(df_2022))
    if len(df_2022) > 0:
        print('Top codes in 2022:')
        print(df_2022.nlargest(5, 'count'))
    
    # Process each code
    results = []
    for code in level5_symbols:
        code_data = counts[counts['code'] == code].sort_values('year')
        if len(code_data) >= 2:
            year_min = int(code_data['year'].min())
            year_max = int(code_data['year'].max())
            year_range = list(range(year_min, year_max + 1))
            full_years = pd.DataFrame({'year': year_range})
            code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
            code_full = code_full.sort_values('year')
            
            code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
            best_year = int(code_full.loc[code_full['ema'].idxmax(), 'year'])
            
            results.append({'code': code, 'best_year': best_year})
    
    results_df = pd.DataFrame(results)
    print('\nTotal codes analyzed:', len(results_df))
    
    if len(results_df) > 0:
        print('Best year distribution:')
        print(results_df['best_year'].value_counts().sort_index())
        
        codes_2022 = results_df[results_df['best_year'] == 2022]['code'].tolist()
    else:
        codes_2022 = []
else:
    codes_2022 = []

print('\nCodes with best year 2022:', len(codes_2022))

result = json.dumps(codes_2022)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
