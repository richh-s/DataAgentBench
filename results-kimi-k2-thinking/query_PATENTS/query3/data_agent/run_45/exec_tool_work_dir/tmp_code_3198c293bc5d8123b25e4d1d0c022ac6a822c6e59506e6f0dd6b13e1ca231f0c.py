code = """import json
import re
from collections import defaultdict
import os

# Get data from storage - check if it's a file path or actual data
uc_patents_ref = 'var_functions.query_db:8'
all_patents_ref = 'var_functions.query_db:22'

uc_patents = locals()[uc_patents_ref]
all_patents = locals()[all_patents_ref]

# If it's a file path (string), read the file
if isinstance(uc_patents, str) and os.path.exists(uc_patents):
    with open(uc_patents, 'r') as f:
        uc_patents = json.load(f)

if isinstance(all_patents, str) and os.path.exists(all_patents):
    with open(all_patents, 'r') as f:
        all_patents = json.load(f)

print('UNIV CALIFORNIA patents:', len(uc_patents))
print('All patents sample:', len(all_patents))

if uc_patents:
    print('Sample UC patent:', uc_patents[0]['Patents_info'][:100])

if all_patents:
    print('Sample all patent:', all_patents[0]['Patents_info'][:100])
    cit = all_patents[0].get('citation', 'None')
    print('Sample citation:', str(cit)[:200] if cit else 'None')

# Extract UC publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    info = patent['Patents_info']
    match = re.search(r'pub\.?\s*number\s*([A-Z0-9-]+)', info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.add(pub_num)

print('Extracted UC publication numbers:', len(uc_pub_numbers))
if uc_pub_numbers:
    print('Sample numbers:', list(uc_pub_numbers)[:5])

print('__RESULT__:')
result = {
    'uc_patents_count': len(uc_patents),
    'all_patents_count': len(all_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['cpc_definition'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'symbol': 'A', 'titleFull': 'HUMAN NECESSITIES'}, {'symbol': 'B', 'titleFull': 'PERFORMING OPERATIONS; TRANSPORTING'}, {'symbol': 'C', 'titleFull': 'CHEMISTRY; METALLURGY'}]}

exec(code, env_args)
