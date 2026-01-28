code = """import json
import re

# Load data from storage variables
docs = var_functions.query_db:8
funding = var_functions.query_db:10

# Build funding lookup
funding_lookup = {}
for item in funding:
    key = item['Project_Name'].lower().replace(' ', '')
    funding_lookup[key] = int(item['Amount'])

# Parse documents for park projects completed in 2022
park_projects = []

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)-1):
        line = lines[i].strip()
        if not line or 'Page' in line or '---' in line:
            continue
        
        # Look for project name patterns
        if len(line) > 10 and not line[0] in '-*(' and 'PROJECTS' not in line.upper():
            next_line = lines[i+1].strip()
            
            # Check for completion in 2022
            if 'completed' in next_line.lower() and '2022' in next_line:
                # Check if park-related
                if 'park' in line.lower() or ('shade' in line.lower() and 'structure' in line.lower()):
                    park_projects.append(line)

# Get funding for these projects
total = 0
matched = []

for proj in park_projects:
    proj_key = proj.lower().replace(' ', '')
    if proj_key in funding_lookup:
        amount = funding_lookup[proj_key]
        total += amount
        matched.append({'project': proj, 'amount': amount})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
