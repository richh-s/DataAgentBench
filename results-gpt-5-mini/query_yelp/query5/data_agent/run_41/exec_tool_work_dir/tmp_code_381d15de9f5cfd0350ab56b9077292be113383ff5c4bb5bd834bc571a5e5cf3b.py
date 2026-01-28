code = """import json, re
fp = var_call_XEkgfmj9JwPP0dFeduO2a8QB['path']
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}

wifi_values = set()
records = []
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes') or {}
    # attrs may be dict or string; handle if string by attempting eval? skip if not dict
    wifi = None
    if isinstance(attrs, dict):
        wifi = attrs.get('WiFi')
    else:
        # try to find WiFi in string
        m = re.search(r"WiFi\s*[:=]\s*'?(\w+)'?", str(attrs))
        if m:
            wifi = m.group(1)
    if wifi is None:
        continue
    wifi_values.add(str(wifi))
    desc = rec.get('description') or ''
    state = None
    # try to extract state as two uppercase letters
    m = re.search(r",\s*([A-Za-z .'-]+),\s*([A-Z]{2})[,\s]", desc)
    if m and m.group(2) in us_states:
        state = m.group(2)
    else:
        m2 = re.search(r",\s*([A-Za-z .'-]+),\s*([A-Z]{2})\b", desc)
        if m2 and m2.group(2) in us_states:
            state = m2.group(2)
    records.append({'business_id': bid, 'wifi_raw': wifi, 'state': state, 'description': desc})

wifi_values_list = sorted(list(wifi_values))

wifi_businesses = []
for r in records:
    if r['state'] is None:
        continue
    sval = str(r['wifi_raw'])
    sval_clean = re.sub(r"^u?['\"]|['\"]$", "", sval).lower()
    offers = any(k in sval_clean for k in ['free','paid','yes','spotty','full','limited','guest'])
    if offers:
        bref = r['business_id']
        if isinstance(bref, str) and bref.startswith('businessid_'):
            bref = bref.replace('businessid_', 'businessref_')
        wifi_businesses.append({'business_id': r['business_id'], 'business_ref': bref, 'state': r['state'], 'wifi': r['wifi_raw']})

out = {
    'wifi_values_sample': wifi_values_list[:100],
    'num_wifi_records_processed': len(records),
    'num_wifi_offering_businesses_us': len(wifi_businesses),
    'wifi_businesses': wifi_businesses[:200]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json', 'var_call_XEkgfmj9JwPP0dFeduO2a8QB': {'path': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}}

exec(code, env_args)
