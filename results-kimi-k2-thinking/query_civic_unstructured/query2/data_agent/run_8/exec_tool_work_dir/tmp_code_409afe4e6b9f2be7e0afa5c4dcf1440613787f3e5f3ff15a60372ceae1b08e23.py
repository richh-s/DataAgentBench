code = """import json, re

civic_path = locals()['var_functions.query_db:0']
funding_path = locals()['var_functions.query_db:1']

# Load data
with open(civic_path) as f1:
    civic_docs = json.load(f1)
with open(funding_path) as f2:
    funding = json.load(f2)

# Extract park projects
park_projects = []
for doc in civic_docs:
    lines = doc.get('text', '').split('\n')
    for line in lines:
        l = line.lower()
        if 'park' in l and 'completed' in l and '2022' in l:
            park_projects.append(line.strip())

park_projects = list(set(park_projects))

# Find funding
total = 0
for p in park_projects:
    key = p.split()[0].lower()
    for f in funding:
        name = f['Project_Name'].lower()
        if 'park' in name and key in name:
            total += int(f['Amount'])

print('__RESULT__:')
print(json.dumps({'total_funding': total}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
