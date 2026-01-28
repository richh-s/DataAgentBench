code = """import json
import re
import os
from collections import defaultdict

# First, let's verify what we have in storage
print('Checking available storage variables:')
storage_keys = [k for k in locals().keys() if 'var_' in k]
print('Available variables:', storage_keys)

# Initialize data structures
uc_patents = []
all_patents = []

# Try to find UC patents in storage
for key, value in locals().items():
    if 'query_db' in key:
        if isinstance(value, str):
            # It's a file path
            if os.path.exists(value):
                try:
                    with open(value, 'r') as f:
                        data = json.load(f)
                        if len(data) > 0 and 'UNIV CALIFORNIA' in str(data[0]):
                            uc_patents = data
                            print(f'Loaded UC patents from file: {value} ({len(data)} records)')
                        else:
                            all_patents.extend(data)
                            print(f'Loaded general patents from file: {value} ({len(data)} records)')
                except:
                    pass
        elif isinstance(value, list):
            if len(value) > 0 and 'UNIV CALIFORNIA' in str(value[0]):
                uc_patents = value
                print(f'Found UC patents in memory: {key} ({len(value)} records)')
            else:
                all_patents.extend(value)
                print(f'Found general patents in memory: {key} ({len(value)} records)')

print(f'\nTotal UC patents: {len(uc_patents)}')
print(f'Total general patents: {len(all_patents)}')

# Extract UC publication numbers
uc_pub_numbers = set()
if uc_patents:
    for patent in uc_patents:
        info = patent.get('Patents_info', '')
        match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
        if match:
            pub_num = match.group(1).strip()
            uc_pub_numbers.add(pub_num)

print(f'Extracted UC publication numbers: {len(uc_pub_numbers)}')
print(f'Sample UC patents: {list(uc_pub_numbers)[:5] if uc_pub_numbers else "None"}')

print('\n__RESULT__:')
print(json.dumps({
    'uc_patents_loaded': len(uc_patents),
    'all_patents_loaded': len(all_patents),
    'uc_publication_numbers': len(uc_pub_numbers)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}], 'var_functions.execute_python:32': {'uc_patents_count': 169, 'all_patents_count': 20000, 'uc_pub_numbers_count': 59}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'uc_patents': 0, 'uc_pub_numbers': 0, 'total_citations': 0, 'unique_assignees': 0, 'sample_assignees': []}, 'var_functions.query_db:42': [{'name': 'publicationinfo'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'uc_patents_loaded': 0, 'uc_pub_numbers': 0, 'uc_cpc_codes_stored': 0}, 'var_functions.execute_python:50': {'uc_patents_count': 0, 'uc_pub_numbers_count': 0, 'total_cpc_codes': 0}, 'var_functions.query_db:52': [{'total': '277813'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
