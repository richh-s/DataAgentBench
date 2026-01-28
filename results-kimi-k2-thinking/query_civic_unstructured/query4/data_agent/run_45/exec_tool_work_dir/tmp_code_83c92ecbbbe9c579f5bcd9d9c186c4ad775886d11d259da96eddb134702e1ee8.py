code = """import json
docs_file = '/tmp/tmp_9m9q8o4.json'
docs = json.load(open(docs_file))
print('Loaded', len(docs))

projs = []
for d in docs:
    t = d.get('text','')
    has_spring = False
    for pat in ['2022-Spring','2022-March','2022-April','2022-May']:
        if pat in t:
            has_spring = True
            break
    if has_spring:
        for line in t.split('\n'):
            line = line.strip()
            if line and 'Project' in line:
                u = sum(1 for c in line if c.isupper())
                if u > 3:
                    projs.append(line)

unique = list(set(projs))
result = {'cnt': len(unique), 'list': unique[:30]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
