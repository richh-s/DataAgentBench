code = """import json
import re

civic_docs_file = var_functions.query_db:2
funding_file = var_functions.query_db:5

# Read civic documents
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding records  
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded documents: {len(civic_docs)}, funding records: {len(funding_data)}")

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Skip common headers
        if any(x in line for x in ['Page', 'Agenda', 'Public Works', 'To:', 'From:', 'Date:', 'Subject:', 'Project Schedule']):
            continue
        if line[0] in ['(', '·', '-', '□']:
            continue
            
        # Check for park-related projects
        lower_line = line.lower()
        if 'park' not in lower_line and 'playground' not in lower_line:
            continue
            
        # Look for completion in 2022
        project_name = line
        is_completed = False
        
        for j in range(i+1, min(i+12, len(lines))):
            next_line = lines[j].strip().lower()
            if 'completed' in next_line and '2022' in next_line:
                is_completed = True
                break
            if 'complete construction' in next_line and '2022' in next_line:
                is_completed = True
                break
                
        if is_completed:
            park_projects.append(project_name)
            print(f"Found: {project_name}")

print(f"\nPark projects completed in 2022: {len(park_projects)}")

# Match with funding
total_funding = 0
matches = 0

for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    for project in park_projects:
        proj_lower = project.lower()
        if proj_lower in fund_name or fund_name in proj_lower:
            total_funding += fund_amount
            matches += 1
            print(f"Match: {project} -> {fund.get('Project_Name')} = ${fund_amount}")
            break

print(f"\nMatches: {matches}, Total funding: ${total_funding}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
