code = """import json
import re

# Load the business data from storage variable
file_path = var_call_CvKwb8XslONx1lfsFPefIFEa
with open(file_path, 'r') as f:
    data = json.load(f)

# Extract state from description using regex for two-letter state abbreviations
state_counts = {}
state_business_refs = {}

for rec in data:
    desc = rec.get('description') or ''
    # find all occurrences of a comma followed by space and two uppercase letters
    m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
    if m:
        state = m.group(1)
    else:
        # fallback: try uppercase word at end
        m2 = re.search(r"in\s+([A-Za-z\s]+),\s*([A-Z]{2})", desc)
        if m2:
            state = m2.group(2)
        else:
            state = None
    try:
        rc = int(rec.get('review_count') or 0)
    except:
        # if review_count is not numeric
        try:
            rc = int(float(rec.get('review_count')))
        except:
            rc = 0
    if state:
        state_counts[state] = state_counts.get(state, 0) + rc
        state_business_refs.setdefault(state, []).append(rec.get('business_id'))

# Find the state with highest number of reviews
if not state_counts:
    result = {'top_state': None, 'total_reviews': 0, 'business_refs': []}
else:
    top_state = max(state_counts.items(), key=lambda x: x[1])[0]
    total_reviews = state_counts[top_state]
    # Transform business_id to business_ref by replacing prefix
    business_refs = state_business_refs.get(top_state, [])
    business_refs_transformed = []
    for bid in business_refs:
        if bid is None:
            continue
        if bid.startswith('businessid_'):
            business_refs_transformed.append(bid.replace('businessid_', 'businessref_'))
        else:
            business_refs_transformed.append(bid)
    result = {'top_state': top_state, 'total_reviews': total_reviews, 'business_refs': business_refs_transformed}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_R4VAWuBKEM1yL68n1G0ZL6EA': ['checkin', 'business'], 'var_call_Xd66fok67Dl8Bz52C6ZMt5qS': ['review', 'tip', 'user'], 'var_call_CvKwb8XslONx1lfsFPefIFEa': 'file_storage/call_CvKwb8XslONx1lfsFPefIFEa.json'}

exec(code, env_args)
