code = """import json
docs = json.load(open('/tmp/tmp_9m9q8o4.json'))
print('loaded', len(docs))

spring_projects = []
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for d in docs:
    t = d.get('text', '')
    for pat in patterns:
        if pat in t:
            lines = d.get('text', '').split('\n')
            for line in lines:
                L = line.strip()
                if L and 'Project' in L and L.isupper():
                    spring_projects.append(L)
            break

unique = list(set(spring_projects))
result = {'count': len(unique), 'first_few': unique[:10]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
