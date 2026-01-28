code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:6']

with open(funding_file, 'r') as f:
    funding = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding dictionary
funding_dict = {}
for record in funding:
    name = record.get('Project_Name', '')
    amt = int(record.get('Amount', 0))
    if name and amt > 0:
        funding_dict[name] = funding_dict.get(name, 0) + amt

# Find Spring 2022 projects
spring_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Look for pattern: project name line followed by schedule info
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Skip headers and metadata
        skip_terms = ['page', 'agenda', 'item', 'public works', 'commission', 'prepared by', 'approved by']
        if any(term in line.lower() for term in skip_terms):
            continue
        
        # Look ahead for schedule info with Spring 2022
        next_lines = '\n'.join(lines[i:i+8])
        
        # Check if this looks like a project with Spring 2022 schedule
        has_2022 = '2022' in next_lines
        has_spring = any(x in next_lines.lower() for x in ['spring', 'march', 'april', 'may'])
        
        if has_2022 and has_spring:
            # Check if line is likely a project name (not too long, not a status keyword)
            if (len(line) < 80 and 
                not any(x in line.lower() for x in ['update', 'schedule', 'description']) and
                line[0].isupper()):
                
                spring_projects.add(line)

# Match with funding data
matched = []
total = 0

for proj in spring_projects:
    # Direct match
    if proj in funding_dict:
        amt = funding_dict[proj]
        matched.append({'project': proj, 'funding': amt})
        total += amt
        continue
    
    # Partial match
    for funded_proj in funding_dict:
        if proj.lower() in funded_proj.lower() or funded_proj.lower() in proj.lower():
            amt = funding_dict[funded_proj]
            matched.append({'project': proj, 'funding': amt, 'matched_to': funded_proj})
            total += amt
            break

print('__RESULT__:')
print(json.dumps({
    'spring_2022_project_count': len(matched),
    'total_funding': total
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
