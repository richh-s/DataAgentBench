code = """import json
import re

# Load data
mongo_file = str(globals()['var_functions.query_db:5'])
funding_file = str(globals()['var_functions.query_db:20'])

with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Create funding map
funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name'].strip()] = int(rec['Amount'])

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if '2022' in line and ('Spring' in line or 'spring' in line):
            # Get context around this line
            context_start = max(0, i-3)
            context_end = min(len(lines), i+3)
            context = ' '.join(lines[context_start:context_end])
            
            spring_2022_projects.append({
                'line': line,
                'context': context,
                'filename': doc.get('filename', '')
            })

print('Found Spring 2022 references:', len(spring_2022_projects))

# Match with funding
matched = []
total_funding = 0

for proj in spring_2022_projects:
    context = proj['context']
    line = proj['line']
    
    # Try to extract project name from context
    # Look for patterns that might be project names
    
    # Check if any funded project name appears in the context
    for fund_name, amount in funding_map.items():
        if fund_name.lower() in context.lower():
            matched.append({
                'project': fund_name,
                'funding': amount,
                'context': context[:100]
            })
            total_funding += amount
            break

print('Matched projects:', len(matched))
print('Total funding:', total_funding)

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'funding': total_funding}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:28': {'status': 'loaded', 'civic_docs': 5, 'funding_records': 500}}

exec(code, env_args)
