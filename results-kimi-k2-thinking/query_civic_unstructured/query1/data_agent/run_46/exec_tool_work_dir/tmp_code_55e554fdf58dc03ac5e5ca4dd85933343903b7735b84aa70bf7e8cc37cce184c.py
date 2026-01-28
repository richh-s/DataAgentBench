code = """import json, re

funding = json.load(open(str(locals()['var_functions.query_db:6'])))
docs = json.load(open(str(locals()['var_functions.query_db:8'])))

funding_names = set()
for r in funding:
    if int(r['Amount']) > 50000:
        funding_names.add(r['Project_Name'].lower())

design_names = set()
for d in docs:
    txt = d.get('text','')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1: continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1: end = len(txt)
    for line in txt[start:end].split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line and 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
            keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs']
            if any(kw in line.lower() for kw in keywords):
                design_names.add(line.lower())

count = sum(1 for proj in design_names if any(p in f or f in p for p in [proj] for f in funding_names))

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
