code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC data
cpc_path = locals()['var_functions.query_db:66']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

print('Loading complete:', len(cpc_data), 'patents,', len(level5_symbols), 'level-5 codes')

# Simple approach: extract year and level-5 code
cpc_by_year = {}
years_found = set()
for row in cpc_data[:10000]:  # Sample for speed
    pub_date = row.get('publication_date', '')
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            years_found.add(year)
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
                        cpc_by_year[(year, level5_code)] = cpc_by_year.get((year, level5_code), 0) + 1
        except:
            pass

print('Years found:', sorted(years_found) if years_found else 'None')
print('Sample data points:', len(cpc_by_year))

# Create DataFrame
df = pd.DataFrame([{'year': k[0], 'code': k[1], 'count': v} for k, v in cpc_by_year.items()])

if len(df) > 0:
    print('DataFrame shape:', df.shape)
    print('Year range:', df['year'].min(), 'to', df['year'].max())
    print('Unique codes:', df['code'].nunique())
    print('\nYear distribution:')
    print(df.groupby('year')['count'].sum().sort_index())
    
    # Check if 2022 exists
    df_2022 = df[df['year'] == 2022]
    print(f'\nRecords in 2022: {len(df_2022)}')
    
    if len(df_2022) > 0:
        print('Top codes in 2022:')
        print(df_2022.nlargest(10, 'count'))
    else:
        print('No data for 2022 found')
else:
    print('No data parsed')

result = json.dumps([])
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
