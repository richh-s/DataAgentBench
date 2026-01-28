code = """import json, pandas as pd, re
from datetime import datetime

# Load all data
cpc_path = locals()['var_functions.query_db:66']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

print('Loaded data for analysis')
print('Patents:', len(cpc_data))
print('Level-5 codes:', len(level5_symbols))

# Parse CPC records with year extraction
code_year_counts = {}
years_seen = set()
for row in cpc_data:
    pub_date = row.get('publication_date', '')
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            years_seen.add(year)
        except:
            continue
    
    cpc_str = row.get('cpc', '')
    if cpc_str:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    if level5_code in level5_symbols:
                        key = (level5_code, year)
                        code_year_counts[key] = code_year_counts.get(key, 0) + 1
        except:
            pass

print('Years in data:', sorted(years_seen))
print('Total year-code pairs:', len(code_year_counts))

# Process each code to find best year via EMA
best_2022_codes = []
processed_codes = 0

for code in level5_symbols:
    # Get all years for this code
    code_years = {}
    for (c, y), count in code_year_counts.items():
        if c == code:
            code_years[y] = count
    
    if len(code_years) >= 3:
        # Create full time series
        min_year = min(code_years.keys())
        max_year = max(code_years.keys())
        years = list(range(min_year, max_year + 1))
        counts = [code_years.get(y, 0) for y in years]
        
        # Calculate EMA
        ema = pd.Series(counts).ewm(alpha=0.2, adjust=False).mean()
        best_year = years[ema.idxmax()]
        
        if best_year == 2022:
            best_2022_codes.append(code)
        processed_codes += 1

print('Codes processed:', processed_codes)
print('Codes with best year 2022:', len(best_2022_codes))

# Return JSON result
result = json.dumps(sorted(best_2022_codes))
print('__RESULT__:'+result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': []}

exec(code, env_args)
