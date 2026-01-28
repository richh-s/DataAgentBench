code = """import json
f_path = var_functions.query_db:64
c_path = var_functions.query_db:54
with open(f_path) as f:
    funding = json.load(f)
with open(c_path) as f:
    docs = json.load(f)

funding_names = [r['Project_Name'] for r in funding]
design_projects = []

for doc in docs:
    text = doc.get('text','').lower()
    s = text.find('capital improvement projects (design)')
    if s == -1:
        continue
    e = len(text)
    for m in ['capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects']:
        p = text.find(m, s)
        if p != -1 and p < e:
            e = p
    section = text[s:e]
    for line in section.split('\n'):
        cl = line.strip()
        if not cl or len(cl) < 10:
            continue
        ll = cl.lower()

        # Skip update lines
        if ll.find('updates:') > -1 or ll.find('schedule:') > -1 or ll.find('advertise:') > -1:
            continue
        if ll.find('staff') > -1 or ll.find('city') > -1 or ll.find('project is') > -1:
            continue
        if ll.startswith('to:') or ll.startswith('prepared') or ll.startswith('approved'):
            continue
        if '(cid' in ll or cl.startswith('('):
            continue

        # Skip date lines
        import re
        if re.search(r'\d{4}', ll) and len(cl.split()) <= 4:
            continue

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

print('__RESULT__:')
print(json.dumps(len(matched)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
