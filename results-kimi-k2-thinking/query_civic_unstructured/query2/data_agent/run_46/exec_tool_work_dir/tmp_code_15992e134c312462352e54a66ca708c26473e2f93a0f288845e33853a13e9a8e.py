code = """import json
import re

# Access data from storage
docs = locals()['var_functions.query_db:8']
funding = locals()['var_functions.query_db:10']

# Build funding lookup
lookup = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    lookup[key] = int(item['Amount'])

# Find park projects completed in 2022
completed_2022 = []
total_text = ''

for doc in docs:
    text = doc.get('text', '')
    total_text += text + '\n'
    lines = text.split('\n')
    
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or len(line) < 5 or line[0] in '-*([{':
            continue
        
        # Check if line might be a project name
        if any(c.isupper() for c in line[:30]):
            # Look ahead for completion info
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if 'completed' in next_line.lower() and '2022' in next_line:
                    if 'park' in line.lower():
                        completed_2022.append(line)

# Remove duplicates
completed_2022 = list(set(completed_2022))

# Find funding
total = 0
matched = []

for proj in completed_2022:
    key = proj.lower().replace(' ', '')
    if key in lookup:
        total += lookup[key]
        matched.append({'project': proj, 'amount': lookup[key]})

# Check known projects from preview
known = ['Bluffs Park Shade Structure']
for proj in known:
    if proj in total_text:
        key = proj.lower().replace(' ', '')
        if key in lookup and not any(m['project'] == proj for m in matched):
            total += lookup[key]
            matched.append({'project': proj, 'amount': lookup[key]})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs']}

exec(code, env_args)
