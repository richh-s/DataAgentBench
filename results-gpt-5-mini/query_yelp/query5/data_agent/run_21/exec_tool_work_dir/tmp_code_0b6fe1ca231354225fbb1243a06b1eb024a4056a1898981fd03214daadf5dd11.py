code = """import json, re
fp = var_call_jMnTfOXhNhOpuKrxHpCUinQp
with open(fp, 'r', encoding='utf-8') as f:
    records = json.load(f)

wifi_businesses = []
for r in records:
    attrs = r.get('attributes') or {}
    wifi_val = attrs.get('WiFi')
    if not wifi_val:
        continue
    s = str(wifi_val).lower()
    s = re.sub(r"^u?['\"]|['\"]$", '', s)
    s = s.strip()
    if 'no' in s:
        continue
    desc = r.get('description') or ''
    state = None
    m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
        if m2:
            state = m2.group(1)
    if not state:
        continue
    business_id = r.get('business_id')
    if not business_id:
        continue
    business_ref = business_id.replace('businessid_', 'businessref_')
    wifi_businesses.append({'business_id': business_id, 'business_ref': business_ref, 'state': state, 'wifi_raw': wifi_val})

print("__RESULT__:")
print(json.dumps(wifi_businesses))"""

env_args = {'var_call_ogAXyUAbzhdfA7wxn0QSesde': ['business', 'checkin'], 'var_call_GKBL2knORpUCjBgP3uUpLRSi': ['review', 'tip', 'user'], 'var_call_jMnTfOXhNhOpuKrxHpCUinQp': 'file_storage/call_jMnTfOXhNhOpuKrxHpCUinQp.json'}

exec(code, env_args)
