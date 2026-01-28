code = """import json, re

# Load data from files
with open(var_functions.query_db:6, 'r') as f:
    funding = json.load(f)
with open(var_functions.query_db:8, 'r') as f:
    docs = json.load(f)

# Filter funding > 50000
funding_names = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funding_names.add(r['Project_Name'].lower())

# Extract design projects from civic docs
design_projects = set()
for d in docs:
    t = d.get('text','')
    start = t.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = t.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(t)
    
    section = t[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                if any(kw in line.lower() for kw in ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic']):
                    design_projects.add(line)

# Count matches
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for fund in funding_names:
        if proj_lower in fund or fund in proj_lower:
            count += 1
            break

print('__RESULT__:')
print(json.dumps({'count':count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
