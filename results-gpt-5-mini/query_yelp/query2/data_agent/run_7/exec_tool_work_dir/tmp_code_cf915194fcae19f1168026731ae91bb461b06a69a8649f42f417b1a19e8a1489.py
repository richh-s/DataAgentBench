code = """import json
import re

# Load large JSON results from files
with open(var_call_kVdGyPavQX4AK5RGdR21P5Ma, 'r') as f:
    businesses = json.load(f)
with open(var_call_60vF9iczLhy78Yh9hV17HMBy, 'r') as f:
    reviews = json.load(f)

# Build mapping from business_ref to state using business descriptions
business_ref_to_state = {}
state_reviewcount = {}

for b in businesses:
    bid = b.get('business_id')  # e.g., businessid_49
    desc = b.get('description', '') or ''
    # extract state abbreviation after a comma, take last match if multiple
    matches = re.findall(r',\s*([A-Z]{2})(?:\b|,)', desc)
    state = matches[-1] if matches else None
    if state:
        # map to businessref_x
        bref = bid.replace('businessid_', 'businessref_')
        business_ref_to_state[bref] = state
        # sum review_count from business collection (string -> int)
        try:
            rc = int(b.get('review_count') or 0)
        except:
            try:
                rc = int(float(b.get('review_count')))
            except:
                rc = 0
        state_reviewcount[state] = state_reviewcount.get(state, 0) + rc

# Find state with max reviews
if not state_reviewcount:
    result = {"state": None, "total_reviews": 0, "avg_rating": None}
else:
    max_state = max(state_reviewcount.items(), key=lambda x: x[1])[0]
    total_reviews = state_reviewcount[max_state]

    # Compute average rating of businesses in that state using review records
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if bref in business_ref_to_state and business_ref_to_state[bref] == max_state:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        avg_rating = round(avg_rating, 3)
    else:
        avg_rating = None

    result = {"state": max_state, "total_reviews": total_reviews, "avg_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ACtAR3UbFe1Uewacf0rOGpfx': ['checkin', 'business'], 'var_call_HvPq5ukRknEDcATLWUw3wK6L': ['review', 'tip', 'user'], 'var_call_kVdGyPavQX4AK5RGdR21P5Ma': 'file_storage/call_kVdGyPavQX4AK5RGdR21P5Ma.json', 'var_call_60vF9iczLhy78Yh9hV17HMBy': 'file_storage/call_60vF9iczLhy78Yh9hV17HMBy.json'}

exec(code, env_args)
