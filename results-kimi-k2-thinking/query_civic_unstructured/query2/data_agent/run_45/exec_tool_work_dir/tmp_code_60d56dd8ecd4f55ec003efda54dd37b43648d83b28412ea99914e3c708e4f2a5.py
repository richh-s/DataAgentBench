code = """import json
import re

# Load civic documents
civic_file_path = '/tmp/tmpq0c3uww8.json'
with open(civic_file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_file_path = '/tmp/tmphv6u7l7_.json'
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) > 10 and 'park' in line.lower() and 'Project' in line:
                for j in range(i+1, min(i+15, len(lines))):
                    if '2022' in lines[j] and 'completed' in lines[j].lower():
                        park_projects.append(line)
                        break

# Remove duplicates
park_projects = list(set(park_projects))
print('Found', len(park_projects), 'park projects')

# Create funding lookup
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
print('__RESULT__:')
print(total_funding)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
