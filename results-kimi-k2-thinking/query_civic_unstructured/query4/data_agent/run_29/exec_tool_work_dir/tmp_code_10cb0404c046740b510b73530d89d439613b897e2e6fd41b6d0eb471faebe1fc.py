code = """import json
import os
import re

print('=== LOCATING DATA FILES ===')

# Find the data files
files = os.listdir('.')
funding_file = None
civic_file = None

for f in files:
    if 'query_db' in f and ('14' in f or 'funding' in f):
        funding_file = f
    elif 'query_db' in f and ('24' in f or 'civic' in f or '15' in f):
        civic_file = f

print(f'Funding data file: {funding_file}')
print(f'Civic data file: {civic_file}')

# Load funding data
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic data
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

print(f'\n=== DATA LOADED ===')
print(f'Funding records: {len(funding_data)}')
print(f'Civic documents: {len(civic_data)}')

# Create funding lookup
funding_dict = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_dict[project_name] = amount

print(f'Funding lookup created with {len(funding_dict)} projects')

# Search for Spring 2022 projects
spring_patterns = [
    r'2022[-\s]Spring', r'2022[-\s]March', r'2022[-\s]April', r'2022[-\s]May',
    r'Spring\s+2022', r'March\s+2022', r'April\s+2022', r'May\s+2022'
]

spring_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('Page') or 'Agenda Item' in line:
            continue
            
        # Look for project-like names
        if len(line) > 10 and (line.istitle() or (line[0].isupper() and len(line.split()) > 2)):
            context = ' '.join(lines[i:i+5])
            for pattern in spring_patterns:
                if re.search(pattern, context, re.IGNORECASE):
                    if line not in [p['name'] for p in spring_projects]:
                        spring_projects.append({'name': line, 'context': context[:150]})
                    break

print(f'\n=== SPRING 2022 PROJECTS FOUND ===')
print(f'Count: {len(spring_projects)}')
for i, proj in enumerate(spring_projects[:10], 1):
    print(f'{i}. {proj["name"][:60]}')

# Match with funding
matched = []
total_funding = 0

for proj in spring_projects:
    project_name = proj['name']
    if project_name in funding_dict:
        amount = funding_dict[project_name]
        matched.append({'name': project_name, 'funding': amount, 'type': 'exact'})
        total_funding += amount
        print(f'Match: {project_name} = ${amount}')
    else:
        # Try partial
        for funded_name, amount in funding_dict.items():
            if project_name.lower() in funded_name.lower() or funded_name.lower() in project_name.lower():
                matched.append({'name': project_name, 'funding': amount, 'type': 'partial', 'matched_with': funded_name})
                total_funding += amount
                print(f'Partial: {project_name} -> {funded_name} = ${amount}')
                break

print(f'\n=== SUMMARY ===')
print(f'Projects in Spring 2022: {len(matched)}')
print(f'Total funding: ${total_funding:,}')

result_str = f'Projects started in Spring 2022: {len(matched)}. Total funding: ${total_funding:,}'

print('\n__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
