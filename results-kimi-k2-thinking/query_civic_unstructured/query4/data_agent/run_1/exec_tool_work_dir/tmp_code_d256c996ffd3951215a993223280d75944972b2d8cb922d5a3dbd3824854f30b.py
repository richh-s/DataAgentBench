code = """import json
with open(var_functions.query_db:5, 'r') as f:
    civic_docs = json.load(f)

print('Documents found:', len(civic_docs))

spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and ('Spring' in line or 'March' in line or 'April' in line or 'May' in line or '2022-03' in line or '2022-04' in line or '2022-05' in line):
                for j in range(max(0, i-3), i):
                    prev = lines[j].strip()
                    if prev and len(prev) > 5 and prev[0].isupper() and 'Updates' not in prev and 'Schedule' not in prev:
                        spring_2022_projects.append(prev)
                        break

unique_projects = list(set(spring_2022_projects))
result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
