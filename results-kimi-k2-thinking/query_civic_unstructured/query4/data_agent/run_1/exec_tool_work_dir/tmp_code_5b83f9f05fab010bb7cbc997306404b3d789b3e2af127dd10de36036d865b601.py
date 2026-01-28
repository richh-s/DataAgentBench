code = """import json

file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents:', len(civic_docs))

spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    for pattern in spring_patterns:
        if pattern in text:
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if pattern in line:
                    for j in range(max(0, i-5), i):
                        prev = lines[j].strip()
                        if prev and len(prev) > 5 and prev[0].isupper():
                            if 'Updates' not in prev and 'Schedule' not in prev and 'Agenda' not in prev:
                                spring_projects.append(prev)
                                break
            break

unique = list(set(spring_projects))
result = {'count': len(unique), 'projects': unique}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
