code = """import json
import re

# Get the civic documents data  
civic_docs_result = locals()['var_functions.query_db:14']

# If it's a string (file path), read it
if isinstance(civic_docs_result, str):
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

print('Civic docs loaded:', len(civic_docs_data))

# Find completed projects in 2022
completed_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_clean = line.strip()
        if not line_clean:
            continue
        
        # Check for completion in 2022 (case insensitive)
        if 'completed' in line_clean.lower() and '2022' in line_clean:
            # Look back for project name
            project_name = None
            
            for j in range(i-1, max(-1, i-5), -1):
                prev = lines[j].strip()
                if prev and len(prev) < 100:
                    # Skip formatting lines
                    bad_start = ['(', '●', '■', '·', '◆', '◈']
                    bad_content = ['Updates:', 'Project Schedule:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'Subject:', 'To:']
                    
                    if not any(prev.startswith(s) for s in bad_start):
                        if not any(bc in prev for bc in bad_content):
                            project_name = prev
                            break
            
            if project_name:
                completed_2022.append({
                    'name': project_name,
                    'completion': line_clean
                })

# Remove duplicates
unique_names = set()
unique_projects = []

for p in completed_2022:
    if p['name'] not in unique_names:
        unique_names.add(p['name'])
        unique_projects.append(p)

print('Unique projects completed in 2022:', len(unique_projects))

# Filter for park-related projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume', 'canyon']
park_projects = []

for proj in unique_projects:
    name_lower = proj['name'].lower()
    if any(kw in name_lower for kw in park_keywords):
        park_projects.append(proj)

print('Park-related projects:', len(park_projects))
for p in park_projects:
    print(' -', p['name'])

result = {
    'park_projects_2022': park_projects,
    'count': len(park_projects)
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
