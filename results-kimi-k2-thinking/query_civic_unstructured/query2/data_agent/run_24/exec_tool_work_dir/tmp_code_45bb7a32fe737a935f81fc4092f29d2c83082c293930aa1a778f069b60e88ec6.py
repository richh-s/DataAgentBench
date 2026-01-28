code = """import json
import re

# Load civic documents from the file path
civic_docs_file = locals()['var_functions.query_db:72']
funding_file = locals()['var_functions.query_db:73']

# Read the JSON data
civic_docs = []
funding = []

with open(civic_docs_file, 'r') as f:
    content = f.read()
    civic_docs = json.loads(content)

with open(funding_file, 'r') as f:
    content = f.read()
    funding = json.loads(content)

print('Loaded %d civic documents' % len(civic_docs))
print('Loaded %d funding records' % len(funding))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        # Look for park projects with completion in 2022
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            cleaned = line.strip()
            if len(cleaned) > 10:
                park_projects_2022.append(cleaned)

print('Found %d park project completions in 2022' % len(park_projects_2022))

# Extract specific project names from the found lines
project_names = []
for line in park_projects_2022:
    if 'bluffs park' in line.lower():
        project_names.append('Bluffs Park Shade Structure')
    elif 'broad beach' in line.lower():
        project_names.append('Broad Beach Road Water Quality Repair')
    elif 'point dume' in line.lower():
        project_names.append('Point Dume Walkway Repairs')

project_names = list(set(project_names))
print('Identified projects: %s' % project_names)

# Match with funding records
funding_dict = {}
for rec in funding:
    funding_dict[rec['Project_Name'].lower()] = int(rec['Amount'])

total_funding = 0
matched_projects = []

for proj in project_names:
    proj_lower = proj.lower()
    if proj_lower in funding_dict:
        amount = funding_dict[proj_lower]
        total_funding += amount
        matched_projects.append({'project': proj, 'amount': amount})
        print('Found funding: %s - $%d' % (proj, amount))

# Also check for partial matches in funding records
for rec in funding:
    name = rec['Project_Name'].lower()
    for proj in project_names:
        proj_lower = proj.lower()
        if proj_lower in name and name not in [f['Project_Name'].lower() for f in matched_projects]:
            amount = int(rec['Amount'])
            total_funding += amount
            matched_projects.append({'project': proj, 'amount': amount, 'source': rec['Project_Name']})
            print('Partial match: %s ($%d)' % (rec['Project_Name'], amount))
            break

# Remove duplicates
final_projects = {}
for proj in matched_projects:
    name = proj['project']
    if name not in final_projects:
        final_projects[name] = proj['amount']

result = {
    'total_funding': sum(final_projects.values()),
    'projects': [{'name': k, 'amount': v} for k, v in final_projects.items()],
    'count': len(final_projects)
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
