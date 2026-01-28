code = """import json, re

# var_call_IZ7Xl8OO6uQmBAMPvEWebOej is the storage key for the Mongo query result file path
path = var_call_IZ7Xl8OO6uQmBAMPvEWebOej
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

state_counts = {}
state_businesses = {}

for r in data:
    # Extract WiFi value
    wifi = None
    attrs = r.get('attributes') or {}
    wifi = attrs.get('WiFi')
    if wifi is None:
        continue
    wifi_s = str(wifi).lower()
    # Normalize and decide if offers WiFi: treat as offering unless value contains 'no' or 'none'
    if 'no' in wifi_s or 'none' in wifi_s:
        has_wifi = False
    else:
        has_wifi = True
    if not has_wifi:
        continue
    # Extract state from description
    desc = r.get('description','')
    state = None
    # Try pattern: ' in City, ST,' or ', City, ST,'
    m = re.search(r' in [^,]+,\s*([A-Z]{2})\b', desc)
    if not m:
        m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        cand = m.group(1)
        if cand in US_STATES:
            state = cand
    if not state:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_businesses.setdefault(state, []).append(r.get('business_id'))

# Find top state
if not state_counts:
    result = {"top_state": None, "count": 0, "business_refs": []}
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    count = state_counts[top_state]
    biz_ids = state_businesses.get(top_state, [])
    # Map businessid_ to businessref_
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids]
    result = {"top_state": top_state, "count": count, "business_refs": biz_refs}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ph2sjADjdgLcbK7lQLedGUrw': ['checkin', 'business'], 'var_call_LXxAdUGFtNaGYmRaX9ahBRVR': 'file_storage/call_LXxAdUGFtNaGYmRaX9ahBRVR.json', 'var_call_IZ7Xl8OO6uQmBAMPvEWebOej': 'file_storage/call_IZ7Xl8OO6uQmBAMPvEWebOej.json'}

exec(code, env_args)
