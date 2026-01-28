code = """import json, re
path = var_call_IZ7Xl8OO6uQmBAMPvEWebOej
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

state_counts = {}
state_businesses = {}

for r in data:
    attrs = r.get('attributes') or {}
    wifi = attrs.get('WiFi')
    if wifi is None:
        continue
    wifi_s = str(wifi).lower()
    if 'no' in wifi_s or 'none' in wifi_s:
        continue
    desc = r.get('description','')
    state = None
    # Try patterns
    m = re.search(r',\s*([A-Z]{2})\s*,', desc)
    if m and m.group(1) in US_STATES:
        state = m.group(1)
    if not state:
        m = re.search(r' in [^,]+,\s*([A-Z]{2})\b', desc)
        if m and m.group(1) in US_STATES:
            state = m.group(1)
    if not state:
        # find all uppercase two-letter tokens
        toks = re.findall(r'\b([A-Z]{2})\b', desc)
        for t in toks:
            if t in US_STATES:
                state = t
                break
    if not state:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_businesses.setdefault(state, []).append(r.get('business_id'))

if not state_counts:
    res = {"top_state": None, "count": 0, "business_refs": []}
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    biz_ids = state_businesses[top_state]
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids]
    res = {"top_state": top_state, "count": state_counts[top_state], "business_refs": biz_refs}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_Ph2sjADjdgLcbK7lQLedGUrw': ['checkin', 'business'], 'var_call_LXxAdUGFtNaGYmRaX9ahBRVR': 'file_storage/call_LXxAdUGFtNaGYmRaX9ahBRVR.json', 'var_call_IZ7Xl8OO6uQmBAMPvEWebOej': 'file_storage/call_IZ7Xl8OO6uQmBAMPvEWebOej.json', 'var_call_ujs7pHQTlXU6RQF5ifNLqS2w': {'top_state': None, 'count': 0, 'business_refs': []}, 'var_call_bm10a556i5bCp1IdhOAbOqfo': 'file_storage/call_bm10a556i5bCp1IdhOAbOqfo.json'}

exec(code, env_args)
