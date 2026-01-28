code = """import json
import re

# Access the file paths from storage
civic_docs_file = var_functions.query_db:14
funding_file = var_functions.query_db:2

# Load data from files
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for completion statements with 2022
    if '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        # Extract project names and context
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Check if this is a project name line
            if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
                if 'Project' in line or 'Improvements' in line or 'Repairs' in line or 'Replacement' in line or 'Structure' in line:
                    # Check if it's park-related
                    is_park = 'park' in line.lower() or 'Park' in line
                    
                    if is_park:
                        # Look for 2022 completion in following lines
                        found_2022 = False
                        for j in range(i+1, min(i+15, len(lines))):
                            next_line = lines[j]
                            if '2022' in next_line and ('completed' in next_line.lower() or 'completion' in next_line.lower()):
                                found_2022 = True
                                break
                        
                        if found_2022:
                            park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))
print('Found park projects completed in 2022:', len(unique_projects))
for p in unique_projects:
    print('-', p)

# Match with funding data
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

total_funding = 0
matched_projects = []

for project_name in unique_projects:
    # Direct match
    if project_name in funding_lookup:
        amount = funding_lookup[project_name]
        total_funding += amount
        matched_projects.append({'name': project_name, 'funding': amount})
        print('Matched:', project_name, 'with funding', amount)
    else:
        # Try partial matching
        project_lower = project_name.lower()
        for fund_name in funding_lookup:
            fund_lower = fund_name.lower()
            if project_lower in fund_lower or fund_lower in project_lower:
                amount = funding_lookup[fund_name]
                total_funding += amount
                matched_projects.append({'name': project_name, 'funding': amount})
                print('Partial matched:', project_name, '->', fund_name, 'with funding', amount)
                break

result = {'total_funding': total_funding, 'matched_count': len(matched_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
