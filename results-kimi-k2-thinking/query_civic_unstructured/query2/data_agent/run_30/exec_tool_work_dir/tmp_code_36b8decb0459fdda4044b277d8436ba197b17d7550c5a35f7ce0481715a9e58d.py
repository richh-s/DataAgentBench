code = """import json, re

# Load civic documents data
civic_docs_path = locals()['var_functions.query_db:20']
with open(civic_docs_path) as f:
    civic_docs = json.load(f)

# Load funding data
funding_path = locals()['var_functions.query_db:30']
with open(funding_path) as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')
print('Loaded', len(funding_records), 'funding records')

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if len(line) < 10:
            continue
        
        # Skip headers and formatting lines
        skip_terms = ['Page', 'Agenda', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:']
        should_skip = False
        for term in skip_terms:
            if term in line:
                should_skip = True
                break
        if should_skip:
            continue
        
        # Skip lines starting with common bullet characters
        if line and (line[0] == '(' or line[0] == '-'):
            continue
            
        # Check if this is a park-related project
        line_lower = line.lower()
        if 'park' not in line_lower and 'playground' not in line_lower:
            continue
        
        # Look ahead for completion status in 2022
        found_completion = False
        for j in range(i+1, min(i+15, len(lines))):
            next_line = lines[j].strip().lower()
            if 'completed' in next_line and '2022' in next_line:
                found_completion = True
                break
        
        if found_completion:
            park_projects_2022.append(line)
            print('Found completed park project:', line)

print('\nTotal park projects completed in 2022:', len(park_projects_2022))

# Match with funding records and calculate total funding
total_funding = 0
matched_projects = []

for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects_2022:
        project_lower = project.lower()
        # Check if project names match
        if project_lower in fund_name or fund_name in project_lower:
            total_funding += fund_amount
            matched_projects.append({
                'project': project,
                'funding_name': fund.get('Project_Name'),
                'amount': fund_amount,
                'source': fund.get('Funding_Source')
            })
            print('Matched:', project, '->', fund.get('Project_Name'), '$' + str(fund_amount))
            break

print('\nTotal matched projects:', len(matched_projects))
print('Total funding for park projects completed in 2022: $' + str(total_funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
