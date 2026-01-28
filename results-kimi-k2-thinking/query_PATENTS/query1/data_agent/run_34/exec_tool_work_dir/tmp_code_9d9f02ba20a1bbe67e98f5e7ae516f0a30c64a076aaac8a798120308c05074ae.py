code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC data from file if string path
if isinstance(var_functions.query_db_2, str) and '.json' in var_functions.query_db_2:
    with open(var_functions.query_db_2, 'r') as f:
        cpc_data = json.load(f)
else:
    cpc_data = var_functions.query_db_2

# Level 5 codes from query
level_5_codes = var_functions.query_db_5
level_5_symbols = [item['symbol'] for item in level_5_codes]

print('Loaded CPC data records:', len(cpc_data))
print('Loaded level 5 symbols:', len(level_5_symbols))

# Parse CPC codes and years
cpc_records = []
for row in cpc_data:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year from date
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            pass
    
    # Parse CPC codes
    if cpc_str and cpc_str != '[]':
        try:
            codes_list = json.loads(cpc_str)
            for item in codes_list:
                code = item.get('code', '')
                if code:
                    cpc_records.append({'code': code, 'year': year})
        except:
            # Fallback parsing
            for match in re.findall(r'"code":\s*"([^"]+)"', cpc_str):
                cpc_records.append({'code': match, 'year': year})

# Create DataFrame
df = pd.DataFrame(cpc_records)
print('Total parsed records:', len(df))
print('Year range:', df['year'].min(), 'to', df['year'].max())

# Extract level 5 codes (first part before slash or first 4 characters)
level_5_counts = df[df['code'].notna()].copy()
level_5_counts['level5_code'] = level_5_counts['code'].apply(lambda x: x.split('/')[0][:4] if '/' in x else x[:4])

# Filter to only level 5 codes
level_5_valid = level_5_counts[level_5_counts['level5_code'].isin(level_5_symbols)]
print('Records with level 5 codes:', len(level_5_valid))

# Count filings by year and level5 code
code_year_counts = level_5_valid.groupby(['year', 'level5_code']).size().reset_index(name='count')
print('Total year-code combinations:', len(code_year_counts))

# Calculate EMA for each code
def calc_ema(series, alpha=0.2):
    return series.ewm(alpha=alpha, adjust=False).mean()

results = []
for code in level_5_symbols:
    code_data = code_year_counts[code_year_counts['level5_code'] == code].sort_values('year')
    if len(code_data) > 0:
        code_data['ema'] = calc_ema(code_data['count'])
        best_row = code_data.loc[code_data['ema'].idxmax()]
        results.append({
            'code': code,
            'best_year': int(best_row['year']),
            'best_ema': float(best_row['ema']),
            'best_count': int(best_row['count'])
        })

results_df = pd.DataFrame(results)
print('Codes with EMA calculated:', len(results_df))
print('Best year 2022 count:', len(results_df[results_df['best_year'] == 2022]))

# Filter for codes where best year is 2022
best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()
print('Codes with best year 2022:', len(best_2022_codes))

ans = json.dumps(best_2022_codes)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}]}

exec(code, env_args)
