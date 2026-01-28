code = """import json, re

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:38']))
funding = json.load(open(locals()['var_functions.query_db:30']))

print('Loaded', len(civic_docs), 'documents and', len(funding), 'funding records')

# Find park projects completed in 2022
park_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10: continue
        
        # Skip headers
        if any(x in line for x in ['Page', 'Agenda', 'Public Works']): continue
        if line and line[0] in ['(', '·', '-', '□']: continue
            
        # Check for park projects
        if 'park' not in line.lower() and 'playground' not in line.lower(): continue
        
        # Look for 2022 completion
        completed = False
        for j in range(i+1, min(i+12, len(lines))):
            if 'completed' in lines[j].lower() and '2022' in lines[j].lower():
                completed = True
                break
        
        if completed:
            park_projects.append(line)
            print('Found:', line)

# Calculate funding
total = 0
for fund in funding:
    f_name = fund.get('Project_Name', '').lower()
    for proj in park_projects:
        if proj.lower() in f_name or f_name in proj.lower():
            total += int(fund.get('Amount', 0))
            print('Matched:', proj, '->', fund.get('Project_Name'))
            break

print('\nTotal funding for park projects completed in 2022:', total)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
