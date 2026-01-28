code = """import json

mkey = 'var_functions.query_db:42'
fkey = 'var_functions.query_db:4'

mongo_path = locals()[mkey]
funding_path = locals()[fkey]

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

funding_lookup = {}
for rec in funding_recs:
    funding_lookup[rec['Project_Name']] = int(rec['Amount'])

spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                for j in range(i-1, max(i-8, -1), -1):
                    cand = lines[j].strip()
                    if cand and cand[0] != '(' and 'Schedule' not in cand:
                        spring_projects.add(cand)
                        break

matches = []
for proj in spring_projects:
    if proj in funding_lookup:
        matches.append({'name': proj, 'funding': funding_lookup[proj]})

count = len(matches)
total = sum(m['funding'] for m in matches)

result = {"project_count": count, "total_funding": total}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
