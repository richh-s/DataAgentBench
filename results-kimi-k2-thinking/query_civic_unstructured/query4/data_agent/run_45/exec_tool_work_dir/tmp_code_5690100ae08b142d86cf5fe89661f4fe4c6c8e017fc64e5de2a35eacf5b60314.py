code = """import json

docs_file = locals()['var_functions.query_db:2']
civic_docs = json.load(open(docs_file))
print('Loaded documents count:', len(civic_docs))

spring_2022_projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    text = doc.get('text', '')
    has_spring = any(pattern in text for pattern in spring_patterns)
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line and sum(1 for c in line if c.isupper()) > 3:
                spring_2022_projects.append(line[:200])

unique_projects = list(set(spring_2022_projects))
result = {'spring_2022_count': len(unique_projects), 'project_names': unique_projects[:30]}

print('__RESULT__:') 
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
