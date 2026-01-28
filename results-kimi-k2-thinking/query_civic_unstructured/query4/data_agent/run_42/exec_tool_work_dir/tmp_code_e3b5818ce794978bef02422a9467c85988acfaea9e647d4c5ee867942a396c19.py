code = """import json

# Load the data from files
with open('/tmp/tmp9z4c2iv0.json', 'r') as f:
    mongo_docs = json.load(f)

with open('/tmp/tmps9c7b2d8.json', 'r') as f:
    funding_recs = json.load(f)

# Build funding lookup
d = {r['Project_Name']: int(r['Amount']) for r in funding_recs}

spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        if 'Begin Construction' in line and '2022' in line:
            for j in range(i-1, max(i-8, -1), -1):
                cand = lines[j].strip()
                if cand and cand[0] != '(' and 'Schedule' not in cand and len(cand) > 5:
                    spring_projects.add(cand)
                    break

matches = [{'name': p, 'funding': d[p]} for p in spring_projects if p in d]

count = len(matches)
total = sum(m['funding'] for m in matches)

print('__RESULT__:')
print(json.dumps({'project_count': count, 'total_funding': total}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
