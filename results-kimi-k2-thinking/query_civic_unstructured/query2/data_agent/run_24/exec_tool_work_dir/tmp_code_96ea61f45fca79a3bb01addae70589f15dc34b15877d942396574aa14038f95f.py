code = """import json
import re

print('Starting analysis...')

# Load civic documents
with open('/tmp/tmpw8a01a0z.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding records  
with open('/tmp/tmptjtu3_1d.json', 'r') as f:
    funding_records = json.load(f)

print('Data loaded successfully')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_records))

# Extract project data from civic documents
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        # Look for completed park projects in 2022
        if line and 'completed' in line.lower():
            if '2022' in line and 'park' in line.lower():
                all_projects.append(line)

print('Found potential projects:', len(all_projects))

# Show what we found
for proj in all_projects[:10]:
    print('Project:', proj)

__RESULT__:
print(json.dumps({'civic_docs': len(civic_docs), 'funding': len(funding_records), 'found_projects': len(all_projects)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
