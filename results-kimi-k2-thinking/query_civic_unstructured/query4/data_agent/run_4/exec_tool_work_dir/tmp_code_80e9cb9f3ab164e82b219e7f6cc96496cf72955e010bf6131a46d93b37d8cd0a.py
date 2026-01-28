code = """import json, re

# Load data from files
civic_docs = json.load(open(var_functions.query_db:2))
funding_records = json.load(open(var_functions.query_db:4))

# Create funding lookup dictionary
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find projects in Spring 2022
spring_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        current = None
        for line in lines:
            line = line.strip()
            # Identify project names by keywords and format
            if (any(k in line for k in ['Project', 'Improvements', 'Repairs', 'Replacement']) and
                not line.startswith('(') and 10 < len(line) < 150):
                current = line
            if ('Spring 2022' in line or '2022-Spring' in line) and current:
                spring_projects.append(current)

spring_projects = list(set(spring_projects))

# Match with funding
matches = []
used = set()
for proj in spring_projects:
    # Direct match
    if proj in funding_lookup and proj not in used:
        matches.append({'project': proj, 'funding': funding_lookup[proj]})
        used.add(proj)
        continue
    
    # Partial match
    proj_lower = proj.lower()
    for fund_name in funding_lookup:
        if fund_name in used:
            continue
        if (proj_lower in fund_name.lower() or fund_name.lower() in proj_lower):
            matches.append({'project': proj, 'funding': funding_lookup[fund_name]})
            used.add(fund_name)
            break

total_funding = sum(m['funding'] for m in matches)

result = {
    'project_count': len(matches),
    'total_funding': total_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
