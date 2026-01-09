code = """import json, re

# load funding project names >50k
p = var_call_Bqxm38LOT1pz4NEqbD4bvNeK
if isinstance(p, str) and p.endswith('.json'):
    with open(p, 'r', encoding='utf-8') as f:
        funding_names = json.load(f)
else:
    funding_names = p
funding_set = {d.get('Project_Name') for d in funding_names}
funding_set.discard(None)

# load civic docs
p2 = var_call_5OGYeOICM5QNI2M9LpSCiuKR
if isinstance(p2, str) and p2.endswith('.json'):
    with open(p2, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = p2

status_design_projects = set()
for doc in docs:
    t = (doc.get('text') or '').replace('\r','')
    m = re.search(r'Capital Improvement Projects\s*\(Design\)', t, flags=re.IGNORECASE)
    if not m:
        continue
    after = t[m.end():]
    stop = re.search(r'Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects', after, flags=re.IGNORECASE)
    if stop:
        after = after[:stop.start()]
    lines = [ln.strip() for ln in after.split('\n')]

    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.match(r'^[\(\[\{\*\-\u2022\u00b7\u2023]', ln):
            continue
        low = ln.lower()
        if low in {'updates:', 'project schedule:', 'estimated schedule:', 'project description:', 'discussion:', 'recommended action:'}:
            continue
        if len(ln) > 120:
            continue
        look = '\n'.join(lines[i+1:i+6]).lower()
        if ('updates' in look) or ('project schedule' in look) or ('estimated schedule' in look) or ('project description' in look):
            title = re.sub(r'\s+', ' ', ln).strip()
            status_design_projects.add(title)

matched = sorted(status_design_projects & funding_set)

print('__RESULT__:')
print(json.dumps({'count': len(matched), 'matched_projects_sample': matched[:80], 'total_design_extracted': len(status_design_projects)}))"""

env_args = {'var_call_PQlGS0E1wfYq5WDTx0gwnMbs': [{'cnt': '276'}], 'var_call_5OGYeOICM5QNI2M9LpSCiuKR': 'file_storage/call_5OGYeOICM5QNI2M9LpSCiuKR.json', 'var_call_Bqxm38LOT1pz4NEqbD4bvNeK': 'file_storage/call_Bqxm38LOT1pz4NEqbD4bvNeK.json'}

exec(code, env_args)
