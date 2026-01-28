code = """import json
import pandas as pd
from datetime import datetime
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print('Sample level 5 symbols:', list(level5_symbols)[:20])

# Load full publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    full_publication_data = json.load(f)

print('Publication records:', len(full_publication_data))

# Examine a few records
for i in range(min(5, len(full_publication_data))):
    record = full_publication_data[i]
    print(f'\nRecord {i+1}:')
    print('  Filing date:', record.get('filing_date'))
    print('  CPC field (truncated):', record.get('cpc', '')[:200])
    
    # Extract CPC codes
    cpc_str = record.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    print('  Extracted codes:', codes)
    
    # Check which groups match level 5
    for code in codes:
        group = code.split('/')[0].split()[0]
        is_level5 = group in level5_symbols
        print(f'    {code} -> group {group} (level5: {is_level5})')

# Let's also check the format of level 5 symbols more carefully
print('\nLevel 5 symbol patterns:')
samples = list(level5_symbols)[:10]
for sym in samples:
    print(f'  {sym} (length: {len(sym)})')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}}

exec(code, env_args)
