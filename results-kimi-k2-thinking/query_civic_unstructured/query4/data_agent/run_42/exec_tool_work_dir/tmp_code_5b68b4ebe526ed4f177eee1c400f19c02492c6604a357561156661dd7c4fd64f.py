code = """import json
import re

# Access the stored variables
mongo_path = locals()['var_functions.query_db:14']
funding_path = locals()['var_functions.query_db:4']

# Read data
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create funding lookup
d = {}
for rec in funding_records:
    d[rec['Project_Name']] = int(rec['Amount'])

# Find projects starting in Spring 2022
spring_projects = set()

for doc in mongo_docs:
    t = doc.get('text', '')
    if 'Spring' in t and '2022' in t:
        lines = t.split('\n')
        for i in range(len(lines)):
            if 'Begin Construction' in lines[i] and '2022' in lines[i]:
                # Look up to find project name
                for j in range(i-1, max(i-6, -1), -1):
                    cand = lines[j].strip()
                    if cand and not cand.startswith('(') and len(cand) > 5 and 'Schedule' not in cand:
                        spring_projects.add(cand)
                        break

# Match with funding data
matches = []
for p in spring_projects:
    if p in d:
        matches.append({'name': p, 'funding': d[p]})

count = len(matches)
if count == 0:
    result = json.dumps({'count': 0, 'total_funding': 0})
else:
    total = sum(m['funding'] for m in matches)
    result = json.dumps({'count': count, 'total_funding': total, 'projects': matches})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
