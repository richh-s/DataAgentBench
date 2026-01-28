code = """import json, pandas as pd, re
from datetime import datetime

# Get data using direct locals access to handle colon in variable names
cpc_var = locals()['var_functions.query_db:26']
level5_var = locals()['var_functions.query_db:28']

# Load CPC data
cpc_data = json.load(open(cpc_var)) if isinstance(cpc_var, str) and '.json' in cpc_var else cpc_var
level5_data = json.load(open(level5_var)) if isinstance(level5_var, str) and '.json' in level5_var else level5_var

level5_symbols = [item['symbol'] for item in level5_data]

print('CPC records:', len(cpc_data), 'Level-5 codes:', len(level5_symbols))

# Parse CPC records
cpc_records = []
for row in cpc_data:
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Extract year from date like "Aug 3rd, 2021"
    year = None
    if pub_date and len(pub_date) > 10:
        try:
            # Remove ordinal suffixes (st, nd, rd, th)
            date_clean = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(date_clean.strip(), '%b %d, %Y')
            year = date_obj.year
        except:
            continue
    
    # Parse CPC codes JSON
    if cpc_str and len(cpc_str) > 10:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    # Extract level-5 group code (first 4 characters, like A01B)
                    level5_code = code[:4]
                    cpc_records.append({'level5_code': level5_code, 'year': year, 'full_code': code})
        except:
            continue

# Create DataFrame
df = pd.DataFrame(cpc_records)
print('Parsed records:', len(df))

# Filter to only level 5 codes
level5_df = df[df['level5_code'].isin(level5_symbols)]
print('Level-5 filtered records:', len(level5_df))

# Count filings per year per level-5 code
counts = level5_df.groupby(['year', 'level5_code']).size().reset_index(name='count')
print('Year-code counts:', len(counts), 'Year range:', counts['year'].min(), 'to', counts['year'].max())

# Calculate EMA (exponential moving average) with alpha=0.2
def calc_ema(g, alpha=0.2):
    return g.ewm(alpha=alpha, adjust=False).mean()

results = []
for code in level5_symbols:
    code_data = counts[counts['level5_code'] == code].sort_values('year')
    if len(code_data) >= 2:  # Need at least 2 years
        code_data['ema'] = calc_ema(code_data['count'])
        best_row = code_data.loc[code_data['ema'].idxmax()]
        results.append({
            'code': code,
            'best_year': int(best_row['year']),
            'best_ema': float(best_row['ema']),
            'best_count': int(best_row['count'])
        })

results_df = pd.DataFrame(results)
print('Codes analyzed:', len(results_df))

# Find codes where best year is 2022
best_2022_codes = results_df[results_df['best_year'] == 2022]['code'].tolist()
print('Codes with best year 2022:', len(best_2022_codes))

# Return as JSON string
answer = json.dumps(best_2022_codes)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
