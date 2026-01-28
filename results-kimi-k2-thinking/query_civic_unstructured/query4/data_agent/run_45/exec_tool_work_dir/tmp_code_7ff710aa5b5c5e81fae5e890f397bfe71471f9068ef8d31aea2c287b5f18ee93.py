code = """import json, os, re
file_path = '/tmp/tmp_9m9q8o4.json'
docs = json.load(open(file_path))
spring = []
for d in docs:
    t = d.get('text','')
    if any(x in t for x in ['2022-Spring','2022-March','2022-April','2022-May']):
        for line in t.split('\n'):
            if 'Project' in line and sum(1 for c in line if c.isupper()) > 3:
                spring.append(line.strip())
unique = list(set(spring))
result = {'count': len(unique), 'projects': unique[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
