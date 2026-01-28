code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC patent data and level-5 codes
cpc_data = json.load(open(locals()['var_functions.query_db:66']))
level5_data = json.load(open(locals()['var_functions.query_db:28']))

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC records by year and code
cpc_by_year = {}
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    try:
        clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
        date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
        year = date_obj.year
    except:
        continue
    
    cpc_str = row.get('cpc', '')
    try:
        codes = json.loads(cpc_str)
        for item in codes:
            code = item.get('code', '')
            if code and len(code) >= 4:
                level5_code = code[:4]
                if level5_code in level5_symbols:
                    key = (year, level5_code)
                    cpc_by_year[key] = cpc_by_year.get(key, 0) + 1
    except:
        pass

# Create DataFrame
df = pd.DataFrame([{'year': k[0], 'code': k[1], 'count': v} for k, v in cpc_by_year.items()])

# Calculate EMA for each code and find best year
codes_2022 = []
for code in level5_symbols:
    code_data = df[df['code'] == code].sort_values('year')
    if len(code_data) >= 3:
        year_min, year_max = int(code_data['year'].min()), int(code_data['year'].max())
        year_range = list(range(year_min, year_max + 1))
        
        full_years = pd.DataFrame({'year': year_range})
        code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
        code_full = code_full.sort_values('year')
        code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
        
        best_year = int(code_full.loc[code_full['ema'].idxmax(), 'year'])
        
        if best_year == 2022:
            codes_2022.append(code)

# Return as JSON
result = json.dumps(codes_2022)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
