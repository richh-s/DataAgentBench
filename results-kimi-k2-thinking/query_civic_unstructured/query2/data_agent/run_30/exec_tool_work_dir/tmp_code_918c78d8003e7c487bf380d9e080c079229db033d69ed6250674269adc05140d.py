code = """import json
import re

# Load the full data from the files
civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:5

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Find park-related projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers and bullet points
        if any(h in line for h in ['Page', 'Agenda Item', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:', 'Project Schedule', 'Recommended Action']):
            continue
        if line.startswith(('(', '•', '-', '□', 'cid:')):
            continue
            
        # Check if this line could be a project name (contains park-related terms)
        lower_line = line.lower()
        if not ('park' in lower_line or 'playground' in lower_line):
            continue
            
        # Look ahead for completion status in 2022
        project_name = line
        status = None
        
        for j in range(i+1, min(i+15, len(lines))):
            next_line = lines[j].strip().lower()
            
            if 'completed' in next_line and '2022' in next_line:
                status = 'completed'
                break
            elif 'complete construction' in next_line and '2022' in next_line:
                status = 'completed'
                break
                
        if status == 'completed':
            park_projects_2022.append(project_name)
            print(f"Found park project: {project_name}")

print(f"\nTotal park projects completed in 2022: {len(park_projects_2022)}")

# Match with funding records
matched_funding = []
total_amount = 0

for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects_2022:
        proj_name_lower = project.lower()
        
        # Check if project name is in funding name or vice versa
        if proj_name_lower in fund_name or fund_name in proj_name_lower:
            matched_funding.append({
                'project': project,
                'funding_name': fund.get('Project_Name'),
                'amount': fund_amount
            })
            total_amount += fund_amount
            print(f"MATCHED: {project} -> {fund.get('Project_Name')} = ${fund_amount}")
            break

print(f"\nTotal matched funding records: {len(matched_funding)}")
print(f"Total funding amount: ${total_amount}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
