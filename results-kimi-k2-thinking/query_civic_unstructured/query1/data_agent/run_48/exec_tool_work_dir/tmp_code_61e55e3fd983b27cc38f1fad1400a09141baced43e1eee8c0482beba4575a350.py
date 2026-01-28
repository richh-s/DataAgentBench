code = """import json

f1 = open(var_functions.query_db:0)
funding = json.load(f1)
f1.close()

f2 = open(var_functions.query_db:2)
docs = json.load(f2)
f2.close()

high_funding = []
for r in funding:
    if int(r['Amount']) > 50000:
        high_funding.append(r['Project_Name'])

design_projects = []
for doc in docs:
    txt = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in txt:
        continue
    dstart = txt.find('Capital Improvement Projects (Design)')
    dsection = txt[dstart + 37:]
    end = len(dsection)
    for m in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        p = dsection.find(m)
        if p > 0 and p < end:
            end = p
    dsection = dsection[:end]
    blocks = dsection.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            first = block.split('\n')[0].strip()
            if len(first) > 10 and not first.isupper():
                design_projects.append(first)

matched = 0
for proj in design_projects:
    pl = proj.lower()
    for fund in high_funding:
        fl = fund.lower()
        if pl == fl or proj in fund or fund in proj:
            matched += 1
            break
        if len(pl.split()) >= 2 and len(fl.split()) >= 2:
            if len(set(pl.split()) & set(fl.split())) >= 2:
                matched += 1
                break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
