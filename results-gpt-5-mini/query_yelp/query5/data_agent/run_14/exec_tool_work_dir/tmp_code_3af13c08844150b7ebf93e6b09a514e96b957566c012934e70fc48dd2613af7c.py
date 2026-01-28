code = """import json, re

# Load business records from the stored JSON file
with open(var_call_2mQZXksl33KcC0GbmzZKG5d3, 'r') as f:
    records = json.load(f)

wifi_businesses = []

state_pattern = re.compile(r',\s*([A-Z]{2})[,\.]')
# Fallback pattern: 'in City, ST,' or just ', ST,'
for doc in records:
    business_id = doc.get('business_id')
    attrs = doc.get('attributes') or {}
    wifi_val = None
    # Try various casing
    for k in attrs:
        if k.lower() == 'wifi':
            wifi_val = attrs[k]
            break
    if wifi_val is None:
        continue
    wifi_str = str(wifi_val).lower()
    # Clean value to check for 'no'
    cleaned = re.sub("[^a-z]", "", wifi_str)
    if 'no' in cleaned:
        continue
    if cleaned == '':
        continue
    # Parse state from description
    desc = doc.get('description') or ''
    m = state_pattern.search(desc)
    state = None
    if m:
        state = m.group(1)
    else:
        # try alternate: 'in City, ST,' pattern
        m2 = re.search(r'in\s+[^,]+,\s*([A-Z]{2})', desc)
        if m2:
            state = m2.group(1)
    if state is None:
        # skip if no state
        continue
    business_ref = business_id.replace('businessid_', 'businessref_')
    wifi_businesses.append({'business_id': business_id, 'business_ref': business_ref, 'state': state, 'wifi_raw': wifi_val})

result = {'count_wifi_businesses': len(wifi_businesses), 'wifi_businesses': wifi_businesses}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_64XhkT1xjnWS5IJk13AjtdSC': ['checkin', 'business'], 'var_call_2mQZXksl33KcC0GbmzZKG5d3': 'file_storage/call_2mQZXksl33KcC0GbmzZKG5d3.json'}

exec(code, env_args)
