code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Line-based extraction around completion mentions in 2022
projects = set()

for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    if not any(k in text.lower() for k in ['park', 'playground', 'bluffs']):
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if re.search(r"\b(Construction was completed|construction was completed|completed)\b.*\b2022\b", ln):
            # walk backwards to find a plausible project name line
            for j in range(i-1, max(-1, i-30), -1):
                cand = lines[j].strip()
                if not cand or len(cand) > 120:
                    continue
                if cand.startswith(('(cid', 'Page', 'Agenda', 'Updates', 'Project Schedule', 'Estimated Schedule')):
                    continue
                if any(x in cand.lower() for x in ['updates', 'project schedule', 'estimated schedule', 'project description']):
                    continue
                if re.search(r"\bpark\b|playground|bluffs", cand, re.I):
                    projects.add(cand)
                    break

print('__RESULT__:')
print(json.dumps({'projects_completed_2022_park_related': sorted(projects), 'count': len(projects)}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json'}

exec(code, env_args)
