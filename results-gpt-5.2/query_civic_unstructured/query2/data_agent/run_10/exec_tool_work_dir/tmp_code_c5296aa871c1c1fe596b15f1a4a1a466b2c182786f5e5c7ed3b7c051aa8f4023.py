code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

needle_docs = []
for d in docs:
    t = (d.get('text') or '').lower()
    if '2022' in t and ('park' in t or 'bluffs' in t or 'playground' in t):
        if 'completed' in t or 'construction was completed' in t:
            needle_docs.append(d)

samples = []
for d in needle_docs[:5]:
    lines = (d.get('text') or '').splitlines()
    found = False
    for i, ln in enumerate(lines):
        if '2022' in ln.lower() and ('completed' in ln.lower() or 'construction was completed' in ln.lower()):
            ctx = [x for x in lines[max(0,i-6): min(len(lines), i+7)]]
            samples.append({'filename': d.get('filename'), 'line': ln, 'context': ctx})
            found = True
            break
    if not found:
        # maybe completed and 2022 on different lines; find first completed then show context
        for i, ln in enumerate(lines):
            if 'completed' in ln.lower() or 'construction was completed' in ln.lower():
                ctx = [x for x in lines[max(0,i-6): min(len(lines), i+7)]]
                samples.append({'filename': d.get('filename'), 'line': ln, 'context': ctx})
                break

print('__RESULT__:')
print(json.dumps({'docs': len(needle_docs), 'samples': samples}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json', 'var_call_DvFCvwPxOzQtBKBdG9HiZTyv': {'projects_completed_2022_park_related': [], 'count': 0}, 'var_call_RSTg9AxLTI6rwEUks3N6ebvO': {'docs_with_completed_2022_and_park': 19, 'sample_contexts': []}}

exec(code, env_args)
