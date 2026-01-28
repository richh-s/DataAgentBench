code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_path = locals()['var_functions.query_db:50']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC records
cpc_records = []
year_counts = {}
code_counts = {}

for row in cpc_data:
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
                            year_counts[year] = year_counts.get(year, 0) + 1
                            code_counts[level5_code] = code_counts.get(level5_code, 0) + 1
        except:
            pass

# Analyze the data
df = pd.DataFrame(cpc_records)

print('=== DATA SUMMARY ===')
print(f'Total records: {len(df)}')
print(f'Year range: {df["year"].min()} to {df["year"].max()}')
print(f'Unique level-5 codes: {df["code"].nunique()}')

print('\n=== YEAR DISTRIBUTION ===')
year_dist = df['year'].value_counts().sort_index()
print(year_dist)

print('\n=== TOP 10 LEVEL-5 CODES ===')
top_codes = df['code'].value_counts().head(10)
print(top_codes)

# Check 2022 specifically
print('\n=== 2022 DATA CHECK ===')
df_2022 = df[df['year'] == 2022]
print(f'Records in 2022: {len(df_2022)}')
print(f'Unique codes in 2022: {df_2022["code"].nunique()}')

if len(df_2022) > 0:
    print('Top codes in 2022:')
    print(df_2022['code'].value_counts().head())

# Find codes with best year 2022 by EMA
counts = df.groupby(['year', 'code']).size().reset_index(name='count')
code_best_years = []

for code in counts['code'].unique():
    code_data = counts[counts['code'] == code].sort_values('year')
    
    if len(code_data) >= 3:  # Need at least 3 years
        # Fill missing years
        year_range = range(int(code_data['year'].min()), int(code_data['year'].max()) + 1)
        full_years = pd.DataFrame({'year': list(year_range)})
        code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
        code_full = code_full.sort_values('year')
        
        # Calculate EMA
        code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
        
        best_year = int(code_full.loc[code_full['ema'].idxmax(), 'year'])
        code_best_years.append({'code': code, 'best_year': best_year})

results_df = pd.DataFrame(code_best_years)

if len(results_df) > 0:
    print('\n=== BEST YEAR DISTRIBUTION ===')
    print(results_df['best_year'].value_counts().sort_index())
    
    codes_2022 = results_df[results_df['best_year'] == 2022]['code'].tolist()
    print(f'\nCodes with best year 2022: {len(codes_2022)}')
    if codes_2022:
        print('Sample codes:', codes_2022[:10])
else:
    codes_2022 = []

result = json.dumps(codes_2022)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': []}

exec(code, env_args)
