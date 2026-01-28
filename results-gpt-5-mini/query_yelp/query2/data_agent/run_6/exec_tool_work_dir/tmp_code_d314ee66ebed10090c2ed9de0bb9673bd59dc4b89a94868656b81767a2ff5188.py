code = """import json, re
p = var_call_0yihErUwHGGDGnIs4qS1INo8
with open(p, 'r') as f:
    data = json.load(f)
state_counts = {}
state_businesses = {}
for item in data:
    bid = item.get('business_id')
    rc = item.get('review_count')
    try:
        rc_int = int(rc)
    except:
        # if null or non-int
        try:
            rc_int = int(float(rc))
        except:
            rc_int = 0
    desc = item.get('description') or ''
    state = None
    # try patterns
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if not m:
        m = re.search(r',\s*([A-Z]{2})[,\s]', desc)
    if not m:
        m = re.search(r'([A-Z]{2}) location', desc)
    if m:
        state = m.group(1)
    else:
        # fallback: look for state codes from list
        states = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
        for s in states:
            if (','+s) in desc or (' '+s+' ') in desc or (s+' location') in desc:
                state = s
                break
    if not state:
        continue
    state_counts[state] = state_counts.get(state, 0) + rc_int
    state_businesses.setdefault(state, []).append(bid)
# determine top state
if not state_counts:
    top_state = None
    total_reviews = 0
    business_refs = []
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    total_reviews = state_counts[top_state]
    bids = state_businesses[top_state]
    # convert businessid_XX to businessref_XX
    business_refs = []
    for b in bids:
        if b is None: continue
        parts = b.split('_',1)
        if len(parts) == 2:
            business_refs.append('businessref_' + parts[1])
        else:
            business_refs.append('businessref_' + b)
result = {'top_state': top_state, 'total_reviews': total_reviews, 'business_refs': business_refs}
import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_heHrZb8iBsFnLQcPP2qvJneq': ['business', 'checkin'], 'var_call_dWKz4qgpk9ImF2D5NtiVKi7C': ['review', 'tip', 'user'], 'var_call_0yihErUwHGGDGnIs4qS1INo8': 'file_storage/call_0yihErUwHGGDGnIs4qS1INo8.json'}

exec(code, env_args)
