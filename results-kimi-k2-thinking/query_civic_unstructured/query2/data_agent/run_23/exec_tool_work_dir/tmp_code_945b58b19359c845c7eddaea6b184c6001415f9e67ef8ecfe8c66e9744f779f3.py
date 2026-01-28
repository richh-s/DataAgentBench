code = """import json, re

# Load civic documents
civic_docs = locals()['var_functions.query_db:14']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'documents')

# Find projects completed in 2022
all_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        line_lc = line.lower()
        if 'completed' in line_lc and '2022' in line:
            # Find project name
            proj = None
            for j in range(i-1, max(-1, i-6), -1):
                prev = lines[j].strip()
                if prev and len(prev) < 80:
                    if not prev.startswith('('):
                        if all(x not in prev for x in ['Updates:', 'Schedule:', 'RECOMMENDED']):
                            proj = prev
                            break
            if proj and proj not in [p['name'] for p in all_projects]:
                all_projects.append({'name': proj, 'completion': line})

print('Completed in 2022:', len(all_projects))

# Filter park projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park_projects = []
for p in all_projects:
    name = p['name'].lower()
    if any(k in name for k in park_keywords):
        park_projects.append(p['name'])

print('Park projects:', len(park_projects))
for p in park_projects:
    print(' -', p)

result = {'projects': park_projects, 'count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
