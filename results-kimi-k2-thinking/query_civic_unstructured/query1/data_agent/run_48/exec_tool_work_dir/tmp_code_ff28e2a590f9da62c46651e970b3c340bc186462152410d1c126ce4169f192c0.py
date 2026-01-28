code = """import json
f1 = str(var_functions.query_db:0)
with open(f1) as f:
    funding = json.load(f)

f2 = str(var_functions.query_db:2)
with open(f2) as f:
    docs = json.load(f)

# Projects with funding > 50k
high_funding = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.append(r['Project_Name'])

# Extract design project names
design_projects = []
for doc in docs:
    text = doc.get('text', '')
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        section = text[design_start:]
        parts = section.split('\n\n')
        for part in parts:
            part = part.strip()
            if len(part) > 10:
                name = part.split('\n')[0].strip()
                if len(name) > 10 and not name.isupper():
                    design_projects.append(name)

# Match
matched = 0
for proj in design_projects:
    plower = proj.lower()
    for fund in high_funding:
        flower = fund.lower()
        if plower == flower or proj in fund or fund in proj:
            matched += 1
            break
        if len(plower.split()) >= 3 and len(flower.split()) >= 3:
            commons = set(plower.split()) & set(flower.split())
            if len(commons) >= 2:
                matched += 1
                break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
