code = """import json, re, pandas as pd
from collections import defaultdict

# Load full results from files
with open(var_call_8VAOKKnRYz3JLHEuxWriwNqh, 'r') as f:
    business_data = json.load(f)
with open(var_call_S1DtBNudHJyHVlDv1Z2965gJ, 'r') as f:
    review_data = json.load(f)

# Extract state from description, assume pattern 'City, ST'
state_map = {}
state_pattern = re.compile(r',\s*([A-Z]{2})\b')
for rec in business_data:
    desc = rec.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    bid = rec['business_id']
    # map businessid_X -> state
    state_map[bid] = state

# Aggregate reviews per state
state_review_count = defaultdict(int)
state_rating_sum = defaultdict(float)

for rec in review_data:
    bref = rec['business_ref']
    # convert businessref_X -> businessid_X
    bid = 'businessid_' + bref.split('_', 1)[1]
    state = state_map.get(bid)
    if not state:
        continue
    rating = float(rec['rating']) if rec['rating'] is not None else None
    if rating is None:
        continue
    state_review_count[state] += 1
    state_rating_sum[state] += rating

# Find state with max reviews
if not state_review_count:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    max_state = max(state_review_count, key=lambda s: state_review_count[s])
    avg_rating = state_rating_sum[max_state] / state_review_count[max_state]
    result = {
        "state": max_state,
        "review_count": state_review_count[max_state],
        "average_rating": round(avg_rating, 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_8VAOKKnRYz3JLHEuxWriwNqh': 'file_storage/call_8VAOKKnRYz3JLHEuxWriwNqh.json', 'var_call_S1DtBNudHJyHVlDv1Z2965gJ': 'file_storage/call_S1DtBNudHJyHVlDv1Z2965gJ.json'}

exec(code, env_args)
