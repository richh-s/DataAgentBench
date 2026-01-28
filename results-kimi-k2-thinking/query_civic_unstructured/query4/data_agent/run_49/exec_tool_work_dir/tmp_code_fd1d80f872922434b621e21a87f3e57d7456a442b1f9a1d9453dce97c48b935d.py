code = """import json
import re

civic_docs = var_functions.query_db:10
funding_records = var_functions.query_db:7

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding_records, str) and funding_records.endswith('.json'):
    with open(funding_records, 'r') as f:
        funding_records = json.load(f)

funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    funding_map[name] = amount

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    spring_patterns = ['2022-Spring', 'Spring 2022', '2022-March', 'March 2022', '2022-April', 'April 2022', '2022-May', 'May 2022']
    has_spring = any(pattern in text for pattern in spring_patterns)
    
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Drainage']):
                if len(line) > 15:
                    spring_projects.append(line)

spring_projects = list(set(spring_projects))

matches = []
total = 0

for project in spring_projects:
    if project in funding_map:
        amount = funding_map[project]
        matches.append({'name': project, 'funding': amount})
        total += amount

result = {'num_projects': len(matches), 'total_funding': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
