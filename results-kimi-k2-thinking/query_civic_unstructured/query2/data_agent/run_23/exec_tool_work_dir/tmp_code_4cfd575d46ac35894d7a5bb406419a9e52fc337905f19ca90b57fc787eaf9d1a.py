code = """import json
import re

# Load civic documents data
civic_docs_data = locals()['var_functions.query_db:14']
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print('Loaded', len(civic_docs_data), 'documents')

# Find projects completed in 2022
completed_2022 = []
seen_names = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check if line mentions completion in 2022
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line:
            # Find project name (look back up to 5 lines)
            project_name = None
            for j in range(i-1, max(-1, i-6), -1):
                prev = lines[j].strip()
                if prev and len(prev) < 80:
                    if prev.startswith('('):
                        continue
                    if 'Updates:' in prev:
                        continue
                    if 'Schedule:' in prev:
                        continue
                    if 'RECOMMENDED' in prev:
                        continue
                    project_name = prev
                    break
            
            if project_name and project_name not in seen_names:
                seen_names.add(project_name)
                completed_2022.append({'name': project_name, 'note': line})

print('Completed in 2022:', len(completed_2022))

# Identify park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park_projects = []
for proj in completed_2022:
    name_lower = proj['name'].lower()
    if any(k in name_lower for k in park_keywords):
        park_projects.append(proj['name'])

print('Park projects:', len(park_projects))
for name in park_projects:
    print(' -', name)

result = {'park_projects': park_projects, 'count': len(park_projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
