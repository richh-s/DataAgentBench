code = """import json, re, os
funding_path = str(locals()['var_functions.query_db:6'])
civic_path = str(locals()['var_functions.query_db:8'])
with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    docs = json.load(f)
funding_set = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funding_set.add(r['Project_Name'].lower())
design_set = set()
for d in docs:
    txt = d.get('text','')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1: continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1: end = len(txt)
    section = txt[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
                if any(kw in line.lower() for kw in keywords):
                    design_set.add(line.lower())
count = 0
for proj in design_set:
    for fund in funding_set:
        if proj in fund or fund in proj:
            count += 1
            break
print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
