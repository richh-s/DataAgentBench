code = """import json, re

with open('var_functions.query_db:30') as f:
    funding = json.load(f)

with open('var_functions.query_db:31') as f:
    docs = json.load(f)

fund = {}
for r in funding:
    amt = int(r.get('Amount', 0))
    if amt > 50000:
        name = r.get('Project_Name', '').strip()
        if name:
            fund[name.lower()] = name

projs = []
for doc in docs:
    t = doc.get('text', '')
    s = t.find('Capital Improvement Projects (Design)')
    if s == -1:
        continue
    e = len(t)
    for m in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']:
        p = t.find(m, s + 50)
        if s < p < e:
            e = p
    section = t[s:e]
    lines = section.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        if line.startswith('cid:') or 'Updates:' in line or 'Project Schedule:' in line:
            continue
        if line.isupper() and len(line.split()) <= 3:
            continue
        if line[0].isupper() and len(line.split()) >= 2:
            valid = False
            for j in range(i + 1, min(i + 4, len(lines))):
                nxt = lines[j].lower()
                if 'updates:' in nxt or 'project schedule:' in nxt:
                    valid = True
                    break
            if not valid:
                if any(k in line for k in ['Project', 'Improvements', 'Drainage', 'Repairs']):
                    valid = True
            if valid and line not in projs:
                projs.append(line)

matches = []
for p in projs:
    pk = p.lower()
    if pk in fund:
        matches.append(p)
    else:
        for fk in fund:
            if pk in fk or fk in pk:
                pw = set(pk.split())
                fw = set(fk.split())
                if len(pw.intersection(fw)) >= 2:
                    matches.append(p)
                    break

unique = list(set(matches))
result = len(unique)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:19': 'file_storage/functions.query_db:19.json', 'var_functions.list_db:28': ['civic_docs'], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json'}

exec(code, env_args)
