code = """import json
civic_docs = json.load(open('/tmp/tmp_9m9q8o4.json'))
print('Loaded', len(civic_docs))

spring = []
for doc in civic_docs:
    text = doc.get('text','')
    if '2022-Spring' in text or '2022-March' in text or '2022-April' in text or '2022-May' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                upper = sum(1 for c in line if c.isupper())
                if upper > 3:
                    spring.append(line)

unique = list(set(spring))
result = {'count': len(unique), 'projects': unique[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
