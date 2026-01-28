code = """import json
import re

# Read civic documents from file
civic_docs_path = 'mongo_result_civic_docs.json'
try:
    with open(civic_docs_path, 'r') as f:
        civic_docs_data = json.load(f)
except:
    # Try alternative path
    civic_docs_data = locals()['var_functions.query_db:14']
    if isinstance(civic_docs_data, str):
        with open(civic_docs_data, 'r') as f:
            civic_docs_data = json.load(f)

print('Loaded', len(civic_docs_data), 'documents')

completed_projects = []

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
        # Check for completion in 2022
        if 'completed' in line_lower and '2022' in line:
            # Find project name by looking backward
            project_name = None
            for j in range(i-1, max(-1, i-6), -1):
                prev_line = lines[j].strip()
                if prev_line and len(prev_line) < 100:
                    # Skip bullet points and headers
                    if not any(prev_line.startswith(x) for x in ['(', '●', '■', '\xe2\x97\x8f', '\xe2\x96\xa0']):
                        if all(x not in prev_line for x in ['Updates:', 'Project Schedule:', 'RECOMMENDED ACTION:', 'DISCUSSION:']):
                            project_name = prev_line
                            break
            
            if project_name:
                completed_projects.append({
                    'name': project_name,
                    'note': line
                })

# Remove duplicates
unique = []
seen = set()
for p in completed_projects:
    if p['name'] not in seen:
        unique.append(p)
        seen.add(p['name'])

print('Found', len(unique), 'completed projects in 2022')

# Filter for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park_projects = []

for proj in unique:
    name_lower = proj['name'].lower()
    if any(kw in name_lower for kw in park_keywords):
        park_projects.append(proj)

print('Found', len(park_projects), 'park-related projects:')
for p in park_projects:
    print(' -', p['name'])

result = {
    'park_projects': park_projects,
    'total_park_projects': len(park_projects)
}

# Store for next step
with open('park_projects_2022.json', 'w') as f:
    json.dump(park_projects, f)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
