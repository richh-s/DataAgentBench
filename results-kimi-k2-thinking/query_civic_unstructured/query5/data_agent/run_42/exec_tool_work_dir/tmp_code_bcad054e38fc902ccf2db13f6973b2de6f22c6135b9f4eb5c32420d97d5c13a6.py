code = """import json
import os
import re

# Load data
with open(locals()['var_functions.query_db:12']) as f:
    funding = json.load(f)

with open(locals()['var_functions.query_db:14']) as f:
    civic_docs = json.load(f)

# Extract disaster projects that started in 2022 from civic docs
# Pattern 1: Projects with 2022 in their name followed by keywords
disaster_2022_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line and '2022' in line and len(line) < 150:
            # Check if it's a project name
            if any(kw in line for kw in ['Project', 'Improvements', 'Repairs', 'System', 'Drain']):
                # Confirm disaster-related
                is_disaster = 'FEMA' in line or 'CalOES' in line
                if not is_disaster:
                    # Check surrounding lines
                    snippet = '\n'.join(lines[max(0,i-2):min(len(lines),i+10)]).lower()
                    if any(kw in snippet for kw in ['fema', 'caloes', 'caljpia', 'disaster', 'fire']):
                        is_disaster = True
                
                if is_disaster:
                    disaster_2022_projects.append(line)
        i += 1

# Clean duplicates
seen = set()
clean_projects = []
for p in disaster_2022_projects:
    if p not in seen:
        seen.add(p)
        clean_projects.append(p)

print('Disaster projects starting 2022:', clean_projects)

# Match with funding and sum amounts
matched = []
for proj in clean_projects:
    proj_lower = proj.lower()
    for rec in funding:
        fund_name = rec['Project_Name'].lower()
        if any(kw in fund_name for kw in ['fema', 'caloes', 'caljpia']) and proj_lower.split()[0] in fund_name:
            matched.append(int(rec['Amount']))
            break

print('Total funding:', sum(matched))
print('Matched records:', len(matched))

print('__RESULT__:')
print(json.dumps({'total_funding': sum(matched)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'success': True, 'num_docs': 5}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'funding_total': 500, 'civic_docs_total': 5, 'disaster_funding_count': 27}}

exec(code, env_args)
