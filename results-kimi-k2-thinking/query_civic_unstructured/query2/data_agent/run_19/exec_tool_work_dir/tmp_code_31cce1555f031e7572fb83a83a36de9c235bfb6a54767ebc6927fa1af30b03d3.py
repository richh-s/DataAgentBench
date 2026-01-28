code = """import json
import re

# Load the datasets
funding_path = locals()['var_functions.query_db:0']
civic_path = locals()['var_functions.query_db:14']

funding_data = json.load(open(funding_path))
civic_data = json.load(open(civic_path))

# Define keywords
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'recreation']

# Extract park projects
park_projects = []
for rec in funding_data:
    name = rec.get('Project_Name', '')
    if any(kw in name.lower() for kw in park_keywords):
        park_projects.append({'name': name, 'amount': int(rec.get('Amount', 0))})

# Extract projects completed in 2022
completed_2022 = []
for doc in civic_data:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and '2022' in line and 'completed' in line.lower():
            # Look backwards for project name
            for j in range(max(0, i-15), i):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('(') and not prev.startswith('Page'):
                    completed_2022.append(prev)
                    break

# Match and sum funds
total = 0
matched = []

for park in park_projects:
    park_name = park['name'].lower()
    for comp in completed_2022:
        comp_name = comp.lower()
        
        # Matching logic
        match = False
        if park['name'] in comp or comp in park['name']:
            match = True
        else:
            # Word overlap (2+ words)
            park_words = [w for w in park_name.split() if len(w) > 3]
            comp_words = [w for w in comp_name.split() if len(w) > 3]
            if len(set(park_words) & set(comp_words)) >= 2:
                match = True
        
        if match:
            total += park['amount']
            matched.append(park['name'])
            break

# Deduplicate
unique_matched = list(set(matched))
final_total = sum(p['amount'] for p in park_projects if p['name'] in unique_matched)

result = {
    'total_2022_park_funding': final_total,
    'projects': len(unique_matched),
    'project_names': sorted(unique_matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}, 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
