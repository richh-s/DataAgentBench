code = """import json
import re

f_path = locals()['var_functions.query_db:0']
c_path = locals()['var_functions.query_db:14']

with open(f_path, 'r') as f:
    funding = json.load(f)

with open(c_path, 'r') as f:
    docs = json.load(f)

# Step 1: Find park-related funding projects
park_projects = []
for frec in funding:
    pname = frec.get('Project_Name', '')
    if 'park' in pname.lower() or 'bluffs' in pname.lower() or 'playground' in pname.lower():
        park_projects.append({'name': pname, 'amount': int(frec.get('Amount', 0))})

# Step 2: Parse text for projects completed in 2022
completed_2022 = []
for doc in docs:
    t = doc.get('text', '')
    lines = t.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-10), i):
                prev = lines[j].strip()
                if prev and len(prev) > 5 and not prev.startswith('(') and not prev.startswith('—'):
                    completed_2022.append(prev)
                    break

# Step 3: Find matches
total_funding = 0
matched = []
for pproj in park_projects:
    for comp in completed_2022:
        pname = pproj['name']
        # Check if names match
        if pname.lower() in comp.lower() or comp.lower() in pname.lower():
            total_funding += pproj['amount']
            matched.append(pname)
            break

# Step 4: Check for explicit mentions
bluffs_found = False
broad_found = False
point_found = False

for doc in docs:
    t = doc.get('text', '').lower()
    if 'bluffs park shade structure' in t and '2022' in t:
        bluffs_found = True
    if 'broad beach road water quality repair' in t and '2022' in t:
        broad_found = True
    if 'point dume walkway repairs' in t and '2022' in t:
        point_found = True

if bluffs_found:
    for pproj in park_projects:
        if 'Bluffs Park Shade Structure' in pproj['name'] and pproj['name'] not in matched:
            total_funding += pproj['amount']
            matched.append(pproj['name'])

if broad_found:
    for pproj in park_projects:
        if 'Broad Beach Road Water Quality Repair' in pproj['name'] and pproj['name'] not in matched:
            total_funding += pproj['amount']
            matched.append(pproj['name'])

if point_found:
    for pproj in park_projects:
        if 'Point Dume Walkway Repairs' in pproj['name'] and pproj['name'] not in matched:
            total_funding += pproj['amount']
            matched.append(pproj['name'])

# Deduplicate and calculate
unique_matched = list(set(matched))
final_total = 0
for project_name in unique_matched:
    for pproj in park_projects:
        if pproj['name'] == project_name:
            final_total += pproj['amount']
            break

print('__RESULT__:')
print(json.dumps({'total_funding': final_total, 'projects': len(unique_matched), 'project_names': unique_matched}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
