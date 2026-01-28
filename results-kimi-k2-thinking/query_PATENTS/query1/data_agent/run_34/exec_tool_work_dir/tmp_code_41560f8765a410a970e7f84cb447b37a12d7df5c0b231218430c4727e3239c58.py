code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_data = json.load(open(locals()['var_functions.query_db:50']))
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

# Analyze the data
import pandas as pd
df = pd.DataFrame(cpc_records)

print('=== SUMMARY ===')
print(f'Total records: {len(df)}')
print(f'Year range: {df["year"].min()} to {df["year"].max()}')
print(f'Unique codes: {df["code"].nunique()}')

print('\n=== YEAR DISTRIBUTION ===')
year_dist = df['year'].value_counts().sort_index()
print(year_dist)

# Count filings per year per code
counts = df.groupby(['year', 'code']).size().reset_index(name='count')

# For each code, find its best year based on filing count
print('\n=== FINDING BEST YEAR FOR EACH CODE ===')

best_years_data = []
for code in counts['code'].unique():
    code_data = counts[counts['code'] == code].sort_values('year')
    if len(code_data) >= 2:
        # Find year with max count (simpler than EMA for debugging)
        max_row = code_data.loc[code_data['count'].idxmax()]
        best_years_data.append({
            'code': code,
            'best_year': int(max_row['year']),
            'max_count': int(max_row['count']),
            'years_available': len(code_data)
        })

best_years_df = pd.DataFrame(best_years_data)
print(f'Codes processed: {len(best_years_df)}')

print('\n=== DISTRIBUTION OF BEST YEARS ===')
best_year_dist = best_years_df['best_year'].value_counts().sort_index()
print(best_year_dist)

# Check 2022 specifically
codes_best_in_2022 = best_years_df[best_years_df['best_year'] == 2022]
print(f'\n=== CODES WITH BEST YEAR 2022: {len(codes_best_in_2022)} ===')
if len(codes_best_in_2022) > 0:
    print(codes_best_in_2022.head())
    codes_list = codes_best_in_2022['code'].tolist()
else:
    print('No codes found with best year 2022')
    codes_list = []

# Now use EMA method and compare
print('\n=== EMA ANALYSIS ===')
ema_codes_2022 = []

for code in best_years_df['code'].unique():
    code_data = counts[counts['code'] == code].sort_values('year')
    if len(code_data) >= 3:
        year_range = range(int(code_data['year'].min()), int(code_data['year'].max()) + 1)
        full_years = pd.DataFrame({'year': list(year_range)})
        code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
        code_full = code_full.sort_values('year')
        code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
        
        best_year = int(code_full.loc[code_full['ema'].idxmax(), 'year'])
        if best_year == 2022:
            ema_codes_2022.append(code)

print(f'Codes with EMA best year 2022: {len(ema_codes_2022)}')

result = json.dumps(ema_codes_2022)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': []}

exec(code, env_args)
