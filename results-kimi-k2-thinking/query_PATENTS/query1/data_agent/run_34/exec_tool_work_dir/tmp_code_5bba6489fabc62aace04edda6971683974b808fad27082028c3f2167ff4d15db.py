code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC patent data and level-5 codes
cpc_data = json.load(open(locals()['var_functions.query_db:50'])) if isinstance(locals()['var_functions.query_db:50'], str) else locals()['var_functions.query_db:50']
level5_data = json.load(open(locals()['var_functions.query_db:28'])) if isinstance(locals()['var_functions.query_db:28'], str) else locals()['var_functions.query_db:28']

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC codes and publication years
cpc_records = []
for row in cpc_data:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year from date string
    year = None
    if pub_date and isinstance(pub_date, str):
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            pass
    
    # Parse CPC codes from JSON string
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
        except:
            pass

# Create DataFrame and analyze
df = pd.DataFrame(cpc_records)
counts = df.groupby(['year', 'code']).size().reset_index(name='count')

# Find the year with maximum filings for each code
max_years = counts.loc[counts.groupby('code')['count'].idxmax()]
codes_2022 = max_years[max_years['year'] == 2022]['code'].tolist()

# Return as JSON
result = json.dumps(codes_2022)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
