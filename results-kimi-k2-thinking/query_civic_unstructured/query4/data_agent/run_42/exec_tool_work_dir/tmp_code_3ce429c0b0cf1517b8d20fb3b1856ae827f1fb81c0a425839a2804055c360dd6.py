code = """import json
import re

# Load the data
mongo_file = open(locals()['var_functions.query_db:14'])
mongo_docs = json.load(mongo_file)
mongo_file.close()

funding_file = open(locals()['var_functions.query_db:4'])
funding_records = json.load(funding_file)
funding_file.close()

# Build funding lookup
d = {}
for rec in funding_records:
    d[rec['Project_Name']] = int(rec['Amount'])

# Find Spring 2022 projects
spring_projects = set()

for doc in mongo_docs:
    t = doc.get('text', '')
    if 'Spring' in t and '2022' in t and 'Begin Construction' in t:
        lines = t.split('\n')
        for i in range(len(lines)):
            if 'Begin Construction' in lines[i] and '2022' in lines[i]:
                for j in range(i-1, max(i-8, -1), -1):
                    cand = lines[j].strip()
                    if cand and not cand.startswith('(') and len(cand) > 5:
                        spring_projects.add(cand)
                        break

# Match
matched = []
for p in spring_projects:
    if p in d:
        matched.append({'name': p, 'funding': d[p]})

count = len(matched)
if count == 0:
    result = 'No projects found'
else:
    total = sum(m['funding'] for m in matched)
    result = json.dumps({'project_count': count, 'total_funding': total, 'projects': matched})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
