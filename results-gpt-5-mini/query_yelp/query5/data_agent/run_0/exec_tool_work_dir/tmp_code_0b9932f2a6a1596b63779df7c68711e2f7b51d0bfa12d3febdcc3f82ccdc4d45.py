code = """import json,re
path = var_call_LUR2w8pX0VJCm0Quj5CqYIer
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
out = []
for doc in data:
    bid = doc.get('business_id')
    attrs = doc.get('attributes') or {}
    wifi_raw = attrs.get('WiFi')
    if wifi_raw is None:
        continue
    wifi_str = str(wifi_raw).lower()
    # exclude explicit 'no'
    if 'no' in wifi_str:
        continue
    # include others
    desc = doc.get('description','') or ''
    state = None
    m = re.search(r',\s*([A-Z]{2}),', desc)
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r'in\s+.*?,\s*([A-Z]{2})\b', desc)
        if m2:
            state = m2.group(1)
    out.append({'business_id': bid, 'business_ref': bid.replace('businessid_','businessref_'), 'state': state})
# remove entries with null state
out = [o for o in out if o['state'] is not None]
# deduplicate by business_id
seen=set(); uniq=[]
for o in out:
    if o['business_id'] in seen: continue
    seen.add(o['business_id']); uniq.append(o)
import json
print("__RESULT__:")
print(json.dumps(uniq))"""

env_args = {'var_call_LUR2w8pX0VJCm0Quj5CqYIer': 'file_storage/call_LUR2w8pX0VJCm0Quj5CqYIer.json'}

exec(code, env_args)
