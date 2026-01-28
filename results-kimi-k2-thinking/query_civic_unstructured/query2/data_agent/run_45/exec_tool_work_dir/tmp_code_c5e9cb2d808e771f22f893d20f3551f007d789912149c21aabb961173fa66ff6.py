code = """import json
import os

# Get file paths from environment variables or known temporary locations
civic_docs_path = 'result__functions.query_db:14.json'
funding_path = 'result__functions.query_db:2.json'

# Read the civic documents
civic_docs_content = open('/tmp/tmpq0c3uww8.json', 'r').read()
civic_docs = json.loads(civic_docs_content)

# Read the funding data
funding_content = open('/tmp/tmphv6u7l7_.json', 'r').read()
funding_data = json.loads(funding_content)

# Print summary
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding_data))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and not line.startswith(('(', '•')):
                if 'Project' in line and 'park' in line.lower():
                    for j in range(i+1, min(i+15, len(lines))):
                        if '2022' in lines[j] and 'completed' in lines[j].lower():
                            park_projects_2022.append(line)
                            break

# Remove duplicates
unique_projects = list(set(park_projects_2022))
print('Park projects found:', len(unique_projects))

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Calculate total funding
total_funding = 0
matched = 0

for project in unique_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        matched += 1
    else:
        proj_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            fund_lower = fund_name.lower()
            if proj_lower in fund_lower or fund_lower in proj_lower:
                total_funding += amount
                matched += 1
                break

print('Total funding:', total_funding)
print('Matched projects:', matched)

result = json.dumps({'total_funding': total_funding})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
