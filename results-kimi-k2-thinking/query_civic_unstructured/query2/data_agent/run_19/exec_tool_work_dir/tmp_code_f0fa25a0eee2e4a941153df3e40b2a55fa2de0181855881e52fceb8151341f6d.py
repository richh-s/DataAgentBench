code = """import json
import re

# Load funding data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    funding = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:14'], 'r') as f:
    docs = json.load(f)

# Find all park-related projects completed in 2022
total_funding = 0
matched_projects = []

# Define park keywords
park_kw = ['park', 'bluffs', 'playground', 'arbors', 'recreation']

# Step 1: Find park projects in funding data
park_funding = []
for rec in funding:
    name = rec.get('Project_Name', '')
    if any(kw in name.lower() for kw in park_kw):
        park_funding.append({
            'name': name,
            'amount': int(rec.get('Amount', 0))
        })

# Step 2: Parse civic docs for projects completed in 2022
completed_2022 = []
for doc in docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look for project name before this line
            for j in range(max(0, i-15), i):
                prev = lines[j].strip()
                if prev and len(prev) > 8 and not prev.startswith('(') and not prev.startswith('Page'):
                    completed_2022.append(prev)
                    break

# Step 3: Check for explicit project mentions
for doc in docs:
    text = doc.get('text', '').lower()
    
    if 'bluffs park shade structure' in text and 'november 2022' in text and 'completed' in text:
        completed_2022.append('Bluffs Park Shade Structure')
    
    if 'construction was completed' in text and 'november 2022' in text:
        if 'bluffs park' in text:
            completed_2022.append('Bluffs Park Shade Structure')

# Step 4: Match and sum
for park in park_funding:
    for comp in completed_2022:
        # Check for name matching
        p_name = park['name'].lower()
        c_name = comp.lower()
        
        if (park['name'] in comp or comp in park['name'] or 
            any(word in c_name for word in p_name.split() if len(word) > 4)):
            total_funding += park['amount']
            matched_projects.append(park['name'])
            break

# Step 5: Deduplicate
unique_projects = list(set(matched_projects))
final_total = sum(p['amount'] for p in park_funding if p['name'] in unique_projects)

print('__RESULT__:')
print(json.dumps({
    'total_funding': final_total,
    'project_count': len(unique_projects),
    'projects': sorted(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}, 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
