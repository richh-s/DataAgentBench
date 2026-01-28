code = """import json, re

# Load civic docs
civic_docs_result = locals()['var_functions.query_db:14']
if isinstance(civic_docs_result, str):
    with open(civic_docs_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = civic_docs_result

print('Loaded %d documents' % len(civic_docs_data))

# Find projects completed in 2022
completed = []
seen = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Check for 2022 completion
        line_lower = line.lower()
        if 'completed' in line_lower and '2022' in line:
            # Find project name
            proj_name = None
            for j in range(i-1, max(-1, i-6), -1):
                prev = lines[j].strip()
                if prev and len(prev) < 80:
                    if prev.startswith('(') or 'Updates:' in prev or 'Schedule:' in prev or 'RECOMMENDED' in prev:
                        continue
                    proj_name = prev
                    break
            
            if proj_name and proj_name not in seen:
                seen.add(proj_name)
                completed.append({'name': proj_name, 'note': line})

print('Completed in 2022: %d' % len(completed))

# Filter park projects
park_keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
park = []
for p in completed:
    name = p['name'].lower()
    if any(k in name for k in park_keywords):
        park.append(p['name'])

print('Park projects: %d' % len(park))
for p in park:
    print(' - %s' % p)

result = {'projects': park, 'count': len(park)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
