code = """import json, re

# Read file paths from the stored variables
civic_docs_path = locals()['var_functions.query_db:20']
funding_path = locals()['var_functions.query_db:22']

# Load data
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'documents and', len(funding_records), 'funding records')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        
        # Skip headers and formatting
        skip_terms = ['Page', 'Agenda', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:']
        if any(term in line for term in skip_terms):
            continue
        if line and line[0] in ['(', '·', '-', '□']:
            continue
            
        # Check for park-related projects
        if 'park' not in line.lower() and 'playground' not in line.lower():
            continue
        
        # Check for 2022 completion in following lines
        completed_2022 = False
        for j in range(i+1, min(i+12, len(lines))):
            next_line = lines[j].strip().lower()
            if 'completed' in next_line and '2022' in next_line:
                completed_2022 = True
                break
        
        if completed_2022:
            park_projects.append(line)
            print('Found park project:', line)

print('\nTotal park projects completed in 2022:', len(park_projects))

# Calculate total funding
projects_with_funding = []
total_funding = 0

for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects:
        project_lower = project.lower()
        if project_lower in fund_name or fund_name in project_lower:
            projects_with_funding.append({
                'project': project,
                'funding_record': fund.get('Project_Name'),
                'amount': fund_amount
            })
            total_funding += fund_amount
            print('Match found:', project, '->', fund.get('Project_Name'), '$' + str(fund_amount))
            break

print('\nProjects matched with funding:', len(projects_with_funding))
print('Total funding amount: $' + str(total_funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
