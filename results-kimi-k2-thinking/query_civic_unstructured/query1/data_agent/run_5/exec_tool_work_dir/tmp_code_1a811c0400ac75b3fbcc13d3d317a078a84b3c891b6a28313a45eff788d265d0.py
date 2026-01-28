code = """import json

with open(locals()['var_functions.query_db:72']) as f:
    funding_records = json.load(f)

with open(locals()['var_functions.query_db:2']) as f:
    civic_docs = json.load(f)

# Projects with funding > 50k
funded = {}
for rec in funding_records:
    funded[rec['Project_Name']] = int(rec['Amount'])

print('Funded:', len(funded))

# Extract design projects
design = []
for doc in civic_docs:
    t = doc.get('text', '')
    a = t.find('Projects (Design)')
    if a > 0:
        b = t[a:a+3000]
        parts = b.split('\n\n')
        for p in parts[:20]:
            if p and len(p) > 20:
                line = p.split('\n')[0]
                if line and 'Design)' not in line and 'Project' in line:
                    design.append(line[:100])

print('Design:', len(design))

# Match by counting exact or similar name matches
matched = 0
for dname in design:
    dnorm = dname.split('(')[0].lower().replace('project', '').strip()[:30]
    for fund in list(funded.keys()):
        fnorm = fund.split('(')[0].lower().replace('project', '').strip()[:30]
        if dnorm in fnorm or fnorm in dnorm:
            matched += 1
            del funded[fund]
            break

print('Matched:', matched)
print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
