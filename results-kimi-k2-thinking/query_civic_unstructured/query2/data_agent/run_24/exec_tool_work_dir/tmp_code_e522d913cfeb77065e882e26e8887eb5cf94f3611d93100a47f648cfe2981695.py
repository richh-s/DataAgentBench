code = """import json
import re

# Access the stored results using locals()
civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:8']

# Load the data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_records)))

# Look for park projects completed in 2022 in civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        # Check for completed park projects with 2022 date
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line.strip()) > 10:
                park_projects_2022.append(line.strip())

print('Found %d park projects completed in 2022 mentions' % len(park_projects_2022))

# Identify specific projects with known names
known_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets',
    'Broad Beach Road Water Quality Repair', 
    'Point Dume Walkway Repairs'
]

found_project_names = []
for line in park_projects_2022:
    line_lower = line.lower()
    for proj in known_projects:
        if proj.lower() in line_lower:
            found_project_names.append(proj)

found_project_names = list(set(found_project_names))
print('Identified %d specific projects' % len(found_project_names))

# Match with funding records
total_funding = 0
matched = []

funding_lookup = {}
for f in funding_records:
    funding_lookup[f['Project_Name'].lower()] = int(f['Amount'])

for proj_name in found_project_names:
    if proj_name.lower() in funding_lookup:
        amount = funding_lookup[proj_name.lower()]
        total_funding += amount
        matched.append({'name': proj_name, 'amount': amount})
        print('Matched: %s - $%d' % (proj_name, amount))

# Also check funding records directly for park projects that might be completed in 2022
for f in funding_records:
    proj_name = f['Project_Name']
    if 'park' in proj_name.lower():
        # Check if mentioned in civic docs with 2022 completion
        for doc in civic_docs:
            text = doc.get('text', '')
            if proj_name.lower() in text.lower() and 'completed' in text.lower() and '2022' in text:
                if proj_name not in [m['name'] for m in matched]:
                    amount = int(f['Amount'])
                    total_funding += amount
                    matched.append({'name': proj_name, 'amount': amount})
                    print('Additional: %s - $%d' % (proj_name, amount))
                break

result = {'total_funding': total_funding, 'matched_projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
