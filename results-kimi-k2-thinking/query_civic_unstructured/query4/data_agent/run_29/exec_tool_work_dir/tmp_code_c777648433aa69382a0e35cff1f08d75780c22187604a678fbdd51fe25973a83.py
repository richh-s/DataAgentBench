code = """import json
import os
import re

# Find data files
files = os.listdir('.')
funding_file = None
civic_file = None

for f in files:
    if 'query_db' in f:
        if '14' in f or '28' in f:
            funding_file = f
        else:
            civic_file = f

print('Funding file: ' + funding_file)
print('Civic file: ' + civic_file)

# Load data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print('Funding records: ' + str(len(funding_data)))
print('Civic documents: ' + str(len(civic_data)))

# Build funding lookup
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

# Search for Spring 2022 projects
patterns = [
    '2022-Spring', '2022 March', '2022 April', '2022 May',
    '2022 March', '2022 April', '2022 May',
    'Spring 2022', 'March 2022', 'April 2022', 'May 2022'
]

spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    if any(pattern.lower() in text.lower() for pattern in patterns):
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if not line or len(line) < 15:
                continue
            if line.startswith('Page') or 'Agenda Item' in line:
                continue
            if line.istitle() or (line[0].isupper() and len(line.split()) > 3):
                context = ' '.join(lines[i:i+6])
                for pattern in patterns:
                    if pattern.lower() in context.lower():
                        if line not in [p['name'] for p in spring_projects]:
                            spring_projects.append({'name': line, 'context': context[:200]})
                        break

print('Spring 2022 projects found: ' + str(len(spring_projects)))

# Match with funding
matched = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched.append({'name': project_name, 'funding': amount})
        total_funding = total_funding + amount
    else:
        for funded_name in funding_dict:
            if project_name.lower() in funded_name.lower() or funded_name.lower() in project_name.lower():
                if len(project_name) > 15 and len(funded_name) > 15:
                    amount = funding_dict[funded_name]
                    matched.append({'name': project_name, 'funding': amount, 'matched_with': funded_name})
                    total_funding = total_funding + amount
                    break

# Format result
project_count = len(matched)
funding_str = '{:,}'.format(total_funding)
result = 'Projects started in Spring 2022: ' + str(project_count) + '. Total funding: $' + funding_str

print('\n__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
