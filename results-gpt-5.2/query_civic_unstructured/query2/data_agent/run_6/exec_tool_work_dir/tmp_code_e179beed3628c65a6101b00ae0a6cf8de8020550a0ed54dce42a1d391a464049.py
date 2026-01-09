code = """import json, re

raw = var_call_RWCBaMzypu5Pb5Ttrq2OIv4f
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

text_all = "\n\n".join(d.get('text','') for d in docs)

patterns = [
    re.compile(r"\n\s*([A-Z][^\n]{2,120}?)\n\s*(?:\(.*?\)\n\s*)?(?:\(.*?\)\n\s*)?[^\n]*?Complete Construction:\s*([^\n]{0,40})", re.IGNORECASE),
    re.compile(r"\n\s*([A-Z][^\n]{2,120}?)\n(?:(?!\n\s*[A-Z][^\n]{2,120}?\n).)*?Construction was completed\s*[,:]?\s*([^\n]{0,40})", re.IGNORECASE|re.DOTALL),
]

completed_2022 = set()
for pat in patterns:
    for m in pat.finditer(text_all):
        name = m.group(1).strip()
        date = (m.group(2) or '').strip()
        if '2022' in date:
            completed_2022.add(name)

park_related = sorted([n for n in completed_2022 if re.search(r"\bpark\b|playground|bluffs", n, re.IGNORECASE)])

print('__RESULT__:')
print(json.dumps({"park_related_completed_2022": park_related}))"""

env_args = {'var_call_ZkGLNSU9TkHaiaz8gSwrvuPX': ['Funding'], 'var_call_DRbudRnWnAnVotVALYH4JCve': ['civic_docs'], 'var_call_RWCBaMzypu5Pb5Ttrq2OIv4f': 'file_storage/call_RWCBaMzypu5Pb5Ttrq2OIv4f.json'}

exec(code, env_args)
