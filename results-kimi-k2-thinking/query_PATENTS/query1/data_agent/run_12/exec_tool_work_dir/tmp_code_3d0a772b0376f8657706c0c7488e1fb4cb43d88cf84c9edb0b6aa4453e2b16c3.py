code = """import json
import pandas as pd
from datetime import datetime
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print('Level 5 symbols count:', len(level5_symbols))
print('Sample level 5 symbols:', sorted(list(level5_symbols))[:20])

# Load all publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

print('Total publication records:', len(publication_data))

# Examine CPC codes in publications
all_codes = []
for record in publication_data[:50]:  # Sample first 50
    cpc_str = record.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    all_codes.extend(codes)

print('Sample CPC codes from publications:', list(set(all_codes))[:20])

# Check if any codes match level 5
matching_codes = []
for code in all_codes:
    # Get the group (first part before /)
    group = code.split('/')[0].split()[0]
    # Check against level 5
    if group in level5_symbols:
        matching_codes.append(code)

print('Matching level 5 codes found:', len(matching_codes))
print('Sample matches:', matching_codes[:10])

# Let's also check partial matches - maybe codes start with level5 symbols
partial_matches = []
for code in all_codes:
    code_no_subclass = code.split('/')[0].split()[0]
    for level5 in level5_symbols:
        if code_no_subclass.startswith(level5):
            partial_matches.append((code, level5))

print('Partial matches found:', len(partial_matches))
print('Sample partial matches:', partial_matches[:10])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}}

exec(code, env_args)
