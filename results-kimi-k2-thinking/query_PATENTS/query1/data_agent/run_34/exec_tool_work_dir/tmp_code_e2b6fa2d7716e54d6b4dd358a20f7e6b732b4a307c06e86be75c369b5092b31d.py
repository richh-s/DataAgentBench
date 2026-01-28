code = """import json, pandas as pd, re
from datetime import datetime

# Debug: print available variables
all_keys = [k for k in locals().keys()]
print('Available keys:', all_keys)

# Load the data using the correct variable names
try:
    with open(var_functions.query_db_2, 'r') as f:
        cpc_data = json.load(f)
    print('Loaded CPC data from file, records:', len(cpc_data))
except:
    print('Failed to load CPC data')
    cpc_data = []

# Level 5 codes
level_5_codes = var_functions.query_db_5
print('Level 5 codes obtained, count:', len(level_5_codes))

# Parse CPC data
cpc_records = []
for row in cpc_data[:1000]:  # Limit for testing
    cpc_str = row.get('cpc', '')
    pub_date = row.get('publication_date', '')
    
    # Parse year
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
            pass

print('Parsed records:', len(cpc_records))
if cpc_records:
    print('Sample record:', cpc_records[0])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01J', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01M', 'level': '5.0'}]}

exec(code, env_args)
