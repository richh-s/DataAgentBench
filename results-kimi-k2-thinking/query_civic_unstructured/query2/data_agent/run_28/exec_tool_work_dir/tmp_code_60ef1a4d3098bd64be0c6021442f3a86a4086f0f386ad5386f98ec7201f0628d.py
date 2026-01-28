code = """import json
import re

# Store the reference to the funding data in a local variable
funding_data = var_functions.query_db:8

print(f"Type of funding_data: {type(funding_data)}")
print(f"Content preview: {funding_data[:2] if isinstance(funding_data, list) else str(funding_data)[:200]}")

# Filter for park-related projects
park_funding = []
for record in funding_data:
    project_name = str(record.get('Project_Name', '')).lower()
    if 'park' in project_name:
        amount = int(record.get('Amount', 0))
        park_funding.append({
            'project_name': record.get('Project_Name'),
            'amount': amount
        })

print(f"Park-related funding records: {len(park_funding)}")

# Sort by amount descending
park_funding_sorted = sorted(park_funding, key=lambda x: x['amount'], reverse=True)

# Display top 5 for verification
print("\nTop 5 park projects:")
for i, proj in enumerate(park_funding_sorted[:5]):
    print(f"{i+1}. {proj['project_name']}: ${proj['amount']:,}")

# Total funding for park projects
total_park_funding = sum(proj['amount'] for proj in park_funding_sorted)
print(f"\nTotal park funding (all years): ${total_park_funding:,}")

result = {
    'park_projects': park_funding_sorted,
    'total_park_funding_all_years': total_park_funding
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
