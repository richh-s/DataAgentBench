code = """import json, re

# Load civic docs (may be a filepath)
raw = var_call_RWCBaMzypu5Pb5Ttrq2OIv4f
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

text_all = "\n\n".join(d.get('text','') for d in docs)

# Extract project name blocks and completion end-times containing 2022.
# We'll parse lines around "Complete Construction:" or "Construction was completed".
patterns = [
    # Format: <Project Name> ... Complete Construction: <date>
    re.compile(r"\n\s*([A-Z][^\n]{2,120}?)\n\s*(?:\(.*?\)\n\s*)?(?:\(.*?\)\n\s*)?[^\n]*?Complete Construction:\s*([^\n]{0,40})", re.IGNORECASE),
    # Format: <Project Name> ... Construction was completed <date>
    re.compile(r"\n\s*([A-Z][^\n]{2,120}?)\n(?:(?!\n\s*[A-Z][^\n]{2,120}?\n).)*?Construction was completed\s*[,:]?\s*([^\n]{0,40})", re.IGNORECASE|re.DOTALL),
]

completed_2022 = set()
park_related = set()

for pat in patterns:
    for m in pat.finditer(text_all):
        name = m.group(1).strip()
        date = (m.group(2) or '').strip()
        if '2022' in date:
            completed_2022.add(name)

# Determine park-related project names: those with 'Park' or 'Playground' in name.
for name in completed_2022:
    if re.search(r"\bpark\b|playground|bluffs", name, re.IGNORECASE):
        park_related.add(name)

result = {
    "completed_2022": sorted(completed_2022),
    "park_related_completed_2022": sorted(park_related)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ZkGLNSU9TkHaiaz8gSwrvuPX': ['Funding'], 'var_call_DRbudRnWnAnVotVALYH4JCve': ['civic_docs'], 'var_call_RWCBaMzypu5Pb5Ttrq2OIv4f': 'file_storage/call_RWCBaMzypu5Pb5Ttrq2OIv4f.json'}

exec(code, env_args)
