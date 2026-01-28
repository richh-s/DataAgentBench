code = """import json, re

# Get the file paths from storage
civic_docs_file = locals()['var_functions.query_db:20']
funding_file = locals()['var_functions.query_db:30']

# Load data
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

with open(funding_file) as f:
    funding_records = json.load(f)

print('Loaded civic docs:', len(civic_docs), 'funding records:', len(funding_records))

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
        if line and line[0] in ['(', '·', '-', '□', '•']:
            continue
            
        # Check for park-related projects
        lower_line = line.lower()
        if 'park' not in lower_line and 'playground' not in lower_line:
            continue
        
        # Look for completion in 2022
        completed_2022 = False
        for j in range(i+1, min(i+12, len(lines))):
            next_line = lines[j].strip().lower()
            if 'completed' in next_line and '2022' in next_line:
                completed_2022 = True
                break
        
        if completed_2022:
            park_projects.append(line)
            print('Found park project completed 2022:', line)

# Match with funding records
total_funding = 0
matched_count = 0

for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects:
        proj_lower = project.lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            total_funding += fund_amount
            matched_count += 1
            print('Matched:', project, '->', fund.get('Project_Name'), '=', fund_amount)
            break

print('\nMatched projects:', matched_count)
print('Total funding for park projects completed in 2022:', total_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
