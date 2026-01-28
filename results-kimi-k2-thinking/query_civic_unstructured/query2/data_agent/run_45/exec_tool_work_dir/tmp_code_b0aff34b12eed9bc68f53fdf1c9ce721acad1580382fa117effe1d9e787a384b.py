code = """import json, re

# Load data
civic_docs = json.load(open(var_functions.query_db:14))
funding_data = json.load(open(var_functions.query_db:2))

print('Documents loaded:', len(civic_docs))

# Extract park projects completed in 2022
park_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find projects with 2022 completion
    if '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 10 and not line.startswith('('):
                if 'Project' in line or 'Improvements' in line:
                    if 'park' in line.lower() or 'Park' in line:
                        # Check following lines for 2022 completion
                        for j in range(i+1, min(i+20, len(lines))):
                            if '2022' in lines[j] and 'completed' in lines[j].lower():
                                park_projects.add(line)
                                break

print('Park projects in 2022:', len(park_projects))

# Match with funding
funding_lookup = {f['Project_Name']: int(f['Amount']) for f in funding_data}
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

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
