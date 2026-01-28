code = """import json, re

# Load data
civic_docs = json.load(open('/tmp/tmpq0c3uww8.json'))
funding_data = json.load(open('/tmp/tmphv6u7l7_.json'))

print('Loaded documents')

# Extract park projects in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find lines with park-related projects
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) > 5 and not line.startswith(('(', '•')):
            line_lower = line.lower()
            if 'park' in line_lower and ('project' in line_lower or 'improvements' in line_lower):
                # Check following lines for 2022 completion
                found = False
                for j in range(i+1, min(i+10, len(lines))):
                    if '2022' in lines[j] and 'completed' in lines[j].lower():
                        found = True
                        break
                if found:
                    park_projects.append(line)

# Remove duplicates
park_projects = list(set(park_projects))
print('Found park projects:', len(park_projects))

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    name = fund.get('Project_Name')
    amount = int(fund.get('Amount', 0))
    funding_lookup[name] = amount

# Match and sum funding
total_funding = 0
for project in park_projects:
    if project in funding_lookup:
        total_funding += funding_lookup[project]
    else:
        # Try partial match
        proj_lower = project.lower()
        for fund_name, amount in funding_lookup.items():
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                total_funding += amount
                break

result = str(total_funding)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
