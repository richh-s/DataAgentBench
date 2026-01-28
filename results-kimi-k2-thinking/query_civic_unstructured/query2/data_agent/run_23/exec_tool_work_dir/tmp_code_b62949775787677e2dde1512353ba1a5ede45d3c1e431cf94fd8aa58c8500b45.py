code = """import json
import re

# Load civic documents
civic_docs_result = locals()['var_functions.query_db:14']
if isinstance(civic_docs_result, str):
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

print('Loaded %d documents' % len(civic_docs_data))

# Extract projects completed in 2022
projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line:
            project_name = None
            # Look back up to 5 lines for project name
            for j in range(i-1, max(-1, i-5), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) < 80:
                    # Skip formatting lines
                    if prev_line.startswith('('):
                        continue
                    if 'Updates:' in prev_line or 'Schedule:' in prev_line:
                        continue
                    if 'RECOMMENDED' in prev_line:
                        continue
                    project_name = prev_line
                    break
            
            if project_name and project_name not in [p['name'] for p in projects_2022]:
                projects_2022.append({'name': project_name, 'note': line})

print('Completed in 2022: %d' % len(projects_2022))

# Filter for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park_projects = []
for proj in projects_2022:
    name_lower = proj['name'].lower()
    if any(keyword in name_lower for keyword in park_keywords):
        park_projects.append(proj['name'])

print('Park projects: %d' % len(park_projects))
for p in park_projects:
    print(' - %s' % p)

result = {
    'park_project_names': park_projects,
    'count': len(park_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
