code = """import json

# Load civic documents
civic_path = 'var_functions_query_db_2.json'
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding records
funding_path = 'var_functions_query_db_4.json'
with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Build funding lookup
funding = {}
for rec in funding_recs:
    name = rec.get('Project_Name', '')
    if name:
        funding[name] = int(rec.get('Amount', 0))

# Find Spring 2022 projects
import re
spring_2022 = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or '2022-Spring' in text:
        # Look for project names
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if (len(line) > 10 and 
                any(k in line for k in ['Project', 'Improvements', 'Repairs', 'Replacement'])):
                if not line.startswith('(') and not line.startswith('To:'):
                    spring_2022.add(line)

# Match with funding
matched = []
used = set()
for proj in spring_2022:
    if proj in funding and proj not in used:
        matched.append({'project': proj, 'funding': funding[proj]})
        used.add(proj)
        continue
    # Partial match
    for fund_name in funding:
        if fund_name in used:
            continue
        if proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower():
            matched.append({'project': proj, 'funding': funding[fund_name]})
            used.add(fund_name)
            break

count = len(matched)
total = sum(m['funding'] for m in matched)

print('__RESULT__:')
result = json.dumps({'project_count': count, 'total_funding': total})
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:24': {'var_functions.list_db:0': "<class 'list'>", 'var_functions.query_db:2': "<class 'str'>", 'var_functions.query_db:4': "<class 'str'>"}}

exec(code, env_args)
