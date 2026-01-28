code = """import json, re
from collections import defaultdict

# Load data from storage-provided file paths
with open(var_call_oUPC1A5H7aRmcQmW3CpGOTAm, 'r') as f:
    businesses = json.load(f)
with open(var_call_SGWfjBUpDIX9ay0iVhMKZb5T, 'r') as f:
    reviews = json.load(f)

# Normalize and filter businesses that offer WiFi
wifi_businesses = []
for b in businesses:
    attrs = b.get('attributes') or {}
    wifi_val = attrs.get('WiFi')
    if wifi_val is None:
        continue
    s = str(wifi_val).lower()
    s = s.replace("u'", "").replace('"', '').replace("'", "").strip()
    offers = 'no' not in s
    if not offers:
        continue
    desc = b.get('description') or ''
    m = re.search(r',\s*([A-Z]{2}),', desc)
    state = None
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r',\s*([A-Z]{2})\b', desc)
        if m2:
            state = m2.group(1)
    if not state:
        continue
    bid = b.get('business_id')
    bref = bid.replace('businessid_', 'businessref_') if bid else None
    wifi_businesses.append({'business_id': bid, 'business_ref': bref, 'state': state})

# Mapping and counts
ref_to_state = {wb['business_ref']: wb['state'] for wb in wifi_businesses if wb['business_ref']}
state_businesss = defaultdict(set)
for wb in wifi_businesses:
    state_businesss[wb['state']].add(wb['business_id'])
state_counts = {st: len(bset) for st, bset in state_businesss.items()}

# Aggregate ratings
state_ratings = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    if bref in ref_to_state:
        try:
            rating = float(r.get('rating'))
        except:
            continue
        state = ref_to_state[bref]
        state_ratings[state].append(rating)

# Compute averages
avg_rating = {}
for st, ratings in state_ratings.items():
    if ratings:
        avg_rating[st] = sum(ratings) / len(ratings)

for st in state_counts:
    if st not in avg_rating:
        avg_rating[st] = None

# Find max
if not state_counts:
    result = {"state": None, "business_count": 0, "average_rating": None}
else:
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    count = state_counts[max_state]
    avg = avg_rating.get(max_state)
    if avg is not None:
        avg = round(avg, 2)
    result = {"state": max_state, "business_count": count, "average_rating": avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tLAtk1cOMzzSPAhB4R6m1FK5': ['business', 'checkin'], 'var_call_ZD9X6eiUuBo82GU5TxzWsqmy': ['review', 'tip', 'user'], 'var_call_oUPC1A5H7aRmcQmW3CpGOTAm': 'file_storage/call_oUPC1A5H7aRmcQmW3CpGOTAm.json', 'var_call_SGWfjBUpDIX9ay0iVhMKZb5T': 'file_storage/call_SGWfjBUpDIX9ay0iVhMKZb5T.json'}

exec(code, env_args)
