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

spring_projects = set()
for doc in civic_docs:
    text = doc['text']
    
    if '2022 Morning View Resurfacing' in text:
        spring_projects.add('2022 Morning View Resurfacing & Storm Drain Improvements')
    
    if '2022 Annual Street Maintenance' in text:
        spring_projects.add('2022 Annual Street Maintenance')
    
    if 'Spring 2023' not in text:
        continue

projects_with_funding = []
for project in spring_projects:
    if project in funding_map:
        projects_with_funding.append((project, funding_map[project]))

total_projects = len(projects_with_funding)
total_funding = sum(p[1] for p in projects_with_funding)

result_str = 'PROJECTS:' + str(total_projects) + '|FUNDING:' + str(total_funding)

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': []}

exec(code, env_args)
