code = """import json

docs = locals().get('var_functions.query_db:5')
funds = locals().get('var_functions.query_db:8')

if isinstance(docs, str) and docs.endswith('.json'):
    with open(docs, 'r') as f:
        docs = json.load(f)

if isinstance(funds, str) and funds.endswith('.json'):
    with open(funds, 'r') as f:
        funds = json.load(f)

spring_projects = []
spring_patterns = ['Spring 2022', '2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if line and len(line) > 5:
            for j in range(1, min(15, len(lines)-i)):
                if any(p in lines[i+j] for p in spring_patterns):
                    spring_projects.append(line)
                    break

spring_projects = list(set(spring_projects))

funding_map = {}
for f in funds:
    n = f.get('Project_Name', '').strip()
    a = int(f.get('Amount', 0))
    funding_map[n] = funding_map.get(n, 0) + a

matched = []
total = 0

for proj in spring_projects:
    if proj in funding_map:
        matched.append({'name': proj, 'amount': funding_map[proj]})
        total += funding_map[proj]

result = {'project_count': len(matched), 'total_funding': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
