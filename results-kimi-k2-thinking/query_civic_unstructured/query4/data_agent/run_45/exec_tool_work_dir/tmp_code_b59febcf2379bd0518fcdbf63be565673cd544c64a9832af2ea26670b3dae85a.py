code = """import json
docs_file = '/tmp/tmp_9m9q8o4.json'
with open(docs_file, 'r') as f:
    docs = json.load(f)
print('Loaded documents count:', len(docs))

spring_projects = []
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in docs:
    text = doc.get('text', '')
    has_spring = any(p in text for p in patterns)
    if has_spring:
        for line in text.split('\n'):
            line = line.strip()
            if line and 'Project' in line:
                uppercase_count = sum(1 for c in line if c.isupper())
                if uppercase_count > 3:
                    spring_projects.append(line)

unique_projects = list(set(spring_projects))
result = {'count': len(unique_projects), 'projects': unique_projects[:50]}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
