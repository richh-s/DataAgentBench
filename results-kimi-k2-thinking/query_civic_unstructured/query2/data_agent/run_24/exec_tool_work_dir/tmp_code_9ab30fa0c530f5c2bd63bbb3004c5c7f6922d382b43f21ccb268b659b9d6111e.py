code = """import json
import re

# Load data from the stored file paths
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:8

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d civic documents and %d funding records' % (len(civic_docs), len(funding_records)))

# Find park projects completed in 2022
park_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line.strip()) > 10:
                park_2022_projects.append(line.strip())

print('Found %d park projects completed in 2022' % len(park_2022_projects))

# Look for specific project names mentioned
specific_projects = []
for proj_line in park_2022_projects:
    proj_lower = proj_line.lower()
    if 'bluffs park shade structure' in proj_lower:
        specific_projects.append('Bluffs Park Shade Structure')
    elif 'marie canyon green streets' in proj_lower:
        specific_projects.append('Marie Canyon Green Streets')
    elif 'broad beach road water quality repair' in proj_lower:
        specific_projects.append('Broad Beach Road Water Quality Repair')
    elif 'point dume walkway repairs' in proj_lower:
        specific_projects.append('Point Dume Walkway Repairs')

specific_projects = list(set(specific_projects))
print('Specific projects identified: %d' % len(specific_projects))

# Match with funding records
funding_dict = {}
for f in funding_records:
    funding_dict[f['Project_Name'].lower()] = int(f['Amount'])

total_funding = 0
matched_projects = []

for proj_name in specific_projects:
    if proj_name.lower() in funding_dict:
        amount = funding_dict[proj_name.lower()]
        total_funding += amount
        matched_projects.append({'name': proj_name, 'amount': amount})
        print('Found: %s - $%d' % (proj_name, amount))

# Also search more broadly in funding for park projects
for f in funding_records:
    proj_name = f['Project_Name']
    if 'park' in proj_name.lower():
        # Look for 2022 completion mention in civic docs
        for doc in civic_docs:
            text = doc.get('text', '')
            if proj_name.lower() in text.lower() and 'completed' in text.lower() and '2022' in text:
                amount = int(f['Amount'])
                if proj_name not in [p['name'] for p in matched_projects]:
                    total_funding += amount
                    matched_projects.append({'name': proj_name, 'amount': amount})
                    print('Additional: %s - $%d' % (proj_name, amount))
                break

result = {'total_funding': total_funding, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
