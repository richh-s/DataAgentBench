code = """import json
import re

# Load data
funding_file = locals()['var_functions.query_db:5']
civic_file = locals()['var_functions.query_db:6']

with open(funding_file) as f:
    funding = json.load(f)

with open(civic_file) as f:
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
    
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) > 70:
                continue
            
            # Skip common headers
            skip = ['page', 'agenda', 'item', 'public works', 'commission', 'prepared']
            if any(x in line.lower() for x in skip):
                continue
            
            # Look ahead for spring 2022
            look_ahead = ' '.join(lines[i:i+6]).lower()
            if '2022' in look_ahead and ('spring' in look_ahead or 'march' in look_ahead or 'april' in look_ahead or 'may' in look_ahead):
                if line[0].isupper() and 'update' not in line.lower() and 'schedule' not in line.lower():
                    spring_projects.add(line)

# Match with funding
matched = []
total = 0

for proj in spring_projects:
    if proj in funding_dict:
        amt = funding_dict[proj]
        matched.append([proj, amt])
        total += amt
    else:
        # Try partial match
        for funded in funding_dict:
            if proj.lower() in funded.lower() or funded.lower() in proj.lower():
                amt = funding_dict[funded]
                matched.append([proj, amt])
                total += amt
                break

# Prepare result
result = {
    'spring_2022_projects': len(matched),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
