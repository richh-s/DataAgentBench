code = """import json
import re

# Access the funding data from the previous query
funding_records = var_functions.query_db:8

print(f"Total funding records: {len(funding_records)}")
print(f"Number of records (preview): {funding_records[:3]}")

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

# Display top projects for verification
for i, proj in enumerate(park_funding_sorted[:10]):
    print(f"{i+1}. {proj['project_name']}: ${proj['amount']:,}")

# Calculate total funding for park projects
total_park_funding = sum(proj['amount'] for proj in park_funding)
print(f"\nTotal park funding (all years): ${total_park_funding:,}")

result = {
    'park_funding': park_funding_sorted,
    'total_park_funding': total_park_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
