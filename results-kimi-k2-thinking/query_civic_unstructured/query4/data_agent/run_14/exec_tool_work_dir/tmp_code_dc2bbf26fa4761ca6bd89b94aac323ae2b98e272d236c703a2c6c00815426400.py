code = """import json

# Load data sources
civic_docs = locals().get('var_functions.query_db:2')
funding = locals().get('var_functions.query_db:5')

# Handle file paths
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

if isinstance(funding, str) and funding.endswith('.json'):
    with open(funding, 'r') as f:
        funding = json.load(f)

# Build funding map
funding_map = {}
for rec in funding:
    funding_map[rec['Project_Name'].strip().lower()] = int(rec['Amount'])

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '').lower()
    if '2022-spring' in text or '2022-march' in text or '2022-april' in text or '2022-may' in text:
        lines = doc.get('text', '').split('\n')
        for i, line in enumerate(lines):
            low = line.lower()
            if '2022-spring' in low or '2022-march' in low or '2022-april' in low or '2022-may' in low:
                project = None
                for j in range(i-1, max(i-4, -1), -1):
                    prev = lines[j].strip().replace('●', '').replace('■', '').strip()
                    bad = ['project schedule', 'updates:', 'complete design', 'advertise:', 'begin construction:']
                    if prev and len(prev) > 8 and not any(b in prev.lower() for b in bad) and not prev.startswith('('):
                        project = prev
                        break
                if project:
                    key = project.lower()
                    amount = funding_map.get(key, 0)
                    if amount == 0:
                        for k, v in funding_map.items():
                            if k in key or key in k:
                                amount = v
                                break
                    spring_projects.append({'name': project, 'funding': amount})

# Deduplicate
unique = {}
for p in spring_projects:
    name = p['name']
    if name not in unique or p['funding'] > 0:
        unique[name] = p

projects = list(unique.values())
count = len(projects)
total_funding = sum(p['funding'] for p in projects)

result = {'project_count': count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
