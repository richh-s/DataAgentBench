code = """import json, re
path = var_call_6s5RpImgm3iTcGaGq8ohXGZr
with open(path,'r') as f:
    data = json.load(f)
uc_recs = [rec for rec in data if 'UNIV CALIFORNIA' in rec.get('Patents_info','')]
patterns = [r"[A-Z]{2}-\d{4,}-[A-Z0-9]+", r"[A-Z]{2}-\d{4,}", r"US-\d{7,}-[A-Z0-9]+", r"[A-Z]{2}-\d{6,}-[A-Z]", r"US-\d{7,}"]
found = set()
for rec in uc_recs:
    text = rec.get('Patents_info','')
    for pat in patterns:
        for m in re.findall(pat, text):
            found.add(m)
for rec in uc_recs:
    text = rec.get('Patents_info','')
    m = re.search(r"pub(?:\.lish)?(?:ation)?(?:\s)?number\s*[:]?\s*([A-Z]{2}-[0-9A-Z\-]+)", text, re.IGNORECASE)
    if m:
        found.add(m.group(1))
    m2 = re.search(r"pub\. number\s*([A-Z]{2}-[0-9A-Z\-]+)", text, re.IGNORECASE)
    if m2:
        found.add(m2.group(1))
for rec in uc_recs:
    text = rec.get('Patents_info','')
    tokens = re.split('[,;()\n]', text)
    for t in tokens:
        t = t.strip()
        if re.match(r'^[A-Z]{2}-\d{4,}-[A-Z0-9]+$', t):
            found.add(t)
samples = [r.get('Patents_info') for r in uc_recs[:5]]
result = {'num_uc_records': len(uc_recs), 'uc_pubnums': sorted(found), 'samples': samples}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_6s5RpImgm3iTcGaGq8ohXGZr': 'file_storage/call_6s5RpImgm3iTcGaGq8ohXGZr.json', 'var_call_gG2899rItsLZOgaJaeMhanfU': []}

exec(code, env_args)
