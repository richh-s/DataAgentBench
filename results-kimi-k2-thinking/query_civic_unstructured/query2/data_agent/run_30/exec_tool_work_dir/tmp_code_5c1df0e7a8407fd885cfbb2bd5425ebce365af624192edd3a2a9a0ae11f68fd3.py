code = """import json, re

# Load data from files
civic_docs_path = var_functions.query_db:20
funding_path = var_functions.query_db:22

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding_records), 'funding records')

# Extract park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        skip_terms = ['Page', 'Agenda', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:']
        if any(term in line for term in skip_terms):
            continue
        if line and line[0] in ['(', '·', '-', '□', '•']:
            continue
            
        # Check for park in line
        if 'park' not in line.lower() and 'playground' not in line.lower():
            continue
        
        # Look for 2022 completion
        completed = False
        for j in range(i+1, min(i+10, len(lines))):
            next_line = lines[j].strip().lower()
            if ('completed' in next_line and '2022' in next_line):
                completed = True
                break
        
        if completed:
            park_projects.append(line)
            print('Found park project:', line)

print('\nPark projects completed in 2022:', len(park_projects))

# Match with funding
total_funding = 0
for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects:
        proj_lower = project.lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            total_funding += fund_amount
            print('Match:', project, '->', fund.get('Project_Name'), '=', fund_amount)
            break

print('\nTotal funding:', total_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
