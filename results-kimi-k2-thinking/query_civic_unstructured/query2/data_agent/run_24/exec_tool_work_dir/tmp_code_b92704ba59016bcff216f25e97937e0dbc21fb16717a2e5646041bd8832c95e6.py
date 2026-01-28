code = """import json

# Load funding records
with open('/tmp/tmppww0g6j4.json', 'r') as f:
    funding = json.load(f)

# Create lookup for park projects
park_projects_funding = {}
for record in funding:
    name = record['Project_Name']
    name_lower = name.lower()
    amount = int(record['Amount'])
    
    # Check for the park projects that were completed in Nov 2022
    if 'bluffs park shade' in name_lower:
        park_projects_funding['Bluffs Park Shade Structure'] = amount
    elif 'broad beach road water quality' in name_lower:
        park_projects_funding['Broad Beach Road Water Quality Repair'] = amount
    elif 'point dume walkway' in name_lower:
        park_projects_funding['Point Dume Walkway Repairs'] = amount

# Calculate total funding for completed park projects
total_funding = sum(park_projects_funding.values())

# Prepare result
result = {
    'total_funding': total_funding,
    'projects': list(park_projects_funding.keys()),
    'amounts': park_projects_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
