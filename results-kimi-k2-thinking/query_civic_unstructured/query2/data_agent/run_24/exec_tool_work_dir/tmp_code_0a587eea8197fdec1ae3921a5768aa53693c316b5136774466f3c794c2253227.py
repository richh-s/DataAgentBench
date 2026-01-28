code = """import json
import re

# Load data from the files
civic_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding_records = json.load(open('/tmp/tmptjtu3_1d.json'))

print('Loaded data successfully')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Find park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower().strip()
        # Check for park projects completed in 2022
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line) > 10:
                park_projects_2022.append(line.strip())

print('Found {} park projects completed in 2022'.format(len(park_projects_2022)))

# Extract project names from the found lines
project_names = []
for proj_line in park_projects_2022:
    # Common park project names in the data
    proj_lower = proj_line.lower()
    
    if 'bluffs park shade structure' in proj_lower:
        project_names.append('Bluffs Park Shade Structure')
    elif 'marie canyon green streets' in proj_lower:
        project_names.append('Marie Canyon Green Streets')  
    elif 'broad beach road water quality repair' in proj_lower:
        project_names.append('Broad Beach Road Water Quality Repair')
    elif 'point dume walkway repairs' in proj_lower:
        project_names.append('Point Dume Walkway Repairs')
    elif 'bluffs park' in proj_lower and 'shade' in proj_lower:
        project_names.append('Bluffs Park Shade Structure')
    elif 'marie canyon' in proj_lower:
        project_names.append('Marie Canyon Green Streets')
    elif 'broad beach' in proj_lower and 'water quality' in proj_lower:
        project_names.append('Broad Beach Road Water Quality Repair')
    elif 'point dume' in proj_lower:
        project_names.append('Point Dume Walkway Repairs')

# Remove duplicates
project_names = list(set(project_names))
print('Extracted {} unique project names'.format(len(project_names)))

# Create funding lookup dictionary
funding_lookup = {}
for f in funding_records:
    funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])

# Calculate total funding
total_funding = 0
matched = []

for name in project_names:
    name_lower = name.lower()
    if name_lower in funding_lookup:
        amount = funding_lookup[name_lower]
        total_funding += amount
        matched.append({'name': name, 'amount': amount})

result = {
    'total_funding': total_funding,
    'matched_projects': matched,
    'project_count': len(project_names)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
