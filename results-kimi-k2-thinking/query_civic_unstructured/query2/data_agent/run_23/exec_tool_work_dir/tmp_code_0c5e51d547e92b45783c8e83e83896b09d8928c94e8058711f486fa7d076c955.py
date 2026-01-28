code = """import json
import re

# Get civic documents data
civic_docs_result = locals()['var_functions.query_db:14']

# Load if it's a file path
if isinstance(civic_docs_result, str):
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

print('Loaded', len(civic_docs_data), 'documents')

# Find all projects with completion dates in 2022
completed_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(min(50, len(lines))):  # Limit to avoid issues
        line = lines[i].strip()
        if not line:
            continue
        
        # Check for 2022 completion
        if 'completed' in line.lower() and '2022' in line:
            # Find project name
            proj_name = None
            for j in range(i-1, max(-1, i-4), -1):
                prev = lines[j].strip()
                if prev and len(prev) < 80:
                    if not prev.startswith('(') and not prev.startswith('●'):
                        if 'Updates:' not in prev and 'Schedule:' not in prev:
                            proj_name = prev
                            break
            
            if proj_name:
                completed_2022.append({'name': proj_name, 'note': line})

# Remove duplicates
seen = set()
unique = []
for p in completed_2022:
    if p['name'] not in seen:
        seen.add(p['name'])
        unique.append(p)

print('Found', len(unique), 'completed in 2022')

# Park keywords
park_words = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park_projs = []

for p in unique:
    name = p['name'].lower()
    if any(w in name for w in park_words):
        park_projs.append(p)

print('Park projects:', len(park_projs))
for p in park_projs:
    print(p['name'])

result = {
    'park_projects': park_projs,
    'count': len(park_projs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
