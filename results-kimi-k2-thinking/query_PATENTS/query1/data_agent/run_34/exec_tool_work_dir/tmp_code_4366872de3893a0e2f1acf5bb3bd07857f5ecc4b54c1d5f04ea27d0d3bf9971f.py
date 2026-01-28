code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_var = locals()['var_functions.query_db:26']
level5_var = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_var)) if isinstance(cpc_var, str) else cpc_var
level5_data = json.load(open(level5_var)) if isinstance(level5_var, str) else level5_var

level5_symbols = set([item['symbol'] for item in level5_data])
print('Loaded:', len(cpc_data), 'records,', len(level5_symbols), 'level-5 codes')

# Let's examine the data structure first
sample = cpc_data[0] if cpc_data else {}
print('Sample record:', json.dumps(sample)[:200])

# Parse records carefully
cpc_records = []
year_counts = {}

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
            year_counts[year] = year_counts.get(year, 0) + 1
        except:
            pass
    
    # Parse CPC codes
    if cpc_str and len(cpc_str) > 10:
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

print('Year distribution:', year_counts)
print('Parsed records:', len(cpc_records))

# Process the data
if cpc_records:
    df = pd.DataFrame(cpc_records)
    df = df.dropna(subset=['year', 'code'])
    
    # Filter to recent years where we likely have data
    valid_years = list(range(2015, 2024))
    df_filtered = df[df['year'].isin(valid_years)]
    
    print('Filtered records:', len(df_filtered))
    
    # Count filings per year per code
    counts = df_filtered.groupby(['year', 'code']).size().reset_index(name='count')
    print('Year-code combinations:', len(counts))
    
    # Check each code's best year based on simple max count
    code_best_years = {}
    for code in counts['code'].unique():
        code_data = counts[counts['code'] == code]
        if len(code_data) >= 2:
            best_year = code_data.loc[code_data['count'].idxmax(), 'year']
            code_best_years[code] = best_year
    
    # Count which year is most common as best year
    best_years = list(code_best_years.values())
    year_dist = pd.Series(best_years).value_counts().sort_index()
    print('\nDistribution of best years:')
    print(year_dist)
    
    # Find codes best in 2022
    codes_2022 = [code for code, year in code_best_years.items() if year == 2022]
    print(f'\nCodes with best year 2022: {len(codes_2022)}')
    
    result = codes_2022
else:
    result = []

print('__RESULT__:', json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': []}

exec(code, env_args)
