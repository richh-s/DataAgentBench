code = """import json
fp = var_call_XEkgfmj9JwPP0dFeduO2a8QB['path']
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

records = []
wifi_values = set()
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes')
    if not isinstance(attrs, dict):
        continue
    wifi = attrs.get('WiFi')
    if wifi is None:
        continue
    wifi_values.add(str(wifi))
    desc = rec.get('description') or ''
    state = None
    parts = [p.strip() for p in desc.split(',')]
    for p in parts:
        if len(p) == 2 and p.isupper() and p in us_states:
            state = p
            break
    records.append({'business_id': bid, 'wifi_raw': wifi, 'state': state})

offer_keywords = ['free','paid','yes','spotty','full','limited','guest']
wifi_businesses = []
for r in records:
    if r['state'] is None:
        continue
    sval = str(r['wifi_raw']).lower()
    if sval.startswith("u'") or sval.startswith('u"'):
        sval = sval[2:]
    sval = sval.strip("'\" ")
    offers = any(k in sval for k in offer_keywords)
    if offers:
        bref = r['business_id']
        if isinstance(bref, str) and bref.startswith('businessid_'):
            bref = bref.replace('businessid_', 'businessref_')
        wifi_businesses.append({'business_id': r['business_id'], 'business_ref': bref, 'state': r['state'], 'wifi': r['wifi_raw']})

out = {'num_data': len(data), 'num_wifi_records': len(records), 'num_wifi_offering_businesses_us': len(wifi_businesses), 'sample_wifi_values': list(sorted(wifi_values))[:50], 'wifi_businesses': wifi_businesses[:500]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json', 'var_call_XEkgfmj9JwPP0dFeduO2a8QB': {'path': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}}

exec(code, env_args)
