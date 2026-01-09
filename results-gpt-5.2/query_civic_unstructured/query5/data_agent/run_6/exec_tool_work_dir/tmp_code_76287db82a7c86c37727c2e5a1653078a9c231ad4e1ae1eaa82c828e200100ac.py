code = """import json, re

path = var_call_K2hwlcqqTZL2gfcVFExZ9mfr
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
for d in docs:
    text = d.get('text','') or ''
    if 'Disaster Recovery Projects' not in text:
        continue
    idx = text.find('Disaster Recovery Projects')
    sub = text[idx:]
    lines = [ln.strip() for ln in sub.splitlines()]
    current = None
    buf = []
    in_disaster = False
    for ln in lines:
        if re.search(r'^Disaster Recovery Projects', ln):
            in_disaster = True
            current = None
            buf = []
            continue
        if not in_disaster:
            continue
        if re.match(r'^(Capital Improvement Projects|Public Works Quarterly|RECOMMENDED ACTION|DISCUSSION:)', ln):
            if current:
                projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})
            in_disaster = False
            current = None
            buf = []
            continue
        if ln and (not ln.startswith('(cid')) and ln not in ['Updates:', 'Project Schedule:', 'Estimated Schedule:']:
            if (('Project' in ln) or ('Repair' in ln) or ('Repairs' in ln) or ('Restoration' in ln) or ('Recovery' in ln) or ('Slope' in ln) or ('Road' in ln) or ('Canyon' in ln) or ('Drainage' in ln) or ('Storm' in ln) or ('Park' in ln)) and len(ln) < 120 and (':' not in ln):
                if current and ln != current and (('Updates' in '\n'.join(buf)) or ('Schedule' in '\n'.join(buf)) or len(buf)>0):
                    projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})
                    buf = []
                current = ln
                continue
        if current:
            buf.append(ln)
    if current:
        projects.append({'Project_Name': current, 'details':'\n'.join(buf), 'source_file': d.get('filename')})

started_2022 = set()
for p in projects:
    det = p['details']
    if re.search(r'Begin (Construction|construction)\s*:\s*[^\n]*2022', det):
        started_2022.add(p['Project_Name'])
    elif re.search(r'(\bStart\b|\bStarted\b)\s*:\s*[^\n]*2022', det):
        started_2022.add(p['Project_Name'])

started_2022 = sorted(started_2022)

print('__RESULT__:')
print(json.dumps({'disaster_projects_started_2022': started_2022, 'count': len(started_2022)}))"""

env_args = {'var_call_BeorDsx8JrPIuB2mlCATPqZZ': ['Funding'], 'var_call_OADTgr7Ub1LCEk7c1kButQGv': ['civic_docs'], 'var_call_K2hwlcqqTZL2gfcVFExZ9mfr': 'file_storage/call_K2hwlcqqTZL2gfcVFExZ9mfr.json'}

exec(code, env_args)
