code = """import json
import re

# Read MongoDB file
mongo_docs = json.loads(open('/tmp/tmp9z4c2iv0.json').read())
funding_recs = json.loads(open('/tmp/tmps9c7b2d8.json').read())

# Build funding lookup
d = {}
for r in funding_recs:
    d[r['Project_Name']] = int(r['Amount'])

# Find Spring 2022 projects
spring = set()

for doc in mongo_docs:
    t = doc.get('text','')
    if 'Spring' in t and '2022' in t and 'Begin Construction' in t:
        lines = t.split('\n')
        for i in range(len(lines)):
            if 'Begin Construction' in lines[i] and '2022' in lines[i]:
                for j in range(i-1, max(i-10, -1), -1):
                    cand = lines[j].strip()
                    if cand and not cand.startswith('(') and 'Schedule' not in cand and len(cand) > 5:
                        spring.add(cand)
                        break

# Match with funding
matches = []
for p in spring:
    if p in d:
        matches.append({'name': p, 'funding': d[p]})

# Calculate result
count = len(matches)
total_funding = sum(m['funding'] for m in matches)

# Output in required format
result_string = 'Count=' + str(count) + ' TotalFunding=$' + str(total_funding)
print('__RESULT__:')
print(result_string)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
