code = """import json, re
# Load the business collection JSON from the provided storage file path
path = var_call_KaKUAMBmDPbvGrZNP2DEddeW
with open(path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

state_counts = {}
state_business_ids = {}

for b in businesses:
    biz_id = b.get('business_id')
    desc = b.get('description') or ''
    attrs = b.get('attributes')
    # determine WiFi availability
    wifi_val = None
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi')
    # if wifi_val is a string representation like "u'free'", normalize
    if isinstance(wifi_val, str):
        wifi_str = wifi_val.lower()
    else:
        wifi_str = ''
    # consider offering WiFi if wifi_str exists and does not contain 'no'
    offers_wifi = False
    if wifi_str and 'no' not in wifi_str:
        offers_wifi = True
    # parse state from description using regex
    state = None
    if isinstance(desc, str):
        m = re.search(r'in\s+[^,]+,\s*([A-Z]{2}),', desc)
        if m:
            state = m.group(1)
    if offers_wifi and state:
        state_counts[state] = state_counts.get(state, 0) + 1
        state_business_ids.setdefault(state, []).append(biz_id)

# determine top state
if state_counts:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    top_count = state_counts[top_state]
    biz_ids = state_business_ids[top_state]
else:
    top_state = None
    top_count = 0
    biz_ids = []

# convert businessid_... to businessref_...
business_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]

out = {
    'top_state': top_state,
    'wifi_business_count': top_count,
    'business_refs': business_refs
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_KaKUAMBmDPbvGrZNP2DEddeW': 'file_storage/call_KaKUAMBmDPbvGrZNP2DEddeW.json'}

exec(code, env_args)
