code = """import json

mongo_path = locals()['var_functions.query_db:42']
funding_path = locals()['var_functions.query_db:4']

f = open(mongo_path)
mongo_docs = json.load(f)
f.close()

f = open(funding_path)
funding_recs = json.load(f)
f.close()

funding_lookup = {r['Project_Name']: int(r['Amount']) for r in funding_recs}

spring_projects = set()

for doc in mongo_docs:
    text = doc.get('text', '')
    if 'Spring' in text and '2022' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i]
            if 'Begin Construction' in line and '2022' in line:
                for j in range(i-1, max(i-6, -1), -1):
                    cand = lines[j].strip()
                    if cand and not cand.startswith('(') and 'Schedule' not in cand:
                        if len(cand) > 5:
                            spring_projects.add(cand)
                            break

matches = [{'name': p, 'funding': funding_lookup[p]} for p in spring_projects if p in funding_lookup]

count = len(matches)
total_funding = sum(m['funding'] for m in matches)

result = json.dumps({'project_count': count, 'total_funding': total_funding})

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json'}

exec(code, env_args)
