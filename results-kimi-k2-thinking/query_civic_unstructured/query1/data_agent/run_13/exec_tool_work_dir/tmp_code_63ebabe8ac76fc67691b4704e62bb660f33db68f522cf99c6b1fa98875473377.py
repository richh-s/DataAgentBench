code = """import json, re
funding_path = '/tmp/tmpf6o4o9x2.json'
civic_path = '/tmp/tmpp3s6x5y4.json'
with open(funding_path) as f:
    funding = json.load(f)
with open(civic_path) as f:
    docs = json.load(f)
funding_names = [r['Project_Name'].lower() for r in funding]
design_projects = []
for doc in docs:
    txt = doc.get('text','').lower()
    s = txt.find('capital improvement projects (design)')
    if s == -1: continue
    e = len(txt)
    for m in ['capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects']:
        p = txt.find(m,s)
        if p != -1 and p < e: e = p
    section = txt[s:e]
    for line in section.split('\n'):
        cl = line.strip()
        if not cl or len(cl) < 10: continue
        ll = cl.lower()
        if ll.find('updates:') > -1 or ll.find('schedule:') > -1 or ll.find('advertise:') > -1: continue
        if ll.find('staff') > -1 or ll.find('city') > -1 or ll.find('project is') > -1: continue
        if ll.startswith('to:') or ll.startswith('prepared') or ll.startswith('approved'): continue
        if '(cid' in ll or cl.startswith('('): continue
        if re.search(r'\d{4}', ll) and len(cl.split()) <= 4: continue
        pname = cl.title().strip()
        if pname not in design_projects:
            design_projects.append(pname)
matched = []
for d in design_projects:
    d_core = d.lower().split('(')[0].strip()
    if d_core in funding_names and d not in matched:
        matched.append(d)
print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.query_db:80': 'file_storage/functions.query_db:80.json'}

exec(code, env_args)
