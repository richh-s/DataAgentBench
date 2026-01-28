code = """import json
import re
from collections import defaultdict

# Get stored file path
stored = var_functions.query_db:32
file_path = stored if isinstance(stored, str) else stored[0] if isinstance(stored, list) else None

print(f'File path: {file_path}')

# Load data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f'Total records: {len(data)}')

# Process data to count CPC codes by year and calculate EMA
year_cpc_counts = defaultdict(lambda: defaultdict(int))
all_years = set()
all_cpc_codes = set()

for record in data:
    cpc_str = record.get('cpc', '[]')
    try:
        cpc_list = json.loads(cpc_str)
        codes = [item.get('code', '') for item in cpc_list if item.get('code')]
        
        # This data doesn't have publication dates, so we'll skip EMA calculation
        # Just extract CPC level 5 codes
        for code in codes:
            base = code.split('/')[0]
            if len(base) >= 5:
                level5 = base[:5]
                all_cpc_codes.add(level5)
    except:
        continue

print(f'Found {len(all_cpc_codes)} unique level 5 CPC codes')
print('Sample CPC codes:', list(all_cpc_codes)[:10])

# Return empty list as we need more data to calculate EMA properly
result = []
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': [{'count': '277813'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}, {'symbol': 'A01N', 'level': '5.0'}, {'symbol': 'A01P', 'level': '5.0'}, {'symbol': 'A01D', 'level': '5.0'}, {'symbol': 'A01L', 'level': '5.0'}, {'symbol': 'A01K', 'level': '5.0'}], 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
