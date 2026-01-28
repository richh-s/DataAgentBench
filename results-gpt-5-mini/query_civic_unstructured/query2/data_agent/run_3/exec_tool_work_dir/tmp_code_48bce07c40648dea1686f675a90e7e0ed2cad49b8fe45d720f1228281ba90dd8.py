code = """import json, re
p = var_call_lGT6WoCuyWvDkZO6yDO1wveb
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)

names = []
for doc in docs:
    text = doc.get('text','')
    paras = re.split(r"\n\n+", text)
    for para in paras:
        low = para.lower()
        if 'completed' in low and '2022' in low and re.search(r'park|playground|walkway|shade|bluffs|point dume|trancas', low):
            first = para.strip().splitlines()[0].strip()
            if first:
                first = re.sub(r"\s*-?\s*Project$", "", first, flags=re.I).strip()
                names.append(first)

# dedupe preserving order
seen = set()
unique = []
for n in names:
    if n not in seen:
        seen.add(n)
        unique.append(n)

print("__RESULT__:")
print(json.dumps(unique))"""

env_args = {'var_call_lGT6WoCuyWvDkZO6yDO1wveb': 'file_storage/call_lGT6WoCuyWvDkZO6yDO1wveb.json'}

exec(code, env_args)
