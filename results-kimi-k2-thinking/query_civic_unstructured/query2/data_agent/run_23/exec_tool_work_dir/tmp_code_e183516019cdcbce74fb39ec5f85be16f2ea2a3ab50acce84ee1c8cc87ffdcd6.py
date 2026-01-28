code = """import json

# Get civic docs data
civic_docs_data = locals()['var_functions.query_db:14']

# Load file if needed
if isinstance(civic_docs_data, str):
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

print('Docs count:', len(civic_docs_data))

# Look for 2022 completions
projects_2022 = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    if not text:
        continue
    
    text_lower = text.lower()
    if 'completed' in text_lower and '2022' in text_lower:
        # Extract lines around completed
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'completed' in line.lower() and '2022' in line:
                # Get project name (look up to 5 lines back)
                proj = None
                for j in range(i-1, max(-1, i-5), -1):
                    cand = lines[j].strip()
                    if cand and len(cand) < 80:
                        if not cand.startswith('(') and 'Updates:' not in cand:
                            proj = cand
                            break
                if proj:
                    projects_2022.append(proj)

# Deduplicate
unique = list(set(projects_2022))
print('Unique projects:', len(unique))

# Check for park-related
park = []
keywords = ['park', 'playground', 'walkway', 'shade', 'green', 'bluff', 'dume']
for p in unique:
    p_low = p.lower()
    if any(k in p_low for k in keywords):
        park.append(p)

print('Park projects found:', len(park))
for p in park:
    print('-', p)

result = {'park_projects': park, 'count': len(park)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
