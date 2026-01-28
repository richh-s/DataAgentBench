code = """import json
file_path = locals()['var_functions.query_db:2']
print('File path:', file_path)

civic_docs = json.load(open(file_path))
print('Loaded', len(civic_docs), 'documents')

spring_2022_projects = []
patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    if any(pat in text for pat in patterns):
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line and 'Project' in line:
                upper = sum(1 for c in line if c.isupper())
                if upper > 3:
                    spring_2022_projects.append(line[:200])

unique_projects = list(set(spring_2022_projects))
result = {'spring_2022_count': len(unique_projects), 'projects': unique_projects[:50]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
