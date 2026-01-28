code = """import json
import pandas as pd
import re

# Load CPC level 5 symbols
cpc_file_path = locals()['var_functions.query_db:8']
with open(cpc_file_path, 'r') as f:
    cpc_level5_data = json.load(f)

print('Sample CPC level 5 symbols:')
for item in cpc_level5_data[:10]:
    print(f"  {item['symbol']}")

# Load all publication data
pub_file_path = locals()['var_functions.query_db:20']
with open(pub_file_path, 'r') as f:
    publication_data = json.load(f)

print('\nSample CPC codes from publications:')
for i in range(min(5, len(publication_data))):
    record = publication_data[i]
    cpc_str = record.get('cpc', '')
    print(f"\nRecord {i+1} - Filing date: {record.get('filing_date')}")
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    for code in codes:
        print(f"  Full code: {code}")
        # Parse different group levels
        parts = code.split('/')[0].split('.')
        if len(parts) >= 1:
            group_level = len(parts[0])
            print(f"    Main group: {parts[0]} (length: {group_level})")
        if len(parts) >= 2:
            print(f"    Subclass: {parts[1]}")

# Check for pattern matches manually
all_codes = []
for record in publication_data:
    cpc_str = record.get('cpc', '')
    codes = re.findall(r'"code":\s*"([^"]+)"', cpc_str)
    all_codes.extend(codes)

print(f"\nTotal unique codes found: {len(set(all_codes))}")
print('Sample unique codes:', list(set(all_codes))[:20])

# Check if any code contains any level 5 symbol pattern
level5_symbols = set(item['symbol'] for item in cpc_level5_data)
print(f"\nChecking {len(level5_symbols)} level 5 symbols against {len(set(all_codes))} unique codes...")

matches = []
for code in set(all_codes):
    for level5 in level5_symbols:
        if level5 in code:
            matches.append((code, level5))

print(f"Direct substring matches found: {len(matches)}")
for match in matches[:10]:
    print(f"  {match[0]} contains {match[1]}")

print('__RESULT__:')
print(json.dumps({'matches_found': len(matches)}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['cpc_definition'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:32': {'status': 'exploration complete'}, 'var_functions.execute_python:34': {'level5_symbols': 677, 'publication_records': 100, 'status': 'data_loaded'}, 'var_functions.execute_python:38': {'valid_records': 0, 'df_shape': [0, 0], 'data_loaded': True}, 'var_functions.execute_python:54': []}

exec(code, env_args)
