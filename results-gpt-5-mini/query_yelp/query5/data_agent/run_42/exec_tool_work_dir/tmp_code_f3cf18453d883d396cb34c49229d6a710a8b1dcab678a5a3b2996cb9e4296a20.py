code = """import json, re
# Read the Mongo query result from storage variable
path = var_call_XOSA9iI13kq2EaWHXmzBEWGB
with open(path, 'r') as f:
    records = json.load(f)

state_to_refs = {}
for r in records:
    biz_id = r.get('business_id')
    attrs = r.get('attributes') or {}
    wifi_val = attrs.get('WiFi')
    if wifi_val is None:
        continue
    w = str(wifi_val).lower()
    # consider offering wifi if value does not contain 'no'
    if "no" in w:
        continue
    desc = r.get('description') or ''
    m = re.search(r",\s*([A-Z]{2}),", desc)
    if not m:
        continue
    state = m.group(1)
    biz_ref = biz_id.replace('businessid_','businessref_')
    state_to_refs.setdefault(state, []).append(biz_ref)

# find top state
if not state_to_refs:
    result = {"top_state": None, "business_count": 0, "business_refs": []}
else:
    counts = {s: len(v) for s,v in state_to_refs.items()}
    max_count = max(counts.values())
    top_states = [s for s,c in counts.items() if c==max_count]
    top_state = sorted(top_states)[0]
    result = {"top_state": top_state, "business_count": len(state_to_refs[top_state]), "business_refs": state_to_refs[top_state]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XOSA9iI13kq2EaWHXmzBEWGB': 'file_storage/call_XOSA9iI13kq2EaWHXmzBEWGB.json'}

exec(code, env_args)
