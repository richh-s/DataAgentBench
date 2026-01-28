code = """import json
import re

# Get file paths
mongo_path = locals()['var_functions.query_db:14']
funding_path = locals()['var_functions.query_db:4']

# Load data
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(mongo_docs), 'documents and', len(funding_records), 'funding records')

# Create funding lookup
funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

spring_projects = set()

# Extract projects starting Spring 2022
for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Begin Construction' in line and '2022' in line and 'Spring' in line:
                # Look backward for project name
                for j in range(i-1, max(i-10, -1), -1):
                    prev_line = lines[j].strip()
                    if prev_line and not prev_line.startswith('('):
                        if len(prev_line) > 5 and 'Schedule' not in prev_line:
                            spring_projects.add(prev_line)
                            break

print('Spring 2022 projects found:', len(spring_projects))
for proj in spring_projects:
    print(' -', proj)

# Match with funding
matched = []
for proj in spring_projects:
    if proj in funding_lookup:
        matched.append({'name': proj, 'funding': funding_lookup[proj]})

total_funding = sum([m['funding'] for m in matched])

print('Projects with funding:', len(matched))
print('Total funding: $', total_funding)

# Prepare output
output = {
    'count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(str(output)))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
