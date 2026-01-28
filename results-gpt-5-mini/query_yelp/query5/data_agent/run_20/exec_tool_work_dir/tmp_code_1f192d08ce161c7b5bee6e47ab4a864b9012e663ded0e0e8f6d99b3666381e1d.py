code = """import json, re

# Load Mongo query result file
path = var_call_iZU5oKUxuDZXG7cXh0BjQZ4L
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

state_businesses = {}

for doc in data:
    business_id = doc.get('business_id')
    attrs = doc.get('attributes') or {}
    wifi = attrs.get('WiFi') if isinstance(attrs, dict) else None
    if wifi is None:
        continue
    wifi_str = str(wifi).lower()
    # treat as offering wifi if it does not contain 'no'
    if 'no' in wifi_str:
        continue
    # extract state from description
    desc = doc.get('description') or ''
    state = None
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r',\s*([A-Z]{2})\b', desc)
        if m2:
            state = m2.group(1)
    if state is None:
        continue
    # map businessid_ -> businessref_
    business_ref = business_id.replace('businessid_', 'businessref_')
    state_businesses.setdefault(state, []).append(business_ref)

# compute counts
state_counts = {s: len(v) for s, v in state_businesses.items()}
if not state_counts:
    result = {'top_state': None, 'business_refs': []}
else:
    # pick state with max count, tie-break by lexicographic
    top_state = sorted(state_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
    result = {'top_state': top_state, 'business_refs': state_businesses[top_state], 'count': len(state_businesses[top_state])}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_AVnID2AbtzsoF3Z1fKps5TMD': ['business', 'checkin'], 'var_call_vRlvrfnRNcacz2jHCK6xlI8N': ['review', 'tip', 'user'], 'var_call_iZU5oKUxuDZXG7cXh0BjQZ4L': 'file_storage/call_iZU5oKUxuDZXG7cXh0BjQZ4L.json'}

exec(code, env_args)
