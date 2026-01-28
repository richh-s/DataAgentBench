code = """import json
import pandas as pd
from datetime import datetime
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print('Level 5 symbols loaded:', len(level5_symbols))

# Load all publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

print('Processing publication records:', len(publication_data))

# Process all records
cpc_years = []
years_found = set()
codes_found = set()

for record in publication_data:
    # Extract year
    filing_date = record.get('filing_date', '')
    year_match = re.search(r'(\d{4})', str(filing_date))
    if not year_match:
        continue
    
    year = int(year_match.group(1))
    years_found.add(year)
    
    # Extract CPC codes  
    cpc_str = record.get('cpc', '')
    if not cpc_str:
        continue
    
    # Parse CPC codes from JSON string
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    for code in codes:
        # Get base group (before /)
        base_group = code.split('/')[0].strip()
        # Extract first part (main group before dot)
        main_group = base_group.split('.')[0]
        codes_found.add(main_group)
        
        # Check if matches any level 5 symbol
        if main_group in level5_symbols:
            cpc_years.append({'cpc_group': main_group, 'year': year})

print('Years found:', sorted(list(years_found)))
print('Unique CPC codes extracted:', len(codes_found))
print('Matching level 5 records:', len(cpc_years))

# Check partial matches - codes that start with level5 symbols
partial_matches = []
for code in codes_found:
    for level5 in level5_symbols:
        if len(code) >= len(level5) and code[:len(level5)] == level5:
            partial_matches.append((code, level5))

print('Partial matches found:', len(partial_matches))
print('Sample partial matches:', partial_matches[:10])
print('Sample codes from data:', list(codes_found)[:20])
print('Sample level 5 symbols:', sorted(list(level5_symbols))[:20])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}}

exec(code, env_args)
