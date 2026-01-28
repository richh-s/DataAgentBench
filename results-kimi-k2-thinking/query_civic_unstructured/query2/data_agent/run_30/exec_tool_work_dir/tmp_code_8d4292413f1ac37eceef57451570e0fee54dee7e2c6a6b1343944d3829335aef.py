code = """import json
import re

# Load full civic documents data
civic_docs_path = var_functions.query_db:20
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load full funding data
funding_path = var_functions.query_db:22
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_records)} funding records")

# Extract park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers and formatting
        skip_terms = ['Page', 'Agenda Item', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:']
        if any(term in line for term in skip_terms):
            continue
        if line.startswith(('(', '·', '-', '□', '•')):
            continue
            
        # Check if park-related
        lower_line = line.lower()
        if 'park' not in lower_line and 'playground' not in lower_line:
            continue
        
        # Look ahead for completion status in 2022
        project_name = line
        completed_2022 = False
        
        for j in range(i+1, min(i+10, len(lines))):
            next_line = lines[j].strip().lower()
            if ('completed' in next_line and '2022' in next_line) or ('completion' in next_line and '2022' in next_line):
                completed_2022 = True
                break
        
        if completed_2022:
            park_projects_2022.append(project_name)
            print(f"Found completed 2022 park project: {project_name}")

print(f"\nTotal park projects completed in 2022: {len(park_projects_2022)}")

# Match with funding records
total_funding = 0
matched_projects = []

for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects_2022:
        proj_name_lower = project.lower()
        
        # Check for match
        if proj_name_lower in fund_name or fund_name in proj_name_lower:
            total_funding += fund_amount
            matched_projects.append({
                'project': project,
                'funding_name': fund.get('Project_Name'),
                'amount': fund_amount,
                'source': fund.get('Funding_Source')
            })
            print(f"MATCH: {project} -> {fund.get('Project_Name')} = ${fund_amount}")
            break

print(f"\nMatched {len(matched_projects)} projects")
print(f"Total funding: ${total_funding}")

# Also check for direct matches in funding for park projects with 2022 in name
print("\n" + "="*50)
print("Checking for park projects with '2022' in funding names...")

for fund in funding_records:
    fund_name = fund.get('Project_Name', '').lower()
    if '2022' in fund_name and ('park' in fund_name or 'playground' in fund_name):
        fund_amount = int(fund.get('Amount', 0))
        print(f"Found 2022 park project in funding: {fund.get('Project_Name')} = ${fund_amount}")
        
        # Check if not already counted
        already_counted = False
        for matched in matched_projects:
            if matched['funding_name'] == fund.get('Project_Name'):
                already_counted = True
                break
        
        if not already_counted:
            total_funding += fund_amount
            print(f"  -> Added: ${fund_amount}")

print(f"\nFinal total funding for park projects completed in 2022: ${total_funding}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
