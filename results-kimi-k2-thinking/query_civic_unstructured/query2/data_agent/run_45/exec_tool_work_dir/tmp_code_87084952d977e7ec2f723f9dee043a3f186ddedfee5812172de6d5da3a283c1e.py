code = """import json
import re

# Load data from files
civic_docs_file = locals()['var_functions.query_db:22']
funding_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Documents loaded')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
                if 'Project' in line and ('park' in line.lower() or 'Park' in line):
                    for j in range(i+1, min(i+15, len(lines))):
                        if '2022' in lines[j] and 'completed' in lines[j].lower():
                            park_projects_2022.append(line)
                            break

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print('Found park projects:', len(unique_projects))

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Sum funding for matched projects
total_funding = 0
matched = 0

for project in unique_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        matched += 1
    else:
        project_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            fund_lower = fund_name.lower()
            if project_lower in fund_lower or fund_lower in project_lower:
                total_funding += amount
                matched += 1
                break

result = json.dumps({'total_funding': total_funding, 'matched': matched, 'found': len(unique_projects)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
