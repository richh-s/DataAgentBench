code = """import json
civic_docs = json.load(open('/tmp/tmp_9m9q8o4.json'))
print('Loaded docs:', len(civic_docs))

spring = []
for doc in civic_docs:
    txt = doc.get('text','')
    if '2022-Spring' in txt or '2022-March' in txt or '2022-April' in txt or '2022-May' in txt:
        for L in txt.split('\n'):
            L = L.strip()
            if L and 'Project' in L:
                up = sum(1 for c in L if c.isupper())
                if up > 3:
                    spring.append(L)

unique = list(set(spring))[:50]
print('Spring projects:', len(unique))
print('__RESULT__:')
print(json.dumps({'count': len(unique), 'projects': unique}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
