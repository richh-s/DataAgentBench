code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:5']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_functions.query_db:16']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_map = {}
for rec in funding_records:
    funding_map[rec['Project_Name']] = int(rec['Total_Amount'])

spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('(cid:') or line.startswith('Page'):
            continue
            
        if (line.startswith('2022 ') or 
            line.startswith('Capital Improvement') or 
            line.startswith('Disaster Recovery') or
            line.startswith('Design') or
            line.startswith('Construction') or
            'Project' in line):
            current_project = line
        
        if current_project and any(x in line for x in ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May']):
            spring_2022_projects.add(current_project)
            
        if any(line.startswith(x) for x in ['2022 Morning View', '2022 Annual Street']):
            spring_2022_projects.add(line)

final_projects = []
for name in spring_2022_projects:
    amount = funding_map.get(name, 0)
    if amount > 0:
        final_projects.append((name, amount))

final_projects.sort(key=lambda x: x[1], reverse=True)

result = f"{len(final_projects)}|{sum(p[1] for p in final_projects)}"

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': []}

exec(code, env_args)
