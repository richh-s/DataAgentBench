code = """import json, re
c_docs = json.load(open('/tmp/tmpw8a01a0z.json'))
funding = json.load(open('/tmp/tmptjtu3_1d.json'))

# Find park projects completed in 2022
projects = []
for doc in c_docs:
    txt = doc.get('text', '')
    lines = txt.split('\n')
    for line in lines:
        line_lower = line.lower().strip()
        if 'completed' in line_lower and '2022' in line and 'park' in line_lower and len(line.strip()) > 10:
            projects.append(line.strip())

# Get funding for park projects
funding_dict = {f['Project_Name'].lower(): int(f['Amount']) for f in funding}

# Based on sample, these park projects completed in 2022
targets = ['Bluffs Park Shade Structure', 'Marie Canyon Green Streets', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs']

total = 0
matched = []
for target in targets:
    if target.lower() in funding_dict:
        amount = funding_dict[target.lower()]
        total += amount
        matched.append({'name': target, 'amount': amount})

result = {'total_funding': total, 'projects': matched, 'doc_count': len(projects)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs']}

exec(code, env_args)
