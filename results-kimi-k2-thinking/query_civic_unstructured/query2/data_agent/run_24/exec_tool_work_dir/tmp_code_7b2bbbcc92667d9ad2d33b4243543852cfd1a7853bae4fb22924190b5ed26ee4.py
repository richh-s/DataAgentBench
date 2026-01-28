code = """import json
import re

# Load the civic documents data
civic_docs_path = '/tmp/tmpw8a01a0z.json'
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_path = '/tmp/tmptjtu3_1d.json'
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded {} civic documents and {} funding records'.format(len(civic_docs), len(funding_records)))

# Step 1: Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_stripped = line.strip()
        line_lower = line_stripped.lower()
        
        # Look for completion in 2022 and park-related
        if ('completed' in line_lower and '2022' in line_stripped and 
            'park' in line_lower and len(line_stripped) > 10):
            park_projects_2022.append(line_stripped)

print('Found {} lines mentioning park projects completed in 2022'.format(len(park_projects_2022)))

# Step 2: Identify specific project names from these lines
project_name_patterns = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets', 
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

identified_projects = []

for line in park_projects_2022:
    line_lower = line.lower()
    for pattern in project_name_patterns:
        if pattern.lower() in line_lower:
            identified_projects.append(pattern)

identified_projects = list(set(identified_projects))
print('Identified {} unique park projects completed in 2022'.format(len(identified_projects)))

# Step 3: Match with funding records and calculate total
funding_lookup = {}
for f in funding_records:
    funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])

total_funding = 0
funding_breakdown = []

for project_name in identified_projects:
    if project_name.lower() in funding_lookup:
        amount = funding_lookup[project_name.lower()]
        total_funding += amount
        funding_breakdown.append({'project': project_name, 'amount': amount})
        print('Found funding for {}: ${}'.format(project_name, amount))

# Step 4: Also check for other park projects in funding that might be completed in 2022
print('\nChecking for other park projects in funding records...')
additional_park_funding = 0
additional_projects = []

for f in funding_records:
    proj_name = f['Project_Name']
    # Check if it's a park project
    if 'park' in proj_name.lower():
        amount = int(f['Amount'])
        # Check if it wasn't already counted
        if proj_name not in identified_projects:
            # Look for this project in civic docs to see if completed in 2022
            for doc in civic_docs:
                text = doc.get('text', '').lower()
                if proj_name.lower() in text and 'completed' in text and '2022' in doc.get('text', ''):
                    additional_park_funding += amount
                    additional_projects.append(proj_name)
                    print('Additional park project completed in 2022: {} - ${}'.format(proj_name, amount))
                    break

total_funding += additional_park_funding

result = {
    'total_funding': total_funding,
    'primary_projects': funding_breakdown,
    'additional_projects': additional_projects,
    'additional_funding': additional_park_funding
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
