code = """import json
import re
import os

# Read funding data
funding_file = 'funding_query_result.json'
with open(funding_file, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

print(f"Total funding records: {len(funding_records)}")

# Filter for park-related projects
park_funding = []
for record in funding_records:
    project_name = record.get('Project_Name', '').lower()
    if 'park' in project_name:
        park_funding.append({
            'project_name': record.get('Project_Name'),
            'amount': int(record.get('Amount', 0))
        })

print(f"Park-related funding records: {len(park_funding)}")

# Sort by amount descending
park_funding_sorted = sorted(park_funding, key=lambda x: x['amount'], reverse=True)

for i, proj in enumerate(park_funding_sorted[:10]):
    print(f"{i+1}. {proj['project_name']}: ${proj['amount']:,}")

result = park_funding_sorted
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
