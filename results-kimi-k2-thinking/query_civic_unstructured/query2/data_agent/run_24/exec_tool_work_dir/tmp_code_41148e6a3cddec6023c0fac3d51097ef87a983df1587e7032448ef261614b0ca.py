code = """import json
import re

# Load civic documents
civic_docs_path = '/tmp/tmpw8a01a0z.json'
funding_path = '/tmp/tmptjtu3_1d.json'

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Data loaded successfully')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Parse projects from civic documents
found_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower().strip()
        # Look for park projects with 2022 completion
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line) > 10:  # Skip very short lines
                found_projects.append(line.strip())

print('Found {} potential park projects completed in 2022'.format(len(found_projects)))

# Show samples
for i, proj in enumerate(found_projects[:5]):
    print('Sample:', i, proj[:80])

# Now match with funding records
# First, create a dictionary of project names from civic docs that are park-related and completed in 2022
civic_project_names = []

for proj_line in found_projects:
    # Try to extract project name from line
    # Common patterns: "Project Name - completed" or "Completed: Project Name"
    line = proj_line.lower()
    
    # Look for specific park names
    if 'bluffs park' in line:
        civic_project_names.append('Bluffs Park Shade Structure')
    elif 'marie canyon' in line:
        civic_project_names.append('Marie Canyon Green Streets')
    elif 'broad beach' in line:
        civic_project_names.append('Broad Beach Road Water Quality Repair')
    elif 'point dume' in line:
        civic_project_names.append('Point Dume Walkway Repairs')

print('Extracted project names:', len(civic_project_names))

# Match with funding and calculate total
funding_dict = {}
for f in funding_records:
    funding_dict[f['Project_Name'].lower()] = int(f['Amount'])

total_funding = 0
matched_projects = []

for name in civic_project_names:
    name_lower = name.lower()
    if name_lower in funding_dict:
        amount = funding_dict[name_lower]
        total_funding += amount
        matched_projects.append({'name': name, 'amount': amount})
        print('Matched: {} - ${}'.format(name, amount))

result = {
    'total_funding': total_funding,
    'matched_projects': matched_projects,
    'civic_project_count': len(civic_project_names)
}

__RESULT__:
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
