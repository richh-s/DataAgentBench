code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:5']) as f:
    funding_data = json.load(f)
    
with open(locals()['var_functions.query_db:6']) as f:
    civic_data = json.load(f)

# Build funding dictionary
funding_dict = {}
for record in funding_data:
    name = record.get('Project_Name')
    if name:
        amt = int(record.get('Amount', 0))
        funding_dict[name] = funding_dict.get(name, 0) + amt

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    # Split into lines and look for projects
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty or long lines
        if not line or len(line) > 60:
            continue
        
        # Skip headers
        if any(x in line.lower() for x in ['page', 'agenda', 'prepared by', 'approved by']):
            continue
        
        # Look ahead for spring 2022 context
        context = ' '.join(lines[i:i+8]).lower()
        if '2022' in context and ('spring' in context or 'march' in context or 'april' in context or 'may' in context):
            if line[0].isupper():
                spring_projects.add(line)

# Match with funding
count = 0
total = 0

for proj in spring_projects:
    # Direct match
    if proj in funding_dict:
        count += 1
        total += funding_dict[proj]
        continue
    
    # Check for variants
    for funded in funding_dict:
        if proj.lower() in funded.lower():
            count += 1
            total += funding_dict[funded]
            break

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
