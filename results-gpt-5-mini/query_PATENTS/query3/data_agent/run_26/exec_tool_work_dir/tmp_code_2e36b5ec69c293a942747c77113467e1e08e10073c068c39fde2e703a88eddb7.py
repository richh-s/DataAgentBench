code = """import json, re
# var_call_1io1Ln1MpXYuyOoPruPFfSdO contains the filepath to the JSON results from the earlier query
path = var_call_1io1Ln1MpXYuyOoPruPFfSdO
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
pubnums = set()
patterns = [r'pub(?:lication)?\. number\s*([A-Z0-9-]+)', r'publication number\s*([A-Z0-9-]+)', r'pub\. number\s*([A-Z0-9-]+)', r'publication number\s*([A-Z0-9-]+)']
for r in records:
    pi = r.get('Patents_info','')
    for pat in patterns:
        for m in re.finditer(pat, pi, flags=re.IGNORECASE):
            pubnums.add(m.group(1))
# fallback: also look for patterns like "with pub. number X" or "with publication number X"
for r in records:
    pi = r.get('Patents_info','')
    m = re.search(r'with (?:pub(?:lication)?\. number|publication number|pub\. number)\s*([A-Z0-9-]+)', pi, flags=re.IGNORECASE)
    if m:
        pubnums.add(m.group(1))
# As an extra, look for uppercase token sequences with hyphens that look like publication numbers
for r in records:
    pi = r.get('Patents_info','')
    toks = re.findall(r'\b[A-Z]{2,}-[A-Z0-9-]+\b', pi)
    for t in toks:
        if any(ch.isdigit() for ch in t):
            pubnums.add(t)

pubnums = sorted(pubnums)
# Output as JSON-serializable string
out = json.dumps({'publication_numbers': pubnums})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1io1Ln1MpXYuyOoPruPFfSdO': 'file_storage/call_1io1Ln1MpXYuyOoPruPFfSdO.json', 'var_call_q6uBgUJjdgKLjIj9qxzqBT1n': 'file_storage/call_q6uBgUJjdgKLjIj9qxzqBT1n.json'}

exec(code, env_args)
