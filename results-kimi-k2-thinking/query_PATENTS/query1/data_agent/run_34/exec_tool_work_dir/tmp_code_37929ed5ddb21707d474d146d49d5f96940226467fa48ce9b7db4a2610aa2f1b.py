code = """import json, pandas as pd, re
from datetime import datetime
from dateutil import parser

print('Loading CPC data...')
cpc_path = locals()['var_functions.query_db:66']
if isinstance(cpc_path, str) and '.json' in cpc_path:
    with open(cpc_path, 'r') as f:
        cpc_data = json.load(f)
else:
    cpc_data = cpc_path

print('Loading level-5 CPC codes...')
level5_path = locals()['var_functions.query_db:28']
if isinstance(level5_path, str) and '.json' in level5_path:
    with open(level5_path, 'r') as f:
        level5_data = json.load(f)
else:
    level5_data = level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

# More flexible date parsing
def parse_flexible_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    
    try:
        # Remove ordinal suffixes and extra text
        clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', date_str)
        clean_date = re.sub(r'on |of |the ', '', clean_date, flags=re.IGNORECASE)
        clean_date = clean_date.strip()
        
        # Try parsing with dateutil
        date_obj = parser.parse(clean_date, fuzzy=True)
        return date_obj.year
    except:
        try:
            # Manual parsing for common formats
            patterns = [
                r'(\w+)\s+(\d+),?\s+(\d{4})',  # "March 15, 2022" or "March 15 2022"
                r'(\d+)\s+(\w+)\s+(\d{4})',    # "15 March 2022" or "15th March 2022"
                r'(\d{4}),?\s+(\w+)\s+(\d+)'   # "2022, March 15"
            ]
            
            for pattern in patterns:
                match = re.search(pattern, clean_date)
                if match:
                    return int(match.group(3))
        except:
            pass
    return None

# Parse CPC records
print('Parsing records...')
code_year_counts = {}
years_seen = set()
for i, row in enumerate(cpc_data):
    pub_date = row.get('publication_date', '')
    year = parse_flexible_date(pub_date)
    
    if year:
        years_seen.add(year)
    
    cpc_str = row.get('cpc', '')
    if cpc_str and isinstance(cpc_str, str) and len(cpc_str.strip()) > 10:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                if isinstance(item, dict):
                    code = item.get('code', '')
                    if code and len(code) >= 4:
                        level5_code = code[:4]
                        if level5_code in level5_symbols:
                            key = (level5_code, year)
                            code_year_counts[key] = code_year_counts.get(key, 0) + 1
        except:
            pass

print(f'Parsed {len(code_year_counts)} year-code pairs from {len(cpc_data)} patents')
print(f'Years in data: {sorted(years_seen)}')

# Check 2022 specifically
has_2022 = any(year == 2022 for (_, year) in code_year_counts.keys())
print(f'2022 data present: {has_2022}')
if has_2022:
    codes_2022 = [code for (code, year) in code_year_counts.keys() if year == 2022]
    print(f'Codes with 2022 data: {len(set(codes_2022))}')

# Calculate EMA for each code
codes_best_in_2022 = []
processed = 0

for code in level5_symbols:
    # Get all years data for this code
    code_data = {}
    for (c, y), count in code_year_counts.items():
        if c == code and y is not None:
            code_data[y] = count
    
    # Need at least 3 years of data for meaningful EMA
    if len(code_data) >= 3:
        processed += 1
        years = sorted(code_data.keys())
        counts = [code_data[y] for y in years]
        
        # Calculate EMA
        ema = pd.Series(counts).ewm(alpha=0.2, adjust=False).mean()
        best_year_idx = ema.idxmax()
        best_year = years[best_year_idx]
        
        if best_year == 2022:
            codes_best_in_2022.append(code)

print(f'Codes processed: {processed}')
print(f'Codes with best year 2022: {len(codes_best_in_2022)}')

if codes_best_in_2022:
    print('Sample codes with best year 2022:')
    for code in sorted(codes_best_in_2022)[:10]:
        print(f'  {code}')

# Return final result
result = json.dumps(sorted(codes_best_in_2022))
print('__RESULT__:' + result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:44': [], 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:58': [], 'var_functions.execute_python:62': [], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.execute_python:68': [], 'var_functions.execute_python:86': [], 'var_functions.execute_python:90': [], 'var_functions.query_db:92': [{'publication_date': 'on March 15th, 2022'}, {'publication_date': '25th Jan 2022'}, {'publication_date': 'April 19th, 2022'}, {'publication_date': '28th June 2022'}, {'publication_date': '25th October 2022'}, {'publication_date': '30th of August, 2022'}, {'publication_date': '2nd August 2022'}, {'publication_date': 'Feb 8th, 2022'}, {'publication_date': '8th November 2022'}, {'publication_date': '2022, November 1st'}], 'var_functions.query_db:93': [{'publication_date': 'on September 9th, 2022'}, {'publication_date': 'on September 9th, 2021'}, {'publication_date': 'on September 9th, 2019'}, {'publication_date': 'on September 9th, 2017'}, {'publication_date': 'on September 9th, 2015'}, {'publication_date': 'on September 9th, 2014'}, {'publication_date': 'on September 9th, 2011'}, {'publication_date': 'on September 9th, 2009'}, {'publication_date': 'on September 9th, 2005'}, {'publication_date': 'on September 9th, 2004'}]}

exec(code, env_args)
