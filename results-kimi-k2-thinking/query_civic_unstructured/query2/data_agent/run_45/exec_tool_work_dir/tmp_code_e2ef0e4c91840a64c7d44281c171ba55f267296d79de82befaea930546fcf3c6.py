code = """import json
import re

# Load the data
civic_docs_file = locals()['var_functions.query_db:22']
funding_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'documents')

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Look for project names (not bullet points, reasonable length)
        if len(line) > 10 and not line.startswith(('(', '•', '-')):
            if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
                if 'park' in line.lower() or 'Park' in line:
                    # Check following lines for 2022 completion
                    for j in range(i+1, min(i+15, len(lines))):
                        if '2022' in lines[j] and 'completed' in lines[j].lower():
                            park_projects.append(line)
                            break

# Remove duplicates
park_projects = list(set(park_projects))
print('Park projects:', len(park_projects))

# Match with funding
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

total_funding = 0
matched = 0

for project in park_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
        matched += 1
    else:
        # Try partial match
        proj_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                total_funding += amount
                matched += 1
                break

result_text = json.dumps({'total_funding': total_funding, 'matched': matched, 'found': len(park_projects)})
print('__RESULT__:')
print(result_text)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
