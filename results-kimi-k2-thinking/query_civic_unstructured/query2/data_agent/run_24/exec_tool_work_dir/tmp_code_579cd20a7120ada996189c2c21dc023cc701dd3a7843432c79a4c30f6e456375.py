code = """import json
import re

# Load from the stored file paths
with open('/tmp/tmpw8a01a0z.json', 'r') as f:
    civic_docs = json.load(f)

with open('/tmp/tmptjtu3_1d.json', 'r') as f:
    funding_records = json.load(f)

print('Loaded data')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Find park projects completed in 2022
projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line_lower = line.lower().strip()
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower:
            if len(line.strip()) > 10:
                projects_2022.append(line.strip())

print('Found', len(projects_2022), 'park projects completed in 2022')

# Sample of what was found
for i, proj in enumerate(projects_2022[:3]):
    print('Sample', i, proj[:80])

# Calculate total funding for these projects
funding_dict = {f['Project_Name'].lower(): int(f['Amount']) for f in funding_records}

# Target park projects that appear to be completed in 2022 based on the sample text
targets = ['Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs']

total_funding = 0
matched_projects = []

for target in targets:
    if target.lower() in funding_dict:
        amount = funding_dict[target.lower()]
        total_funding += amount
        matched_projects.append({'name': target, 'amount': amount})

result = {'total_funding': total_funding, 'projects': matched_projects, 'found_docs': len(projects_2022)}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
