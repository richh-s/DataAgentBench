code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_var = locals()['var_functions.query_db:50']
level5_var = locals()['var_functions.query_db:28']

cpc_raw = json.load(open(cpc_var)) if isinstance(cpc_var, str) and '.json' in cpc_var else cpc_var
level5_raw = json.load(open(level5_var)) if isinstance(level5_var, str) and '.json' in level5_var else level5_raw

level5_symbols = set([item['symbol'] for item in level5_raw])

# Debug - check sample data
if cpc_raw:
    print('Sample patent record:')
    print(json.dumps(cpc_raw[0])[:200])

# Parse CPC records
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
                        level5_code = code[:4]
                        if level5_code in level5_symbols:
                            cpc_records.append({'code': level5_code, 'year': year})
        except Exception as e:
            pass

# Create DataFrame
print(f'Parsed {len(cpc_records)} records')

df = pd.DataFrame(cpc_records)
print(f'DataFrame shape: {df.shape}')
print(f'Year range: {df["year"].min()} to {df["year"].max()}')

# Filter and count
counts = df.groupby(['year', 'code']).size().reset_index(name='count')
print(f'Year-code combinations: {len(counts)}')
print(f'Unique codes: {counts["code"].nunique()}')

# Simple approach: For each code, find year with max count
max_years = counts.loc[counts.groupby('code')['count'].idxmax()]
print(f'Found peak years for {len(max_years)} codes')
print('Year distribution:')
print(max_years['year'].value_counts().sort_index())

# Get codes that peaked in 2022
codes_2022 = max_years[max_years['year'] == 2022]['code'].tolist()
print(f'\nCodes with peak in 2022: {len(codes_2022)}')

result = json.dumps(codes_2022)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
