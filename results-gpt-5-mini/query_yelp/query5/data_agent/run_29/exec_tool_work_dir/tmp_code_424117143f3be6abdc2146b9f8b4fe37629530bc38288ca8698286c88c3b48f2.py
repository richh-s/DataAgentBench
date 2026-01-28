code = """import json, re
# var_call_dTdMzELB4RK2SW9tG9NA5SiF is a path to a JSON file with business records
p = var_call_dTdMzELB4RK2SW9tG9NA5SiF
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# US state codes
US_STATES = {"AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"}

def offers_wifi(val):
    if val is None:
        return False
    s = str(val).lower()
    s = s.replace('u', '')
    s = s.replace('\\'','')
    s = s.strip()
    if s in ('none', 'null', 'nan', "", 'n/a'):
        return False
    if 'no' in s and 'not' not in s:
        # treat any appearance of 'no' as no
        return False
    # if it contains free/paid/yes or does not contain 'no', consider it offers wifi
    if 'free' in s or 'paid' in s or 'yes' in s or 'limited' in s or 'signal' in s or "'" in s or 'wifi' in s:
        return True
    # default: if it's some other value but not 'no', consider True
    return True

ref_to_state = {}
business_refs = []
for rec in data:
    # attributes may be dict or string
    attrs = rec.get('attributes')
    wifi_val = None
    if isinstance(attrs, dict):
        wifi_val = attrs.get('WiFi')
    else:
        # attrs might be string like 'None'
        wifi_val = None
    if not offers_wifi(wifi_val):
        continue
    desc = rec.get('description', '') or ''
    # Look for pattern like 'in City, ST' or ', City, ST,'
    m = re.search(r' in [^,]+,\s*([A-Z]{2})\b', desc)
    if not m:
        m = re.search(r',\s*([A-Z]{2})\b', desc)
    if not m:
        continue
    state = m.group(1)
    if state not in US_STATES:
        continue
    bid = rec.get('business_id')
    if not bid:
        continue
    bref = bid.replace('businessid_', 'businessref_')
    ref_to_state[bref] = state
    business_refs.append(bref)

# Deduplicate
business_refs = sorted(list(set(business_refs)))
out = {"business_refs": business_refs, "ref_to_state": ref_to_state}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ZESpVOW8rLKXaIlEar1igsb3': ['business', 'checkin'], 'var_call_BkALsWIa0Flqm7nUNmc0QjvX': ['review', 'tip', 'user'], 'var_call_M0ZKJDSbejRHfgoAjAgTh3bp': 'file_storage/call_M0ZKJDSbejRHfgoAjAgTh3bp.json', 'var_call_dTdMzELB4RK2SW9tG9NA5SiF': 'file_storage/call_dTdMzELB4RK2SW9tG9NA5SiF.json'}

exec(code, env_args)
