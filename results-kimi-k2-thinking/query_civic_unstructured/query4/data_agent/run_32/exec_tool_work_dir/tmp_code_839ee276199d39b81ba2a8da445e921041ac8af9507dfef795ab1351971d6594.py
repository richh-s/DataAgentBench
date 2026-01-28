code = """import json, re

# Load data
civic = json.load(open(locals()['var_functions.query_db:6']))
funding = json.load(open(locals()['var_functions.query_db:5']))

# Funding lookup
funds = {}
for r in funding:
    name = r.get('Project_Name')
    if name:
        funds[name] = funds.get(name, 0) + int(r.get('Amount', 0))

# Find projects
found = set()
for doc in civic:
    txt = doc.get('text', '')
    if not txt or '2022' not in txt:
        continue
    
    lines = txt.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if line and line[0].isupper() and len(line) < 60:
            ctx = ' '.join(lines[i:i+8]).lower()
            if '2022' in ctx and ('spring' in ctx or 'march' in ctx or 'april' in ctx or 'may' in ctx):
                if all(x not in line.lower() for x in ['page', 'agenda', 'item', 'prepared', 'approved']):
                    found.add(line)

# Match
count = 0
total = 0
for p in found:
    if p in funds:
        count += 1
        total += funds[p]
    else:
        for f in funds:
            if p.lower() in f.lower():
                count += 1
                total += funds[f]
                break

result = {'count': count, 'total': total}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_documents': 5, 'status': 'loaded'}}

exec(code, env_args)
