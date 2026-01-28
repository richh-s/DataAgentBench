code = """import json
import re

# Read the full dataset
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    records = json.load(f)

print('Total records:', len(records))

# Let's examine the structure of Patents_info, citation, and cpc
sample = records[0]
print('Sample Patents_info:', sample['Patents_info'][:200] if sample['Patents_info'] else 'None')
print('Sample citation (first 500 chars):', str(sample['citation'])[:500] if sample['citation'] else 'None')
print('Sample cpc (first 500 chars):', str(sample['cpc'])[:500] if sample['cpc'] else 'None')

# Count records with UNIV CALIFORNIA
univ_california_records = 0
for record in records:
    if record['Patents_info'] and 'UNIV CALIFORNIA' in record['Patents_info']:
        univ_california_records += 1

print('Records with UNIV CALIFORNIA:', univ_california_records)

# Check the structure better
print('\n=== Detailed Analysis ===')
for i, record in enumerate(records[:3]):
    print('\n--- Record', i, '---')
    print('Patents_info:', record['Patents_info'])
    print('Citation:', record['citation'])
    # Try to parse CPC
    if record['cpc']:
        if record['cpc'].strip().startswith('['):
            try:
                cpc_data = json.loads(record['cpc'])
                print('CPC entries:', len(cpc_data))
            except:
                print('CPC (unparsed):', record['cpc'][:200])
        else:
            print('CPC (not JSON array):', record['cpc'][:200])"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
