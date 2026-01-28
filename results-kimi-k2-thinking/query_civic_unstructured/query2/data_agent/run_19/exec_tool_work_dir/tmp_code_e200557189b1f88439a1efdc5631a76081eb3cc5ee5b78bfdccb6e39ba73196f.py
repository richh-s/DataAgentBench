code = """import json
import re

# Load funding data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    funding = json.load(f)

# Load civic docs
with open(locals()['var_functions.query_db:14'], 'r') as f:
    docs = json.load(f)

# Find park projects completed in 2022
park_names = []
for doc in docs:
    t = doc.get('text', '')
    lines = t.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-8), i):
                prev = lines[j].strip()
                if prev and not prev.startswith('('):
                    park_names.append(prev)
                    break

# Match with funding
total = 0
matched_projects = []
park_keywords = ['park', 'bluffs', 'playground', 'arbors']

for record in funding:
    name = record.get('Project_Name', '')
    amt = int(record.get('Amount', 0))
    
    # Check if park project
    is_park = any(kw in name.lower() for kw in park_keywords)
    if not is_park:
        continue
    
    # Check if completed in 2022
    for comp in park_names:
        if name in comp or comp in name:
            total += amt
            matched_projects.append(name)
            break

print('__RESULT__:')
print(json.dumps({'funding': total, 'projects': len(matched_projects), 'project_list': matched_projects[:5]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}}

exec(code, env_args)
