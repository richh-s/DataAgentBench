code = """import json

docs = json.load(open('/tmp/tmp_9m9q8o4.json'))
print('Loaded docs:', len(docs))

spring = []
for d in docs:
    t = d.get('text','')
    if '2022-Spring' in t or '2022-March' in t or '2022-April' in t or '2022-May' in t:
        lines = t.split('\n')
        for L in lines:
            L = L.strip()
            if L and 'Project' in L:
                u = sum(1 for c in L if c.isupper())
                if u>3:
                    spring.append(L)

u = list(set(spring))
print('Spring projects:', len(u))
result = {'cnt':len(u), 'projs':u[:50]}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
