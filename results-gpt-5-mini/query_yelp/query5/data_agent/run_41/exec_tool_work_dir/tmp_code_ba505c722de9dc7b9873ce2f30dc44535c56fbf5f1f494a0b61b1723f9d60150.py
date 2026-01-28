code = """import json
fp = var_call_XEkgfmj9JwPP0dFeduO2a8QB['path']
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

counts = {}
refs_by_state = {}

for rec in data:
    attrs = rec.get('attributes')
    if not isinstance(attrs, dict):
        continue
    wifi_raw = attrs.get('WiFi')
    if wifi_raw is None:
        continue
    s = str(wifi_raw)
    if s.startswith("u'") or s.startswith('u"'):
        s = s[2:]
    s = s.strip("'\" ")
    sval = s.lower()
    offers = any(k in sval for k in ['free','paid','yes','spotty','full','limited','guest'])
    if not offers:
        continue
    desc = rec.get('description') or ''
    parts = [p.strip() for p in desc.split(',')]
    state = None
    for p in parts:
        if len(p) == 2 and p.isupper() and p in us_states:
            state = p
            break
    if state is None:
        continue
    bid = rec.get('business_id')
    bref = bid
    if isinstance(bref, str) and bref.startswith('businessid_'):
        bref = bref.replace('businessid_', 'businessref_')
    counts[state] = counts.get(state, 0) + 1
    refs_by_state.setdefault(state, []).append(bref)

# find top state
if not counts:
    out = {'error': 'no wifi offering businesses found'}
else:
    top_state = max(counts.items(), key=lambda x: x[1])[0]
    top_count = counts[top_state]
    top_refs = sorted(list(set(refs_by_state.get(top_state, []))))
    out = {'top_state': top_state, 'count': top_count, 'business_refs': top_refs}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json', 'var_call_XEkgfmj9JwPP0dFeduO2a8QB': {'path': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}}

exec(code, env_args)
