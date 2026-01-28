code = """import json
import re

# Load data
funding = json.load(open(locals()['var_functions.query_db:0']))
civic = json.load(open(locals()['var_functions.query_db:14']))

# Define park keywords
park_keywords = ['park', 'bluffs', 'playground', 'arbors', 'recreation', 'walkway']

# Get park projects
park_projects = []
for rec in funding:
    name = rec.get('Project_Name', '')
    if any(kw in name.lower() for kw in park_keywords):
        park_projects.append({'name': name, 'amount': int(rec.get('Amount', 0))})

# Find completions in 2022
completed_2022 = []
for doc in civic:
    t = doc.get('text', '')
    lines = t.split('\n')
    for i, line in enumerate(lines):
        if '2022' in line and 'completed' in line.lower():
            for j in range(max(0, i-15), i):
                prev = lines[j].strip()
                if prev and len(prev) > 10 and not prev.startswith('('):
                    completed_2022.append(prev)
                    break

# Match and calculate
total = 0
matched = []

for p in park_projects:
    for c in completed_2022:
        if p['name'].lower() in c.lower() or c.lower() in p['name'].lower():
            total += p['amount']
            matched.append(p['name'])
            break

unique_matched = list(set(matched))
final_total = sum(p['amount'] for p in park_projects if p['name'] in unique_matched)

print('__RESULT__:')
print(json.dumps({'total': final_total, 'count': len(unique_matched), 'projects': sorted(unique_matched)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}, 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
