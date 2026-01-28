code = """import json, re

# Load data from files
civic_docs = json.load(open('/tmp/tmpq0c3uww8.json'))
funding_data = json.load(open('/tmp/tmphv6u7l7_.json'))

print('Loaded data')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    if 'completed' not in text.lower():
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 10:
            continue
        if line.startswith(('(', '•')):
            continue
        
        if 'park' in line.lower() and 'project' in line.lower():
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j]
                if '2022' in next_line and 'completed' in next_line.lower():
                    park_projects_2022.append(line)
                    break

# Remove duplicates
unique_park_projects = list(set(park_projects_2022))
print('Found', len(unique_park_projects), 'park projects')

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Calculate total funding
total_funding = 0
for project in unique_park_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        project_words = set(project.lower().split())
        for fund_name, amount in funding_lookup.items():
            fund_words = set(fund_name.lower().split())
            if len(project_words.intersection(fund_words)) >= 2:
                total_funding += amount
                break

print('Total funding:', total_funding)
result = str(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
