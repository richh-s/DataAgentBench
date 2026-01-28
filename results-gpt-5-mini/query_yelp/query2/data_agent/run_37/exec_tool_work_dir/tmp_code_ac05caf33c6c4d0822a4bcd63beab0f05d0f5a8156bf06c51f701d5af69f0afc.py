code = """import json, re
# Load the business collection result from the JSON file path stored in var_call_9FXhoAkEgUlY3ILP84RrZKxg
path = var_call_9FXhoAkEgUlY3ILP84RrZKxg
with open(path, 'r', encoding='utf-8') as f:
    businesses = json.load(f)

state_totals = {}
state_businesses = {}

pattern = re.compile(r",\s*([A-Z]{2})(?:[\s,]|$)")

for b in businesses:
    desc = b.get('description') or ''
    match = pattern.search(desc)
    state = None
    if match:
        state = match.group(1)
    # try alternative: look for ' in City, ST' pattern
    if not state:
        # find last occurrence of comma followed by space and two letters
        parts = re.findall(r",\s*([A-Z]{2})", desc)
        if parts:
            state = parts[-1]
    if not state:
        continue
    # review_count may be string or int
    rc = b.get('review_count', 0)
    try:
        rc_int = int(rc)
    except:
        rc_int = 0
    state_totals[state] = state_totals.get(state, 0) + rc_int
    state_businesses.setdefault(state, []).append(b.get('business_id'))

if not state_totals:
    result = {"error": "no states found"}
else:
    # find state with max total reviews
    top_state = max(state_totals.items(), key=lambda x: x[1])[0]
    total_reviews = state_totals[top_state]
    biz_ids = state_businesses.get(top_state, [])
    # convert businessid_# to businessref_#
    biz_refs = []
    for bid in biz_ids:
        if not bid:
            continue
        if bid.startswith('businessid_'):
            suffix = bid.split('businessid_')[-1]
            biz_refs.append('businessref_' + suffix)
        else:
            # attempt to replace first underscore
            parts = bid.split('_',1)
            if len(parts)==2:
                biz_refs.append('businessref_' + parts[1])
            else:
                biz_refs.append(bid)

    result = {
        'top_state': top_state,
        'total_reviews': total_reviews,
        'business_ref_count': len(biz_refs),
        'business_refs': biz_refs
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Z1L2Sg4P44zDIAeOtkLCdnkt': ['checkin', 'business'], 'var_call_Ha2U7zlK7vg2YAje53HOygrd': ['review', 'tip', 'user'], 'var_call_9FXhoAkEgUlY3ILP84RrZKxg': 'file_storage/call_9FXhoAkEgUlY3ILP84RrZKxg.json'}

exec(code, env_args)
