code = """import json

# Load MongoDB results
f = open(locals()['var_functions.query_db:42'])
mongo_docs = json.load(f)
f.close()

# Load funding data
f = open(locals()['var_functions.query_db:4'])
funding_recs = json.load(f)
f.close()

# Build funding lookup
d = {}
for r in funding_recs:
    d[r['Project_Name']] = int(r['Amount'])

spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            if 'Begin Construction' in lines[i] and '2022' in lines[i]:
                for j in range(i-1, max(i-6, -1), -1):
                    cand = lines[j].strip()
                    if cand and cand[0] != '(' and 'Schedule' not in cand:
                        if len(cand) > 5:
                            spring_projects.add(cand)
                            break

matches = []
for p in spring_projects:
    if p in d:
        matches.append({'name': p, 'funding': d[p]})

count = len(matches)
total = sum(m['funding'] for m in matches)

result = json.dumps({'count': count, 'total_funding': total})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
