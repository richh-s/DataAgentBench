code = """import json
import re

# Read the full dataset
with open(var_functions.query_db:2, 'r') as f:
    records = json.load(f)

print('Total records:', len(records))

# Examine first record structure
if records:
    sample = records[0]
    print('Sample Patents_info:', sample['Patents_info'][:200] if sample['Patents_info'] else 'None')
    citation_preview = str(sample['citation'])[:500] if sample['citation'] else 'None'
    print('Sample citation (first 500 chars):', citation_preview)
    cpc_preview = str(sample['cpc'])[:500] if sample['cpc'] else 'None'
    print('Sample cpc (first 500 chars):', cpc_preview)

# Count records with UNIV CALIFORNIA
univ_california_records = 0
for record in records:
    if record.get('Patents_info') and 'UNIV CALIFORNIA' in record['Patents_info']:
        univ_california_records += 1

print('Records with UNIV CALIFORNIA:', univ_california_records)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
