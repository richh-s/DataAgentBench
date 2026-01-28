code = """import json, re

# Load business data from the stored JSON file
with open(var_call_2WlZ388LhmZXZkp6DMJW9hWz, 'r') as f:
    data = json.load(f)

res = []
seen = set()
for r in data:
    attrs = r.get('attributes')
    if not attrs:
        continue
    if 'WiFi' not in attrs:
        continue
    val = str(attrs['WiFi'])
    val_low = val.lower()
    # Skip explicit 'no' entries
    if 'no' in val_low:
        continue
    # Try to extract state from description using regex
    desc = r.get('description', '')
    m = re.search(r',\s*([A-Z]{2})\s*,', desc)
    state = m.group(1) if m else None
    if not state:
        # Fallback: first occurrence of ", XX" where XX are caps
        m2 = re.search(r',\s*([A-Z]{2})\b', desc)
        if m2:
            state = m2.group(1)
    if not state:
        continue
    bid = r.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    if bref in seen:
        continue
    seen.add(bref)
    res.append({'business_id': bid, 'business_ref': bref, 'state': state, 'wifi_value': val})

# Output as JSON string
out = json.dumps(res)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2WlZ388LhmZXZkp6DMJW9hWz': 'file_storage/call_2WlZ388LhmZXZkp6DMJW9hWz.json'}

exec(code, env_args)
