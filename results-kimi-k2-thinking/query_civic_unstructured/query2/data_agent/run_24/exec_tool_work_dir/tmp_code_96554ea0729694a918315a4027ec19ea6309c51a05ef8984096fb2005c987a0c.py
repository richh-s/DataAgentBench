code = """import json
import re

# Get file paths from the result variables
civic_file = var_functions.query_db_72
funding_file = var_functions.query_db_73

# Load the data
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

print('Data loaded successfully')
print('Civic docs count:', len(civic_docs))
print('Funding records count:', len(funding))

# According to the civic docs preview, these park projects completed in Nov 2022:
# - Bluffs Park Shade Structure
# - Broad Beach Road Water Quality Repair
# - Point Dume Walkway Repairs
# - Marie Canyon Green Streets (completed Jan 2023, but likely funded)

# Create mapping of project names to funding amounts
funding_map = {}
for record in funding:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[proj_name.lower()] = amount

# Check for our target park projects
park_projects = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

total_funding = 0
matched_projects = []

for project in park_projects:
    proj_lower = project.lower()
    if proj_lower in funding_map:
        amount = funding_map[proj_lower]
        total_funding += amount
        matched_projects.append({'name': project, 'amount': amount})
        print('Found:', project, '- $' + str(amount))
    else:
        # Try partial matching
        for key, value in funding_map.items():
            if proj_lower in key or key in proj_lower:
                total_funding += value
                matched_projects.append({'name': project, 'amount': value, 'matched_to': key})
                print('Partial match:', project, '->', key, '- $' + str(value))
                break

# Remove duplicates and sum
final_amounts = {}
for proj in matched_projects:
    name = proj['name']
    if name not in final_amounts:
        final_amounts[name] = proj['amount']

result = {
    'total_funding': sum(final_amounts.values()),
    'projects': [{'name': k, 'amount': v} for k, v in final_amounts.items()],
    'count': len(final_amounts)
}

print('\nRESULT:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
