code = """import json, re
# var_call_JyRpeMYmyxWIClXmvLS2smg9 is the storage key containing the JSON file path
path = var_call_JyRpeMYmyxWIClXmvLS2smg9
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

state_businesses = {}

for b in data:
    attrs = b.get('attributes')
    if not attrs or not isinstance(attrs, dict):
        continue
    # Normalize keys: some values may be like "u'free'" or "'free'"
    wifi_val = None
    # Keys might be exactly 'WiFi' according to description
    for k in attrs:
        if k and k.lower() == 'wifi':
            wifi_val = attrs[k]
            break
    if wifi_val is None:
        continue
    # Convert to string and normalize
    try:
        sval = str(wifi_val).lower()
    except:
        continue
    # Determine if offers wifi: exclude values that contain 'no' or 'none' or 'false'
    if 'no' in sval or 'none' in sval or 'false' in sval:
        continue
    # Otherwise consider it offers wifi
    desc = b.get('description','') or ''
    # Try to extract state as two-letter uppercase code after a comma
    # Look for pattern: ", <city>, <ST>" or ", <city>, <ST>," or ", <city>, <ST>"
    # We'll search for ", <ANY>, <ST>" pattern
    state = None
    # A simpler approach: find occurrences of ", {city}, {ST}" by splitting on ' in '
    # But description examples have 'Located at 123 in City, ST,' so find last occurrence of ', ' + 2 letters + ','
    m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
    if m:
        state = m.group(1)
    else:
        # try alternative: look for ' in City, ST' pattern
        m2 = re.search(r"in\s+[^,]+,\s*([A-Z]{2})", desc)
        if m2:
            state = m2.group(1)
    if not state:
        # skip if state not found
        continue
    bid = b.get('business_id')
    if not bid:
        continue
    # map to business_ref prefix
    bref = bid.replace('businessid_', 'businessref_')
    state_businesses.setdefault(state, []).append(bref)

# find top state
if not state_businesses:
    result = {'top_state': None, 'business_count': 0, 'business_refs': []}
else:
    top_state = max(state_businesses.items(), key=lambda x: len(x[1]))
    state_code = top_state[0]
    refs = top_state[1]
    result = {'top_state': state_code, 'business_count': len(refs), 'business_refs': refs}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JyRpeMYmyxWIClXmvLS2smg9': 'file_storage/call_JyRpeMYmyxWIClXmvLS2smg9.json', 'var_call_n8KQlG9izEaUuRYwubmxzxcY': ['business', 'checkin'], 'var_call_wRGEkCfUAi4xzTqkqLjbIcGl': ['review', 'tip', 'user']}

exec(code, env_args)
