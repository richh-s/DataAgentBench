code = """import json
import re

# Load data
funding_data = json.load(open(locals()['var_functions.query_db:0']))
civic_data = json.load(open(locals()['var_functions.query_db:14']))

# Park keywords
park_kw = ['park', 'bluffs', 'playground', 'arbors', 'recreation', 'walkway']

# Get park projects from funding
def get_park_projects(funding):
    parks = []
    for rec in funding:
        name = rec.get('Project_Name', '')
        if any(kw in name.lower() for kw in park_kw):
            parks.append({'name': name, 'amount': int(rec.get('Amount', 0))})
    return parks

# Get projects completed in 2022 from civic docs
def get_completed_2022(docs):
    completed = []
    for doc in docs:
        t = doc.get('text', '')
        if '2022' not in t:
            continue
        lines = t.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if '2022' in line and 'completed' in line.lower():
                # Find project name
                for j in range(max(0, i-15), i):
                    prev = lines[j].strip()
                    if prev and len(prev) > 10 and not prev.startswith('(') and not prev.startswith('Page'):
                        completed.append(prev)
                        break
    return completed

# Main matching logic
park_projects = get_park_projects(funding_data)
completed_projects = get_completed_2022(civic_data)

total = 0
matched = []

for park in park_projects:
    for completed in completed_projects:
        p_name = park['name'].lower()
        c_name = completed.lower()
        
        # Check for substring match or at least 2 matching keywords
        if p_name in c_name or c_name in p_name:
            total += park['amount']
            matched.append(park['name'])
            break
        else:
            # Check word overlap
            p_words = set([w for w in p_name.split() if len(w) > 3])
            c_words = set([w for w in c_name.split() if len(w) > 3])
            intersect = p_words.intersection(c_words)
            if len(intersect) >= 2:
                total += park['amount']
                matched.append(park['name'])
                break

# Also check for explicit mentions
for doc in civic_data:
    t = doc.get('text', '').lower()
    if 'bluffs park shade structure' in t and '2022' in t:
        completed_projects.append('Bluffs Park Shade Structure')

# Recalculate with explicit projects
final_total = 0
final_matched = list(set(matched))
for park in park_projects:
    if park['name'] in final_matched:
        final_total += park['amount']

result = {'total_funding': final_total, 'projects': len(final_matched), 'names': sorted(final_matched)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'status': 'inspection_complete'}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}]}, 'var_functions.execute_python:38': {'total_park_funding_2022': 105000, 'projects': 1, 'names': ['Bluffs Park Shade Structure']}, 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json'}

exec(code, env_args)
