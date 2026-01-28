code = """import json
import re

# Load the Mongo query result from storage variable
path = var_call_lxffYFPxofRD6xUi4HnwHzM2
with open(path, 'r') as f:
    data = json.load(f)

state_sums = {}
state_businesses = {}

for rec in data:
    bid = rec.get('business_id')
    rc = rec.get('review_count')
    desc = rec.get('description') or ''
    # normalize review_count
    try:
        rc_int = int(rc)
    except:
        try:
            rc_int = int(float(rc))
        except:
            rc_int = 0
    # extract state: look for pattern 'in <City>, ST' or ', ST,' after 'Located'
    state = None
    if desc:
        m = re.search(r'in [^,]+, ([A-Z]{2})(?:\b|,)', desc)
        if not m:
            m = re.search(r', ([A-Z]{2})(?:,|$)', desc)
        if m:
            state = m.group(1)
    if not state:
        # fallback: try last two uppercase letters in description
        m = re.search(r'([A-Z]{2})', desc)
        if m:
            state = m.group(1)
    if not state:
        continue
    state_sums[state] = state_sums.get(state, 0) + rc_int
    state_businesses.setdefault(state, []).append(bid)

# determine state with max reviews
if not state_sums:
    result = {"top_state": None, "total_reviews": 0, "business_refs": []}
else:
    top_state = max(state_sums.items(), key=lambda x: x[1])[0]
    total_reviews = state_sums[top_state]
    bids = state_businesses[top_state]
    # convert businessid_<n> -> businessref_<n>
    bre = []
    for b in bids:
        if isinstance(b, str) and b.startswith('businessid_'):
            suffix = b.split('businessid_',1)[1]
            bre.append('businessref_' + suffix)
        else:
            # try split on last _
            parts = b.split('_',1)
            if len(parts) == 2:
                bre.append('businessref_' + parts[1])
    result = {"top_state": top_state, "total_reviews": total_reviews, "business_refs": bre}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xWfIHppBYVI5V3bR6C567uBd': ['checkin', 'business'], 'var_call_lxffYFPxofRD6xUi4HnwHzM2': 'file_storage/call_lxffYFPxofRD6xUi4HnwHzM2.json'}

exec(code, env_args)
