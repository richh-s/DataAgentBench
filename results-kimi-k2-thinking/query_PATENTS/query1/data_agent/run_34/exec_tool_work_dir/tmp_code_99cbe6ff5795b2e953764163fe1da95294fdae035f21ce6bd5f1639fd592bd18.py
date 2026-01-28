code = """import json, pandas as pd, re
from datetime import datetime

# Load CPC patent data
cpc_path = locals()['var_functions.query_db:50']
cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path

# Load level-5 CPC codes
level5_path = locals()['var_functions.query_db:28']
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path
level5_symbols = set([item['symbol'] for item in level5_data])

print('Loaded', len(cpc_data), 'patent records and', len(level5_symbols), 'level-5 codes')

# Parse CPC codes and years from patent data
cpc_records = []
year_dist = {}

for row in cpc_data:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year from publication_date
    year = None
    if pub_date and isinstance(pub_date, str):
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            year_dist[year] = year_dist.get(year, 0) + 1
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

# Create DataFrame
df = pd.DataFrame(cpc_records)
print('Parsed', len(df), 'CPC code-year records')
print('Year range:', min(year_dist), 'to', max(year_dist))

# Count filings per year per level-5 code
counts = df.groupby(['year', 'code']).size().reset_index(name='count')
print('Year-code combinations:', len(counts))

# Calculate EMA for each code - alpha=0.2 means smoothing factor 0.2
def calc_ema_for_code(code_data):
    """Calculate exponential moving average for a single code's time series"""
    if len(code_data) < 2:
        return None
    
    # Ensure we have all years and fill missing years with 0
    year_range = range(int(code_data['year'].min()), int(code_data['year'].max()) + 1)
    full_years = pd.DataFrame({'year': list(year_range)})    
    code_full = full_years.merge(code_data, on='year', how='left').fillna(0)
    
    # Sort by year and calculate EMA
    code_full = code_full.sort_values('year')
    code_full['ema'] = code_full['count'].ewm(alpha=0.2, adjust=False).mean()
    
    return code_full

# Process each level-5 code
code_results = []

for code in level5_symbols:
    code_data = counts[counts['code'] == code].copy()
    
    if len(code_data) >= 2:  # Need at least 2 years of data
        code_full = calc_ema_for_code(code_data)
        
        if code_full is not None and not code_full.empty:
            # Find year with maximum EMA
            max_idx = code_full['ema'].idxmax()
            best_year = int(code_full.loc[max_idx, 'year'])
            best_ema = float(code_full.loc[max_idx, 'ema'])
            
            code_results.append({
                'code': code,
                'best_year': best_year,
                'best_ema': best_ema
            })

results_df = pd.DataFrame(code_results)
print('Analyzed', len(results_df), 'level-5 codes')

# Find codes whose best year is 2022
best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()
print('Codes with best year 2022:', len(best_2022_codes))

# Return results as JSON
result = json.dumps(best_2022_codes)
print('__RESULT__:', result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
