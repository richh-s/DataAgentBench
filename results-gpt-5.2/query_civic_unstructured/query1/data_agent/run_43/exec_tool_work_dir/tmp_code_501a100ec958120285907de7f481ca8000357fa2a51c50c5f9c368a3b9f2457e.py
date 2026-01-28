code = """import json, re, pandas as pd

# load funding project names >50k
p = var_call_Bqxm38LOT1pz4NEqbD4bvNeK
if isinstance(p, str) and p.endswith('.json'):
    with open(p, 'r', encoding='utf-8') as f:
        funding_names = json.load(f)
else:
    funding_names = p
funding_set = {d['Project_Name'] for d in funding_names if d.get('Project_Name')}

# load civic docs
p2 = var_call_5OGYeOICM5QNI2M9LpSCiuKR
if isinstance(p2, str) and p2.endswith('.json'):
    with open(p2, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = p2

# heuristic extraction: find 'Capital Improvement Projects (Design)' section and list subsequent project titles
status_design_projects = set()
for doc in docs:
    text = doc.get('text','')
    if not text:
        continue
    # normalize
    t = text.replace('\r','')
    # locate capital design section
    m = re.search(r'Capital Improvement Projects\s*\(Design\)', t, flags=re.IGNORECASE)
    if not m:
        continue
    after = t[m.end():]
    # stop at next header like '(Construction)' or '(Not Started)' or 'Disaster'
    stop = re.search(r'Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects', after, flags=re.IGNORECASE)
    if stop:
        after = after[:stop.start()]

    lines = [ln.strip() for ln in after.split('\n')]
    # candidate titles: non-empty lines not starting with bullets/markers and followed soon by 'Updates' or 'Project Description'
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.match(r'^[\(\[\{\*\-\u2022\u00b7\u2023]|^cid:', ln, flags=re.IGNORECASE):
            continue
        if ln.lower() in {'updates:', 'project schedule:', 'estimated schedule:', 'project description:', 'discussion:', 'recommended action:'}:
            continue
        # titles usually not too long and not all caps boilerplate
        if len(ln) > 120:
            continue
        # check lookahead for keyword lines
        look = '\n'.join(lines[i+1:i+6]).lower()
        if ('updates' in look) or ('project schedule' in look) or ('estimated schedule' in look) or ('project description' in look):
            # clean trailing spaces
            title = re.sub(r'\s+', ' ', ln).strip()
            status_design_projects.add(title)

# intersection with funding set
count = len(status_design_projects & funding_set)

print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': sorted(status_design_projects & funding_set)[:50], 'total_design_extracted': len(status_design_projects)}))"""

env_args = {'var_call_PQlGS0E1wfYq5WDTx0gwnMbs': [{'cnt': '276'}], 'var_call_5OGYeOICM5QNI2M9LpSCiuKR': 'file_storage/call_5OGYeOICM5QNI2M9LpSCiuKR.json', 'var_call_Bqxm38LOT1pz4NEqbD4bvNeK': 'file_storage/call_Bqxm38LOT1pz4NEqbD4bvNeK.json'}

exec(code, env_args)
