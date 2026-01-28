code = """import json
import re

mongo_path = locals()['var_functions.query_db:14']
funding_path = locals()['var_functions.query_db:4']

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_lookup = {}
for rec in funding_records:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text and 'Begin Construction' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line and 'Spring' in line:
                for j in range(i-1, max(i-10, -1), -1):
                    candidate = lines[j].strip()
                    if candidate and not candidate.startswith('('):
                        if len(candidate) > 5 and 'Schedule' not in candidate:
                            spring_projects.add(candidate)
                            break

print('Found', len(spring_projects), 'Spring 2022 projects')
print(list(spring_projects)[:10])

matched_projects = []
for proj in spring_projects:
    if proj in funding_lookup:
        matched_projects.append({'name': proj, 'funding': funding_lookup[proj]})

print('Total funding', sum(p['funding'] for p in matched_projects))

result_str = 'Count: ' + str(len(matched_projects)) + ' Total funding: $' + str(sum(p['funding'] for p in matched_projects))
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
