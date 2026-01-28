code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC data
cpc_path = var_functions.query_db_26
cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path

# Load level 5 codes
level5_path = var_functions.query_db_28
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path
level5_symbols = [item['symbol'] for item in level5_data]

print('Raw records:', len(cpc_data), 'Level-5 symbols:', len(level5_symbols))

# Parse the data
cpc_records = []
for i, row in enumerate(cpc_data[:50000]):  # Process in chunks
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Extract year
    year = None
    if pub_date and len(pub_date) > 10:
        try:
            clean_date = re.sub(r'\d+(st|nd|rd|th)', lambda x: x.group()[:-2], pub_date)
            date_parts = clean_date.replace(',', '').split()
            if len(date_parts) == 3:
                year = int(date_parts[2])
        except:
            year = None
    
    # Parse CPC codes
    if cpc_str and len(cpc_str) > 10:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    cpc_records.append({'code': code, 'year': year})
        except:
            pass

# Process data
df = pd.DataFrame(cpc_records)
print('Parsed records:', len(df))

if len(df) > 0:
    df['level5'] = df['code'].str.extract(r'^([A-Z]\d{2}[A-Z]?)')[0]
    level5_df = df[df['level5'].isin(level5_symbols)]
    print('Level-5 records:', len(level5_df))
    
    # Year counts
    counts = level5_df.groupby(['year', 'level5']).size().reset_index(name='count')
    print('Year-code combinations:', len(counts))
    
    # EMA calculation
    def calc_ema(series, alpha=0.2):
        return series.ewm(alpha=alpha, adjust=False).mean()
    
    results = []
    for code in level5_symbols[:100]:  # Test subset
        code_data = counts[counts['level5'] == code].sort_values('year')
        if len(code_data) > 1:
            code_data['ema'] = calc_ema(code_data['count'])
            best = code_data.loc[code_data['ema'].idxmax()]
            results.append({'code': code, 'best_year': int(best['year'])})
    
    results_df = pd.DataFrame(results)
    best_2022 = results_df[results_df['best_year'] == 2022]['code'].tolist()
    
    print('2022 best year count:', len(best_2022))
    output = json.dumps(best_2022)
else:
    output = json.dumps([])

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
