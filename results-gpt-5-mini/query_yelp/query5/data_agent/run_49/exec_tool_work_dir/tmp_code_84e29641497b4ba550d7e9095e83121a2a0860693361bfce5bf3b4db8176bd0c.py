code = """import json, re
# var_call_lyuIhu1hJ2dZgWmh4ozVScQN is the storage key for the large business query result file path
path = var_call_lyuIhu1hJ2dZgWmh4ozVScQN
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes') or {}
    wifi = attrs.get('WiFi') if isinstance(attrs, dict) else None
    desc = rec.get('description') or ''
    state = None
    # try to extract state abbreviation from description
    m = re.search(r'in [^,]+,\s*([A-Z]{2})\b', desc)
    if m:
        state = m.group(1)
    else:
        # fallback: look for pattern ', XX,'
        m2 = re.search(r',\s*([A-Z]{2}),', desc)
        if m2:
            state = m2.group(1)
    # normalize wifi string
    wifi_norm = None
    if isinstance(wifi, str):
        wifi_norm = wifi.lower()
    # determine if offers wifi: contains 'free' or 'paid' or 'yes' and not contains 'no'
    offers = False
    if wifi_norm:
        if ('free' in wifi_norm) or ('paid' in wifi_norm) or ('yes' in wifi_norm) or ('spot' in wifi_norm):
            offers = True
        elif 'no' in wifi_norm:
            offers = False
        else:
            # unknown value, treat as not offering
            offers = False
    # collect
    if bid and state and offers:
        bref = bid.replace('businessid_', 'businessref_')
        results.append({'business_ref': bref, 'business_id': bid, 'state': state})

# deduplicate
unique = {}
for r in results:
    unique[r['business_ref']] = r['state']

business_refs = sorted(unique.keys())
mapping = unique
out = {'business_refs': business_refs, 'mapping': mapping}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ISQoh6iMVYmAnZq1TNJGCAAx': ['checkin', 'business'], 'var_call_qJb8PqPyM64XFVIREQHFZvqM': ['review', 'tip', 'user'], 'var_call_lyuIhu1hJ2dZgWmh4ozVScQN': 'file_storage/call_lyuIhu1hJ2dZgWmh4ozVScQN.json'}

exec(code, env_args)
