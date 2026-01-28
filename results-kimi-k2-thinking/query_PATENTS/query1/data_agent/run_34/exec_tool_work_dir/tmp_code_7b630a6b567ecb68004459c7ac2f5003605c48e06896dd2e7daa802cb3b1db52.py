code = """import json, pandas as pd, re
from datetime import datetime

# Load data using correct variable access
cpc_path = locals()['var_functions.query_db:26']
level5_path = locals()['var_functions.query_db:28']

# Read JSON data
cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC and year data
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
    if cpc_str:
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

# Create DataFrame and analyze
df = pd.DataFrame(cpc_records)

if len(df) > 0:
    # Count filings per year per code
    counts = df.groupby(['year', 'code']).size().reset_index(name='count')
    
    # Calculate EMA for each code
    def calc_ema(group):
        return group.ewm(alpha=0.2, adjust=False).mean()
    
    results = []
    for code in level5_symbols:
        code_data = counts[counts['code'] == code].sort_values('year')
        if len(code_data) >= 2:
            code_data['ema'] = calc_ema(code_data['count'])
            best_row = code_data.loc[code_data['ema'].idxmax()]
            results.append({
                'code': code,
                'best_year': int(best_row['year'])
            })
    
    results_df = pd.DataFrame(results)
    best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()
else:
    best_2022_codes = []

result_str = json.dumps(best_2022_codes)

print("__RESULT__:")
print(result_str)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
