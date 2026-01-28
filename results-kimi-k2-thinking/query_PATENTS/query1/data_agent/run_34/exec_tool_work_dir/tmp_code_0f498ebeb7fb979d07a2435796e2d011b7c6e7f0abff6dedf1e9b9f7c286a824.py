code = """import json, pandas as pd, re
from datetime import datetime

# Load all data
cpc_path = locals()['var_functions.query_db:66']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

# Parse CPC records with detailed tracking
cpc_by_year = {}
code_totals = {}
year_range = set()

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
                    if year not in cpc_by_year:
                        cpc_by_year[year] = {}
                    cpc_by_year[year][level5_code] = cpc_by_year[year].get(level5_code, 0) + 1
                    code_totals[level5_code] = code_totals.get(level5_code, 0) + 1
                    year_range.add(year)
    except:
        pass

# Create a proper DataFrame
all_records = []
for year, codes in cpc_by_year.items():
    for code, count in codes.items():
        all_records.append({'year': year, 'code': code, 'count': count})

df = pd.DataFrame(all_records)

print('=== DATA ANALYSIS SUMMARY ===')
print(f'Total records: {len(df)}')
print(f'Year range: {min(year_range)} to {max(year_range)}')
print(f'Unique level-5 codes: {df["code"].nunique()}')

print('\n=== YEAR DISTRIBUTION ===')
year_counts = df.groupby('year')['count'].sum().sort_index()
print(year_counts)

# Find which year has most total filings
max_year = year_counts.idxmax()
print(f'\nYear with most filings: {max_year} ({year_counts[max_year]} total)')

# Check 2022 specifically
codes_2022 = df[df['year'] == 2022]
print(f'\nCodes with filings in 2022: {len(codes_2022)}')
if len(codes_2022) > 0:
    print('Top 10 codes in 2022:')
    print(codes_2022.nlargest(10, 'count')[['code', 'count']])

# Now do the formal EMA calculation
code_best_years = []
for code in level5_symbols:
    code_data = df[df['code'] == code].sort_values('year')
    if len(code_data) >= 2:
        year_series = list(range(int(code_data['year'].min()), int(code_data['year'].max()) + 1))
        full_series = []
        for yr in year_series:
            count = code_data[code_data['year'] == yr]['count'].sum() if yr in code_data['year'].values else 0
            full_series.append(count)
        
        if len(full_series) >= 2:
            ema_series = pd.Series(full_series).ewm(alpha=0.2, adjust=False).mean()
            best_year_idx = ema_series.idxmax()
            best_year = year_series[best_year_idx]
            
            code_best_years.append({
                'code': code,
                'best_year': best_year,
                'total_filings': sum(full_series)
            })

results_df = pd.DataFrame(code_best_years)

if len(results_df) > 0:
    print(f'\n=== BEST YEAR DISTRIBUTION (EMA) ===')
    best_year_dist = results_df['best_year'].value_counts().sort_index()
    print(best_year_dist)
    
    codes_best_2022 = results_df[results_df['best_year'] == 2022]['code'].tolist()
    print(f'\nCodes with best year 2022: {len(codes_best_2022)}')
    
    if codes_best_2022:
        print('Sample codes:', codes_best_2022[:10])
else:
    codes_best_2022 = []
    print('\nNo valid data for EMA analysis')

final_result = json.dumps(codes_best_2022)
print('__RESULT__:', final_result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
