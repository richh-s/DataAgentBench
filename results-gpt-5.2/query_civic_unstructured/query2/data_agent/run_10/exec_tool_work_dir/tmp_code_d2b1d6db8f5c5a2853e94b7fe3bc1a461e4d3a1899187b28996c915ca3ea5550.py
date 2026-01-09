code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

projects = set()

for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    if not any(k in text.lower() for k in ['park', 'playground', 'bluffs']):
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if not ('2022' in ln and re.search(r"\bcompleted\b|\bconstruction was completed\b", ln, flags=re.I)):
            continue
        for j in range(i-1, max(-1, i-40), -1):
            cand = lines[j].strip()
            if not cand or len(cand) > 120:
                continue
            if cand.startswith(('(cid', 'Page', 'Agenda', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject:', 'RECOMMENDED', 'DISCUSSION')):
                continue
            low = cand.lower()
            if ('updates' in low) or ('project schedule' in low) or ('estimated schedule' in low) or ('project description' in low) or ('capital improvement projects' in low) or ('disaster recovery projects' in low):
                continue
            if ':' in cand:
                continue
            win = "\n".join(lines[max(0, j-5): min(len(lines), j+6)])
            if re.search(r"\bpark\b|playground|bluffs", cand, re.I) or re.search(r"\bpark\b|playground|bluffs", win, re.I):
                projects.add(cand)
                break

print('__RESULT__:')
print(json.dumps({'projects_completed_2022_park_related': sorted(projects), 'count': len(projects)}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json', 'var_call_DvFCvwPxOzQtBKBdG9HiZTyv': {'projects_completed_2022_park_related': [], 'count': 0}}

exec(code, env_args)
