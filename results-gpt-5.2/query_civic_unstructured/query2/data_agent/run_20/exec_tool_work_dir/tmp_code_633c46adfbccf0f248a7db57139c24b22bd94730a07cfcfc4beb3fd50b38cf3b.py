code = """import json, re, pandas as pd

# Load civic docs (may be a path)
cd = var_call_qvrtWo5ckaPHo4JuQApeYQRO
if isinstance(cd, str):
    with open(cd, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

fund = var_call_BtGgeWnJ2chFFMF7vP6AV4Es
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        funding_rows = json.load(f)
else:
    funding_rows = fund

# Build funding map
funding = {}
for r in funding_rows:
    pn = (r.get('Project_Name') or '').strip()
    try:
        amt = int(r.get('Amount'))
    except Exception:
        continue
    funding[pn] = funding.get(pn, 0) + amt

project_info = {}  # name -> dict(topic_is_park, completed_2022)

# regex for completion lines
completed_re = re.compile(r"^\s*(?P<name>.+?)\s*\n\s*\(cid:190\)\s*Updates\s*:\s*(?P<upd>.+)$", re.MULTILINE)

for doc in civic_docs:
    text = doc.get('text') or ''

    # capture updates lines with completed and 2022 in same/near text
    for m in completed_re.finditer(text):
        name = m.group('name').strip()
        upd = m.group('upd').strip()
        if 'completed' in upd.lower() and '2022' in upd:
            info = project_info.get(name, {'park': False, 'completed_2022': False})
            info['completed_2022'] = True
            project_info[name] = info

    # also handle lines like 'Construction was completed November 2022.' without Updates label
    # pattern: name on its own line then later 'completed' and '2022' within next 5 lines
    lines = text.splitlines()
    for i, line in enumerate(lines):
        cand = line.strip()
        if not cand or len(cand) > 120:
            continue
        # likely a project name line: Title Case with few words and no colon
        if ':' in cand:
            continue
        if cand.lower() in {'discussion','recommended action'}:
            continue
        # lookahead window
        window = '\n'.join(lines[i+1:i+6])
        if ('completed' in window.lower()) and ('2022' in window):
            info = project_info.get(cand, {'park': False, 'completed_2022': False})
            info['completed_2022'] = True
            project_info[cand] = info

    # park-related: mark if project name contains park/playground/skate or within section header includes Park
    park_keywords = ['park', 'playground', 'skate']
    for name in list(project_info.keys()):
        if any(k in name.lower() for k in park_keywords):
            project_info[name]['park'] = True

# Now compute sum for park-related projects completed in 2022 and present in funding
selected = []
for name, info in project_info.items():
    if info.get('park') and info.get('completed_2022'):
        if name in funding:
            selected.append({'Project_Name': name, 'Amount': funding[name]})

# Sum
total = sum(r['Amount'] for r in selected)

out = {'total_funding': total, 'projects': selected}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_qvrtWo5ckaPHo4JuQApeYQRO': 'file_storage/call_qvrtWo5ckaPHo4JuQApeYQRO.json', 'var_call_BtGgeWnJ2chFFMF7vP6AV4Es': 'file_storage/call_BtGgeWnJ2chFFMF7vP6AV4Es.json'}

exec(code, env_args)
