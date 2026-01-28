code = """import json, re

# Load the data files
civic_docs = json.load(open(var_functions.query_db:2))
funding_records = json.load(open(var_functions.query_db:4))

# Create funding lookup
funding_lookup = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    if name:
        funding_lookup[name] = int(rec.get('Amount', 0))

# Find Spring 2022 projects
spring2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) > 10 and len(line) < 150:
                if 'Project' in line or 'Improvements' in line or 'Repairs' in line:
                    if not line.startswith('(') and not line.startswith('To:'):
                        spring2022.append(line)

spring2022 = list(set(spring2022))

# Match with funding
matches = []
used = set()
for proj in spring2022:
    if proj in funding_lookup and proj not in used:
        matches.append({'project': proj, 'funding': funding_lookup[proj]})
        used.add(proj)
    else:
        proj_lower = proj.lower()
        for fund_name in funding_lookup:
            if fund_name in used:
                continue
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                matches.append({'project': proj, 'funding': funding_lookup[fund_name]})
                used.add(fund_name)
                break

count = len(matches)
total = sum(m['funding'] for m in matches)

print('__RESULT__:')
result = json.dumps({'project_count': count, 'total_funding': total})
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
