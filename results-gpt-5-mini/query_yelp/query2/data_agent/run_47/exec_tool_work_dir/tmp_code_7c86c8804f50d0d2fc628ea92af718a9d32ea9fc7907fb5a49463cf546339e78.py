code = """import json
import re
import statistics

# Load data from previous tool results files
with open(var_call_weOWNpAaWSi9ktyh3yRQaSO3, 'r') as f:
    businesses = json.load(f)
with open(var_call_8EFT4sjM8LAMY11I4YX0xuOn, 'r') as f:
    reviews = json.load(f)

# Build business id to state mapping
biz_state = {}
state_pattern = re.compile(r",\s*([^,]+),\s*([A-Z]{2})(?:\b|,)")
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    # extract numeric suffix
    if not bid or '_' not in bid:
        continue
    num = bid.split('_', 1)[1]
    state = None
    m = state_pattern.search(desc)
    if m:
        # m.group(2) is state code
        state = m.group(2)
    # store state if found
    if state:
        biz_state[num] = state

# Aggregate reviews by state
state_counts = {}
state_ratings = {}
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    if not bref or '_' not in bref or rating is None:
        continue
    num = bref.split('_', 1)[1]
    state = biz_state.get(num)
    if not state:
        continue
    try:
        rating_val = float(rating)
    except:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_ratings.setdefault(state, []).append(rating_val)

# If no states, return empty
if not state_counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # find state with max reviews
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    count = state_counts[max_state]
    ratings = state_ratings.get(max_state, [])
    avg_rating = None
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
        # round to 3 decimals
        avg_rating = round(avg_rating, 3)
    result = {"state": max_state, "review_count": count, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IGmh0C3WUUbxMzpOEfaqJ6K7': ['checkin', 'business'], 'var_call_FElMo1J5nErSmukQXNU1NZ1b': ['review', 'tip', 'user'], 'var_call_weOWNpAaWSi9ktyh3yRQaSO3': 'file_storage/call_weOWNpAaWSi9ktyh3yRQaSO3.json', 'var_call_8EFT4sjM8LAMY11I4YX0xuOn': 'file_storage/call_8EFT4sjM8LAMY11I4YX0xuOn.json'}

exec(code, env_args)
