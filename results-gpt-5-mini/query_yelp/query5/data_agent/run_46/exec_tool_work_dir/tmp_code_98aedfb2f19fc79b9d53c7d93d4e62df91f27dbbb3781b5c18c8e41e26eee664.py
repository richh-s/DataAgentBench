code = """import json, re
# var_call_lNKkfWJJX4LCo0BjC4JwWfAK contains path to JSON file with query results
fp = var_call_lNKkfWJJX4LCo0BjC4JwWfAK
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

state_counts = {}
state_business_ids = {}

for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes') or {}
    wifi_raw = None
    if isinstance(attrs, dict):
        # WiFi might be nested or have different key casing
        for k in attrs:
            if k.lower() == 'wifi':
                wifi_raw = attrs[k]
                break
    # Normalize wifi string
    wifi_flag = False
    if wifi_raw is not None:
        try:
            w = str(wifi_raw).lower()
            if 'no' in w:
                wifi_flag = False
            elif 'none' in w:
                wifi_flag = False
            else:
                # treat 'free', 'paid', 'yes', "u'free'" etc. as offering
                wifi_flag = True
        except Exception:
            wifi_flag = False
    # Extract state from description
    desc = rec.get('description') or ''
    state = None
    m = re.search(r"in\s+[^,]+,\s*([A-Z]{2})[,\s]", desc)
    if m:
        cand = m.group(1)
        if cand in us_states:
            state = cand
    # fallback: try last occurrence of ', ' then take two-letter before comma
    if not state:
        m2 = re.findall(r",\s*([A-Z]{2})[,\s]", desc)
        if m2:
            for cand in m2:
                if cand in us_states:
                    state = cand
                    break
    if state and wifi_flag:
        state_counts[state] = state_counts.get(state, 0) + 1
        state_business_ids.setdefault(state, []).append(bid)

# determine top state
if state_counts:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    top_count = state_counts[top_state]
    top_business_ids = state_business_ids.get(top_state, [])
else:
    top_state = None
    top_count = 0
    top_business_ids = []

out = {
    'top_state': top_state,
    'count': top_count,
    'business_ids': top_business_ids
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_x07oAuhWTqZMIy5fdjuj9v1q': ['business', 'checkin'], 'var_call_qKmdSTOXMctGRxPO6QYPOUue': ['review', 'tip', 'user'], 'var_call_V6QpZLl9ysxbV2KLsfJ9j8CZ': 'file_storage/call_V6QpZLl9ysxbV2KLsfJ9j8CZ.json', 'var_call_lNKkfWJJX4LCo0BjC4JwWfAK': 'file_storage/call_lNKkfWJJX4LCo0BjC4JwWfAK.json'}

exec(code, env_args)
