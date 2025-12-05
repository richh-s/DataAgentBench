code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_5IdcQmOBSdzDr5RwJDg5NzW9)
rows = json.loads(path.read_text())

records = []
for r in rows:
    info = r.get('Patents_info','')
    if 'assignee_harmonized:' in info:
        # extract assignee_harmonized value
        try:
            part = info.split('assignee_harmonized:')[1]
            assignee = part.split(' and')[0].split('.')[0].strip()
        except Exception:
            assignee = ''
    else:
        assignee = ''
    records.append({
        'Patents_info': info,
        'assignee': assignee,
        'cpc': r.get('cpc',''),
        'citation': r.get('citation','')
    })

# identify cited publication_numbers for patents assigned to UNIV CALIFORNIA
ucited = set()
for rec in records:
    if 'owned by UNIV CALIFORNIA' in rec['Patents_info'] or 'assigned to UNIV CALIFORNIA' in rec['Patents_info'] or 'UNIV CALIFORNIA holds' in rec['Patents_info']:
        try:
            cites = json.loads(rec['citation'])
        except Exception:
            continue
        for c in cites:
            pn = c.get('publication_number','')
            if pn:
                ucited.add(pn)

# now find all publications (any assignee) that cite these publication_numbers
citing_assignees = {}
for r in rows:
    info = r.get('Patents_info','')
    if 'assignee_harmonized:' in info:
        try:
            part = info.split('assignee_harmonized:')[1]
            assignee = part.split(' and')[0].split('.')[0].strip()
        except Exception:
            assignee = ''
    else:
        # try simpler pattern ' is owned by ' etc
        assignee = ''
    try:
        cites = json.loads(r.get('citation',''))
    except Exception:
        continue
    match = False
    for c in cites:
        if c.get('publication_number','') in ucited:
            match = True
            break
    if match:
        if 'UNIV CALIFORNIA' in assignee:
            continue
        # collect primary CPC subclasses for this citing patent
        try:
            cpcs = json.loads(r.get('cpc',''))
        except Exception:
            cpcs = []
        primary = [c['code'] for c in cpcs if c.get('first')]
        citing_assignees.setdefault(assignee or 'UNKNOWN', set()).update(primary)

result = {a: sorted(list(codes)) for a, codes in citing_assignees.items()}

import json as _j
out = _j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VyvxqGiKX2mHqW0HCBUffhJJ': [], 'var_call_5IdcQmOBSdzDr5RwJDg5NzW9': 'file_storage/call_5IdcQmOBSdzDr5RwJDg5NzW9.json'}

exec(code, env_args)
