code = """import json, re
# var_call_7RDsQJ4weAgqRJhZMU3kruDs is provided by previous query_db call and contains the path to the JSON file
fp = var_call_7RDsQJ4weAgqRJhZMU3kruDs
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

# US state codes
us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}

# Collect unique WiFi values
wifi_values = set()
records = []
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes') or {}
    wifi = attrs.get('WiFi') if isinstance(attrs, dict) else None
    if wifi is None:
        continue
    wifi_values.add(str(wifi))
    desc = rec.get('description') or ''
    # try to extract state as two letter code using pattern ", <City>, ST," or ", <City>, ST "
    state = None
    # find pattern: in <addr> in City, ST,
    m = re.search(r",\s*([A-Za-z .'\-]+),\s*([A-Z]{2})[,\s]", desc)
    if m:
        st = m.group(2)
        if st in us_states:
            state = st
    else:
        # try other pattern like ", <City>, ST"
        m2 = re.search(r",\s*([A-Za-z .'\-]+),\s*([A-Z]{2})\b", desc)
        if m2:
            st = m2.group(2)
            if st in us_states:
                state = st
    records.append({'business_id': bid, 'wifi_raw': wifi, 'state': state, 'description': desc})

# Determine which wifi values likely indicate offering wifi
# We'll consider offering if the lowercased string contains 'free' or 'paid' or 'yes' or 'spotty' or 'no' indicates not offering
wifi_values_list = sorted(list(wifi_values))

# classify offering
offering_reasons = []
wifi_offer_set = set()
for val in wifi_values_list:
    s = str(val).lower()
    # remove leading u' or surrounding quotes
    s_clean = re.sub(r"^u?['\"]|['\"]$", "", s)
    # mark as offering if contains free/paid/yes
    offers = any(k in s_clean for k in ['free','paid','yes','spotty','full','limited','guest'])
    if offers:
        wifi_offer_set.add(val)

# Build list of businesses that offer wifi and have a US state
wifi_businesses = []
for r in records:
    if r['state'] is None:
        continue
    val = r['wifi_raw']
    # normalize raw to string
    sval = str(val)
    sval_clean = re.sub(r"^u?['\"]|['\"]$", "", sval).lower()
    offers = any(k in sval_clean for k in ['free','paid','yes','spotty','full','limited','guest'])
    if offers:
        # convert businessid_ to businessref_
        bref = None
        if isinstance(r['business_id'], str) and r['business_id'].startswith('businessid_'):
            bref = r['business_id'].replace('businessid_', 'businessref_')
        else:
            bref = r['business_id']
        wifi_businesses.append({'business_id': r['business_id'], 'business_ref': bref, 'state': r['state'], 'wifi': r['wifi_raw']})

# Prepare outputs
out = {
    'wifi_values_sample': wifi_values_list[:100],
    'num_wifi_records_processed': len(records),
    'num_wifi_offering_businesses_us': len(wifi_businesses),
    'wifi_businesses': wifi_businesses  # list may be used to query reviews
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_woj4tIn0U10exCkWbYaBd5Yf': ['checkin', 'business'], 'var_call_ijrp6giWNGCVcjhdTof3zBx6': ['review', 'tip', 'user'], 'var_call_qAmoAqh3sTe1FeETR7N45GKP': 'file_storage/call_qAmoAqh3sTe1FeETR7N45GKP.json', 'var_call_7RDsQJ4weAgqRJhZMU3kruDs': 'file_storage/call_7RDsQJ4weAgqRJhZMU3kruDs.json'}

exec(code, env_args)
