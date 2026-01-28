code = """import json, re

# Load data
funding = json.load(open(locals()['var_functions.query_db:6']))
docs = json.load(open(locals()['var_functions.query_db:8']))

# Build funding set (>$50000)
funding_names = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funding_names.add(r['Project_Name'].lower())

# Extract capital design projects
design_names = set()
for d in docs:
    txt = d.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(txt)
    section = txt[start:end]
    for line in section.splitlines():
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                keywords = ['road', 'park', 'drain', 'bridge', 'facility', 'system', 'plan', 'structure', 'study', 'improvements', 'repairs']
                if any(kw in line.lower() for kw in keywords):
                    design_names.add(line.lower())

# Count matches
count = 0
for proj in design_names:
    for fund in funding_names:
        if proj in fund or fund in proj:
            count += 1
            break

result = json.dumps({'count': count})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:78': {'test': 'success'}}

exec(code, env_args)
