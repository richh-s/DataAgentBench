code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_var = locals()['var_functions.query_db:26']
level5_var = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_var)) if isinstance(cpc_var, str) else cpc_var
level5_data = json.load(open(level5_var)) if isinstance(level5_var, str) else level5_var

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse with more lenient criteria
cpc_records = []
for i, row in enumerate(cpc_data):
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
    year = None
    if isinstance(pub_date, str):
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
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
                    if level5_code in level5_symbols:
                        cpc_records.append({'code': level5_code, 'year': year})
        except:
            pass

# Create DataFrame
df = pd.DataFrame(cpc_records)
print('Total records:', len(df))
print('Year distribution:')
print(df['year'].value_counts().sort_index())

# Filter valid years
valid_years = [2018, 2019, 2020, 2021, 2022, 2023]
df_filtered = df[df['year'].isin(valid_years)]

# Count filings per year per code
counts = df_filtered.groupby(['year', 'code']).size().reset_index(name='count')

print('\nYear-code combinations:', len(counts))
print('Unique codes:', counts['code'].nunique())

# For each code, find the year with highest count (simpler approach)
max_years = counts.loc[counts.groupby('code')['count'].idxmax()]

print('\nYear distribution of peak filing years:')
print(max_years['year'].value_counts().sort_index())

# Which codes peaked in 2022?
codes_2022 = max_years[max_years['year'] == 2022]['code'].tolist()
print(f'\nCodes with peak in 2022: {len(codes_2022)}')

# Return these codes
result_str = json.dumps(codes_2022)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': []}

exec(code, env_args)
