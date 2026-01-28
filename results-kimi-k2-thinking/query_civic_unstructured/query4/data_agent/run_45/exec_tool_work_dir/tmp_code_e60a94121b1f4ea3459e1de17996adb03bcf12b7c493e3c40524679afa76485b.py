code = """import json
import os

docs_file = locals()['var_functions.query_db:2']
print('Loading documents')

with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'documents')

spring_projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May']

for doc in civic_docs:
    text = doc.get('text', '')
    has_spring = any(p in text for p in spring_patterns)
    if has_spring:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                upper_count = sum(1 for c in line if c.isupper())
                if upper_count > 3:
                    spring_projects.append(line[:150])

result_data = {
    'count': len(spring_projects),
    'projects': list(set(spring_projects))[:20]
}

print('Projects found:', len(spring_projects))

output = '.__RESULT__.:\n' + json.dumps(result_data)
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
