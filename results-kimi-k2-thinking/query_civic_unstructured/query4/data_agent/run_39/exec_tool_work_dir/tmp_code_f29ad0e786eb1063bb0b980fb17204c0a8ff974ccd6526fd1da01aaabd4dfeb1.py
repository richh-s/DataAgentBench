code = """import json
import re

# Load data
civic_docs = locals().get('var_functions.query_db:5', [])
funding_data = locals().get('var_functions.query_db:8', [])

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

spring_projects = []
patterns = ['Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 5:
            continue
        following = ' '.join(lines[i+1:min(i+15, len(lines))])
        if any(p in following for p in patterns):
            spring_projects.append(line)

spring_projects = list(set(spring_projects))

funding_lookup = {}
for f in funding_data:
    name = f.get('Project_Name', '').strip()
    amount = int(f.get('Amount', 0))
    funding_lookup[name] = funding_lookup.get(name, 0) + amount

matched = []
total = 0

for proj in spring_projects:
    if proj in funding_lookup:
        matched.append({'name': proj, 'amount': funding_lookup[proj]})
        total += funding_lookup[proj]
    else:
        for fund_name, amount in funding_lookup.items():
            if proj.lower() in fund_name.lower() or fund_name.lower() in proj.lower():
                matched.append({'name': proj, 'amount': amount})
                total += amount
                break

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}}

exec(code, env_args)
