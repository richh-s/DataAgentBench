code = """import json, re

# Load business WiFi query result from storage
path = var_call_VCrWVqVG7q2B6wLW2XrbHi5O
with open(path, 'r') as f:
    data = json.load(f)

us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}

state_business = {}
all_refs = set()

for rec in data:
    desc = rec.get('description') or ''
    m = re.search(r' in [^,]+, ([A-Z]{2})', desc)
    state = None
    if m:
        state = m.group(1)
    else:
        m2 = re.search(r',\s*([A-Z]{2})[,\s]', desc)
        if m2:
            state = m2.group(1)
    if not state or state not in us_states:
        continue
    wifi_raw = None
    attrs = rec.get('attributes') or {}
    wifi_raw = attrs.get('WiFi')
    if wifi_raw is None:
        continue
    s = str(wifi_raw).lower()
    s_norm = re.sub(r"[^a-z]", "", s)
    if s_norm in ('no','none','false',''):
        continue
    # Consider it offers wifi
    bid = rec.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_','businessref_')
    state_business.setdefault(state, set()).add(bref)
    all_refs.add(bref)

# Convert sets to lists
state_business_lists = {k: sorted(list(v)) for k,v in state_business.items()}
all_refs_list = sorted(list(all_refs))

out = {'states': state_business_lists, 'business_refs': all_refs_list}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_SsLPa0PwZrecVBQneEZziJuN': ['checkin', 'business'], 'var_call_jnRqR7eAHwU3Z7VjxKzfWkpB': ['review', 'tip', 'user'], 'var_call_9PJVvAXphdniG47izkG6ZUrl': 'file_storage/call_9PJVvAXphdniG47izkG6ZUrl.json', 'var_call_VCrWVqVG7q2B6wLW2XrbHi5O': 'file_storage/call_VCrWVqVG7q2B6wLW2XrbHi5O.json'}

exec(code, env_args)
