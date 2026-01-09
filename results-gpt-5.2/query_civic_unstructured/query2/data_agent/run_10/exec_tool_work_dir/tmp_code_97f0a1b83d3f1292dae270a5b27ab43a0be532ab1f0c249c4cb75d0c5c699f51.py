code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

# Find park-related projects whose completion line mentions 2022
pattern = re.compile(r"(?P<name>[A-Z][A-Za-z0-9\-\&\,\'\(\)\./ ]{3,}?)\n\s*\(cid:[^\n]*\n\s*Updates:[\s\S]{0,400}?\b(?:completed|construction was completed|complete(?:d)? construction)\b[\s\S]{0,120}?\b2022\b", re.I)

found = {}
for d in docs:
    text = d.get('text','') or ''
    if 'park' not in text.lower() and 'playground' not in text.lower() and 'bluffs' not in text.lower():
        continue
    for m in pattern.finditer(text):
        name = m.group('name').strip()
        if re.search(r"\bpark\b|playground|bluffs", name, re.I):
            found[name] = d.get('filename')

projects_2022 = sorted(found.keys())
print('__RESULT__:')
print(json.dumps({'projects_completed_2022_park_related': projects_2022, 'count': len(projects_2022)}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json'}

exec(code, env_args)
