code = """import json, pandas as pd, re
from datetime import datetime

# Load data
cpc_path = locals()['var_functions.query_db:26']
level5_path = locals()['var_functions.query_db:28']

cpc_data = json.load(open(cpc_path)) if isinstance(cpc_path, str) and '.json' in cpc_path else cpc_path
level5_data = json.load(open(level5_path)) if isinstance(level5_path, str) and '.json' in level5_path else level5_path

level5_symbols = set([item['symbol'] for item in level5_data])

print('Input data:', len(cpc_data), 'records,', len(level5_symbols), 'level-5 codes')

# Sample of data
if cpc_data:
    print('Sample record:', json.dumps(cpc_data[0], indent=2)[:200])

# Parse with error handling
cpc_records = []
valid_years = set()
valid_codes = set()

for i, row in enumerate(cpc_data):
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
    year = None
    if pub_date:
        try:
            clean_date = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', pub_date)
            date_obj = datetime.strptime(clean_date.strip(), '%b %d, %Y')
            year = date_obj.year
            valid_years.add(year)
        except Exception as e:
            continue
    
    # Parse CPC codes
    if cpc_str:
        try:
            codes = json.loads(cpc_str)
            for item in codes:
                code = item.get('code', '')
                if code and len(code) >= 4:
                    level5_code = code[:4]
                    cpc_records.append({'level5_code': level5_code, 'year': year})
                    valid_codes.add(level5_code)
        except Exception as e:
            continue

print('Parsed', len(cpc_records), 'records')
print('Valid years range:', min(valid_years) if valid_years else 'None', 'to', max(valid_years) if valid_years else 'None')
print('Unique level-5 codes found:', len(valid_codes))
print('Sample codes:', list(valid_codes)[:10])

# Check intersection with level5 symbols
intersection = valid_codes.intersection(level5_symbols)
print('Matching level-5 codes:', len(intersection))

if cpc_records:
    df = pd.DataFrame(cpc_records)
    print('DataFrame columns:', df.columns.tolist())
    print('DataFrame shape:', df.shape)
    print('First rows:')
    print(df.head())"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}], 'var_functions.list_db:22': ['publicationinfo'], 'var_functions.list_db:23': ['cpc_definition'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
