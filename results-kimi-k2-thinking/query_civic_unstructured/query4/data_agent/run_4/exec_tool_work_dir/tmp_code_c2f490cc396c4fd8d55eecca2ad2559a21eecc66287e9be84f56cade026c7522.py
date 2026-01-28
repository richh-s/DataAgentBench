code = """import json

# Load the data
civic_docs = json.load(open(var_functions.query_db:2))
funding_records = json.load(open(var_functions.query_db:4))

# Build funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find all projects that mention Spring 2022
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Extract project names - look for lines that might be project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Simple heuristic for project names
            if len(line) > 10 and len(line) < 150:
                if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
                    if not line.startswith('(') and not line.startswith('To:'):
                        spring_2022_projects.append(line)

# Remove duplicates
spring_2022_projects = list(set(spring_2022_projects))

# Match with funding data
matched = []
total = 0
for proj in spring_2022_projects:
    if proj in funding_lookup:
        matched.append({'project': proj, 'funding': funding_lookup[proj]})
        total += funding_lookup[proj]
    else:
        # Try partial match
        for fund_proj in funding_lookup:
            if proj.lower() in fund_proj.lower() or fund_proj.lower() in proj.lower():
                matched.append({'project': proj, 'funding': funding_lookup[fund_proj]})
                total += funding_lookup[fund_proj]
                break

# Remove duplicates from matched
unique_projects = {}
for m in matched:
    proj_name = m['project']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = m['funding']

final_count = len(unique_projects)
total_funding = sum(unique_projects.values())

print('__RESULT__:')
print(json.dumps({'project_count': final_count, 'total_funding': total_funding}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
