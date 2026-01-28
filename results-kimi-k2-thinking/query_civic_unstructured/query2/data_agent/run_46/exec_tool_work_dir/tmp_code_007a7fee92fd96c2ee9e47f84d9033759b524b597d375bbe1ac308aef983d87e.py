code = """import json
import re

docs = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

lookup = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    lookup[key] = int(item['Amount'])

# Find park projects completed in 2022
park_projects = []
for doc in docs:
    text = doc.get('text', '')
    # Look for project names and completion dates
    if 'completed' in text.lower() and '2022' in text:
        # Extract relevant sections
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) > 5 and not line[0] in '-*(':
                # Check if this might be a park project
                lower_line = line.lower()
                if 'park' in lower_line or 'bluffs' in lower_line:
                    # Look ahead for completion in 2022
                    for j in range(i+1, min(i+10, len(lines))):
                        next_line = lines[j].strip().lower()
                        if 'completed' in next_line and '2022' in next_line:
                            park_projects.append(line)
                            break

# Remove duplicates
park_projects = list(set(park_projects))

# Match with funding
total = 0
matched = []
for proj in park_projects:
    key = proj.lower().replace(' ', '')
    if key in lookup:
        total += lookup[key]
        matched.append({'project': proj, 'amount': lookup[key]})

# Check for known completed projects
known = ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs']
for proj in known:
    all_text = ' '.join([d.get('text', '') for d in docs])
    if proj in all_text and '2022' in all_text:
        key = proj.lower().replace(' ', '')
        if key in lookup:
            # Check not already matched
            if not any(m.get('project') == proj for m in matched):
                total += lookup[key]
                matched.append({'project': proj, 'amount': lookup[key]})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
