code = """import json, re

file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('Total documents:', len(civic_docs))

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']
    
    for pattern in spring_patterns:
        if pattern in text:
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if pattern in line:
                    for j in range(max(0, i-5), i):
                        prev_line = lines[j].strip()
                        if prev_line and len(prev_line) > 5 and prev_line[0].isupper():
                            if 'Updates' not in prev_line and 'Schedule' not in prev_line and 'Agenda' not in prev_line:
                                spring_projects.append(prev_line)
                                break
                    break

unique_spring_projects = list(set(spring_projects))
print('Spring 2022 projects:', len(unique_spring_projects))
for i, proj in enumerate(unique_spring_projects[:10]):
    print(i+1, proj)

result = {'spring_projects': unique_spring_projects, 'count': len(unique_spring_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
