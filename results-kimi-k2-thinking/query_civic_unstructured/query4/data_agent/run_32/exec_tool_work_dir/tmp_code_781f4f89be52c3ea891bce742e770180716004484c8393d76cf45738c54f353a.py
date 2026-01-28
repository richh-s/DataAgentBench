code = """import json
import re

# Load data files
funding_path = locals()['var_functions.query_db:5']
civic_path = locals()['var_functions.query_db:6']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Build funding lookup
funding_dict = {}
for row in funding_data:
    name = row.get('Project_Name', '')
    if name:
        funding_dict[name] = funding_dict.get(name, 0) + int(row.get('Amount', 0))

# Find Spring 2022 projects in civic documents
spring_project_names = set()

for document in civic_data:
    text = document.get('text', '')
    if not text or '2022' not in text:
        continue
    
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 80:
            continue
        
        # Skip metadata lines
        if any(x in line.lower() for x in ['page', 'agenda item', 'public works', 'commission', 'prepared by']):
            continue
        
        # Look ahead for Spring indicators near 2022
        context = ' '.join(lines[idx:idx+8]).lower()
        has_2022 = '2022' in context
        has_spring = any(s in context for s in ['spring', 'march', 'april', 'may'])
        
        if has_2022 and has_spring:
            # Check if this line looks like a project name
            if line[0].isupper() and 'update' not in line.lower() and 'schedule' not in line.lower():
                spring_project_names.add(line)

# Match projects with funding data
matched_projects = []
total_funding_amount = 0

for proj_name in spring_project_names:
    # Exact match
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        matched_projects.append([proj_name, amount])
        total_funding_amount += amount
        continue
    
    # Partial match check
    for funded_name in funding_dict:
        if proj_name.lower() in funded_name.lower() or funded_name.lower() in proj_name.lower():
            amount = funding_dict[funded_name]
            matched_projects.append([proj_name, amount])
            total_funding_amount += amount
            break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding_amount
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
