code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

needle_docs = []
for d in docs:
    t = (d.get('text') or '').lower()
    if 'completed' in t and '2022' in t and ('park' in t or 'bluffs' in t or 'playground' in t):
        needle_docs.append(d)

# show sample lines around completed mentions
samples = []
for d in needle_docs[:5]:
    lines = (d.get('text') or '').splitlines()
    for i, ln in enumerate(lines):
        if '2022' in ln and re.search(r"\bcompleted\b|\bconstruction was completed\b", ln, re.I):
            ctx = lines[max(0,i-4): min(len(lines), i+3)]
            samples.append({'filename': d.get('filename'), 'context': ctx})
            break

print('__RESULT__:')
print(json.dumps({'docs_with_completed_2022_and_park': len(needle_docs), 'sample_contexts': samples}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json', 'var_call_DvFCvwPxOzQtBKBdG9HiZTyv': {'projects_completed_2022_park_related': [], 'count': 0}}

exec(code, env_args)
