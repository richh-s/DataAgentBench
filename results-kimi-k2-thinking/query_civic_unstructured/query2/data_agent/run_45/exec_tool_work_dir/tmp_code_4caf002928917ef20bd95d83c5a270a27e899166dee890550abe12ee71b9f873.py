code = """import json
import re

# Load data from JSON files
civic_docs = json.load(open('/tmp/tmpq0c3uww8.json'))
funding_data = json.load(open('/tmp/tmphv6u7l7_.json'))

print('Loaded data successfully')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and 'park' in line.lower() and 'Project' in line:
                for j in range(i+1, min(i+15, len(lines))):
                    if '2022' in lines[j] and 'completed' in lines[j].lower():
                        park_projects.append(line)
                        break

# Remove duplicates
park_projects = list(set(park_projects))
print('Found', len(park_projects), 'park projects')

# Build funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Calculate total funding
total_funding = 0
for project in park_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        proj_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            fund_lower = fund_name.lower()
            if proj_lower in fund_lower or fund_lower in proj_lower:
                total_funding += amount
                break

print('Total funding:', total_funding)
result = str(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
