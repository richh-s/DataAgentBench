code = """import json, re
path = var_call_IZ7Xl8OO6uQmBAMPvEWebOej
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

out = []
for i, r in enumerate(data[:40]):
    wifi = (r.get('attributes') or {}).get('WiFi')
    desc = r.get('description','')
    m = re.search(r" in [^,]+,\s*([A-Z]{2})\b", desc)
    m2 = re.search(r",\s*([A-Z]{2})\b", desc)
    out.append({
        'idx': i,
        'business_id': r.get('business_id'),
        'wifi_raw': wifi,
        'wifi_norm': str(wifi).lower() if wifi is not None else None,
        'desc': desc,
        'match1': m.group(1) if m else None,
        'match2': m2.group(1) if m2 else None
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ph2sjADjdgLcbK7lQLedGUrw': ['checkin', 'business'], 'var_call_LXxAdUGFtNaGYmRaX9ahBRVR': 'file_storage/call_LXxAdUGFtNaGYmRaX9ahBRVR.json', 'var_call_IZ7Xl8OO6uQmBAMPvEWebOej': 'file_storage/call_IZ7Xl8OO6uQmBAMPvEWebOej.json', 'var_call_ujs7pHQTlXU6RQF5ifNLqS2w': {'top_state': None, 'count': 0, 'business_refs': []}}

exec(code, env_args)
