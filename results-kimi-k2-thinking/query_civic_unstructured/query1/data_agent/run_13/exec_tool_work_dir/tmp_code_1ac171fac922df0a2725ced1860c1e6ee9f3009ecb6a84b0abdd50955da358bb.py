code = """import json, re

funding_path = var_functions.query_db:64
civic_path = var_functions.query_db:54

with open(funding_path) as f:
    funding = json.load(f)

with open(civic_path) as f:
    docs = json.load(f)

funding_names = [r['Project_Name'] for r in funding]

design_projects = []

for doc in docs:
    t = doc.get('text','').lower()
    s = t.find('capital improvement projects (design)')
    if s == -1: continue
    
    e = len(t)
    for m in ['capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects']:
        p = t.find(m,s)
        if p != -1 and p < e: e = p
    
    section = t[s:e]
    for line in section.split('\n'):
        cl = line.strip()
        if not cl or len(cl) < 10: continue
        
        ll = cl.lower()
        
        skip = False
        for kw in ['updates:','schedule:','advertise:','staff','city','project is']:
            if kw in ll: skip = True
        if skip: continue
        
        for prefix in ['to:','prepared','approved','date','meeting','subject:','agenda','item','page','public works','commission']:
            if ll.startswith(prefix): skip = True
        if skip: continue
        
        if '(cid' in ll or cl.startswith('('): continue
        
        if re.search(r'\d{4}',ll) and len(cl.split()) <= 4: continue
        
        pname = cl.title().strip()
        if pname not in design_projects:
            design_projects.append(pname)

matched = []
for d in design_projects:
    d_core = d.lower().split('(')[0].strip()
    for f in funding_names:
        f_core = f.lower().split('(')[0].strip()
        if d_core == f_core and d not in matched:
            matched.append(d)
            break

count = len(matched)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
