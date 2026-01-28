code = """import json, re
from collections import defaultdict

path = var_call_GETMSgFVgDBmQ75wBV0Y1PYD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

state_counts = defaultdict(int)
state_to_businesses = defaultdict(list)

for b in data:
    attrs = b.get('attributes')
    if not isinstance(attrs, dict):
        continue
    wifi = attrs.get('WiFi')
    if wifi is None:
        continue
    s = str(wifi).lower()
    s = s.replace("u'", "").replace('"', '').replace("'", '').strip()
    if 'no' in s or 'none' in s:
        continue
    desc = b.get('description') or ''
    m = re.search(r'in [^,]+, ([A-Z]{2})', desc)
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r', ([A-Z]{2})\b', desc)
        state = m2.group(1) if m2 else None
    if not state:
        continue
    state_counts[state] += 1
    state_to_businesses[state].append(b.get('business_id'))

if not state_counts:
    out = {'top_state': None, 'count': 0, 'business_ids': []}
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    out = {'top_state': top_state, 'count': state_counts[top_state], 'business_ids': state_to_businesses[top_state]}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YW0MNUIpy8qimuQlLtlvK3rN': ['checkin', 'business'], 'var_call_GETMSgFVgDBmQ75wBV0Y1PYD': 'file_storage/call_GETMSgFVgDBmQ75wBV0Y1PYD.json'}

exec(code, env_args)
