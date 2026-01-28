code = """import json, re, os

with open(var_functions.query_db:6, 'r') as f:
    funding = json.load(f)

with open(var_functions.query_db:8, 'r') as f:
    docs = json.load(f)

def clean(n):
    n = re.sub(r'\(FEMA[^\)]*\)', '', n, flags=2)
    n = re.sub(r'\(CalOES[^\)]*\)', '', n, flags=2)
    n = re.sub(r'\(CalJPIA[^\)]*\)', '', n, flags=2)
    n = re.sub(r'Project$', '', n, flags=2)
    return n.strip().lower()

funding_map = {}
for r in funding:
    if int(r['Amount']) > 50000:
        key = clean(r['Project_Name'])
        if key:
            funding_map[key] = True

design_project_names = set()
for d in docs:
    txt = d.get('text', '')
    start = txt.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end = txt.find('Capital Improvement Projects (Construction)', start)
    if end == -1:
        end = len(txt)
    section = txt[start:end]
    for line in section.split('\n'):
        line = line.strip()
        if len(line) > 10 and not line.startswith('(') and 'Capital Improvement' not in line:
            if 'FEMA' not in line and 'CalOES' not in line and 'CalJPIA' not in line:
                keywords = ['road','park','drain','bridge','facility','system','plan','structure','study','improvements','repairs','street','water','traffic']
                if any(kw in line.lower() for kw in keywords):
                    design_project_names.add(line)

matched = 0
for proj in design_project_names:
    cproj = clean(proj)
    for fkey in funding_map:
        if cproj in fkey or fkey in cproj:
            matched += 1
            break

print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
