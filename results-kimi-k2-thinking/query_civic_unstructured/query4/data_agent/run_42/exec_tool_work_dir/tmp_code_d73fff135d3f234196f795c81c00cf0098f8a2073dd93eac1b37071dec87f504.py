code = """import json
import re

# Load data from files
mongo_path = locals()['var_functions.query_db:42']
funding_path = locals()['var_functions.query_db:4']

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Build funding lookup
d = {}
for r in funding_recs:
    d[r['Project_Name']] = int(r['Amount'])

# Extract Spring 2022 projects
spring = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if 'Begin Construction' in line and '2022' in line:
            for j in range(i-1, max(i-8, -1), -1):
                cand = lines[j].strip()
                if cand and cand[0] != '(' and 'Schedule' not in cand:
                    if len(cand) > 5:
                        spring.add(cand)
                        break

# Match projects with funding
matches = []
for p in spring:
    if p in d:
        matches.append({'name': p, 'funding': d[p]})

count = len(matches)
total = sum(m['funding'] for m in matches)

result = json.dumps({'project_count': count, 'total_funding': total})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
