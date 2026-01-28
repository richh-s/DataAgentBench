code = """import json
import re

# Load data
civic_docs = var_functions_query_db_36
funding_data = var_functions_query_db_34

print('Spring 2022 docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Simple extraction
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 15 or len(line) > 150:
            continue
            
        keywords = ['project', 'improvements', 'repairs', 'replacement', 'facility']
        if any(k in line.lower() for k in keywords):
            context = ' '.join(lines[i:i+6])
            
            if re.search(r'Begin.*?Spring.*?2022|Begin.*?(March|April|May).*?2022', context, re.IGNORECASE):
                name = re.sub(r'^(cid:\d+\s*)+', '', line)
                name = re.sub(r'^[\-\*\•\d\.\s]+', '', name)
                name = name.strip()
                
                if name and len(name) > 15:
                    projects.append(name)

# Remove duplicates
seen = set()
unique_projects = []
for p in projects:
    if p.lower() not in seen:
        seen.add(p.lower())
        unique_projects.append(p)

print('Unique projects:', len(unique_projects))

# Match funding
total = 0
for project in unique_projects:
    proj_lower = project.lower()
    for fund in funding_data:
        fund_lower = fund['Project_Name'].lower()
        if proj_lower in fund_lower or fund_lower in proj_lower:
            total += int(fund['Amount'])
            break

print('Total funding:', total)
print('__RESULT__:', json.dumps({'count': len(unique_projects), 'funding': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:24': {'civic_count': 5, 'funding_count': 500}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json'}

exec(code, env_args)
