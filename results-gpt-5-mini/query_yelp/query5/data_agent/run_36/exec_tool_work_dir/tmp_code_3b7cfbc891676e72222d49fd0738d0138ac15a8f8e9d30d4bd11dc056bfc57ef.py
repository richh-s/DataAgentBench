code = """import json
import re

# Load the large Mongo query result from storage file
path = var_call_HRbzImfiTlPYDcmxv9Hcahb4
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# US state codes
us_states = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"}

biz_state_map = {}
refs = []
state_counts = {}

for r in records:
    bid = r.get('business_id')
    attrs = r.get('attributes') or {}
    wifi = attrs.get('WiFi') if isinstance(attrs, dict) else None
    if wifi is None:
        continue
    # normalize wifi string
    wifi_str = str(wifi).lower()
    # remove non-letter chars except spaces
    wifi_clean = re.sub("[^a-z ]", "", wifi_str)
    wifi_clean = wifi_clean.strip()
    # Exclude entries that explicitly say no
    if 'no' in wifi_clean.split():
        continue
    # Consider this business offers wifi
    desc = r.get('description') or ''
    # try to find state code like ', XX' in description
    m = re.search(r",\s*([A-Z]{2})\b", desc)
    state = None
    if m:
        code = m.group(1)
        if code in us_states:
            state = code
    # If no match, try patterns like 'City, StateName' - extract two-letter at end of line
    if state is None:
        # fallback: look for last two-letter all-caps token
        toks = re.findall(r"\b([A-Z]{2})\b", desc)
        for t in reversed(toks):
            if t in us_states:
                state = t
                break
    if state is None:
        continue
    # convert business_id prefix
    biz_ref = bid.replace('businessid_', 'businessref_')
    refs.append(biz_ref)
    biz_state_map[biz_ref] = state
    state_counts[state] = state_counts.get(state, 0) + 1

output = {
    'business_refs': refs,
    'biz_state_map': biz_state_map,
    'state_counts': state_counts
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_FcU8ULKgLTvgq2xHt8RuPo4k': ['checkin', 'business'], 'var_call_HRbzImfiTlPYDcmxv9Hcahb4': 'file_storage/call_HRbzImfiTlPYDcmxv9Hcahb4.json'}

exec(code, env_args)
