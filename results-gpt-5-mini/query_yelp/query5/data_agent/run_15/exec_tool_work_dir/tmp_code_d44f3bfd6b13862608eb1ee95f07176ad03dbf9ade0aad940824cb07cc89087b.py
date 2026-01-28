code = """import json, re

with open(var_call_cKAUvs32jTulvBxlVKm3UG9A, 'r') as f:
    businesses = json.load(f)
with open(var_call_HqfVjLmSpm2LUwUZsWZG8Qg2, 'r') as f:
    reviews = json.load(f)

ratings_by_ref = {}
for r in reviews:
    br = r.get('business_ref')
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings_by_ref.setdefault(br, []).append(rating)

def offers_wifi(attrs):
    if not isinstance(attrs, dict):
        return False
    for k, v in attrs.items():
        if not k:
            continue
        key = str(k).lower()
        if 'wifi' in key or 'wi-fi' in key:
            if v is None:
                return False
            sval = str(v).lower()
            if 'no' in sval:
                return False
            return True
    return False

wifi_businesses_by_state = {}
for b in businesses:
    attrs = b.get('attributes')
    if not attrs:
        continue
    if not offers_wifi(attrs):
        continue
    desc = b.get('description') or ''
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if not m:
        # try ' in City, ST'
        m = re.search(r' in [^,]+,\s*([A-Z]{2})\b', desc)
    if not m:
        continue
    state = m.group(1)
    bid = b.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    wifi_businesses_by_state.setdefault(state, set()).add(bref)

results = []
for state, bref_set in wifi_businesses_by_state.items():
    count = len(bref_set)
    total = 0.0
    cnt = 0
    for bref in bref_set:
        rlist = ratings_by_ref.get(bref, [])
        total += sum(rlist)
        cnt += len(rlist)
    avg = None
    if cnt > 0:
        avg = round(total / cnt, 2)
    results.append({'state': state, 'wifi_business_count': count, 'average_rating': avg, 'ratings_count': cnt})

if not results:
    out = {'error': 'No results'}
else:
    top = sorted(results, key=lambda x: (-x['wifi_business_count'], x['state']))[0]
    out = {'state': top['state'], 'wifi_business_count': top['wifi_business_count'], 'average_rating': top['average_rating'], 'ratings_count': top['ratings_count']}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_cKAUvs32jTulvBxlVKm3UG9A': 'file_storage/call_cKAUvs32jTulvBxlVKm3UG9A.json', 'var_call_HqfVjLmSpm2LUwUZsWZG8Qg2': 'file_storage/call_HqfVjLmSpm2LUwUZsWZG8Qg2.json'}

exec(code, env_args)
