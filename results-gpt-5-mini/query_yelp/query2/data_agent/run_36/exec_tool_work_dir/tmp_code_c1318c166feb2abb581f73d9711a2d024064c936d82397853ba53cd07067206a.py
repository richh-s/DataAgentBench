code = """import json
import re
from statistics import mean

# Load data from stored JSON files
with open(var_call_xkoVjzxXHbeGfHh6aW6ERGFi, 'r') as f:
    businesses = json.load(f)
with open(var_call_4lgLaNEZ0r13ONlJibRlezfH, 'r') as f:
    reviews = json.load(f)

# Build mapping from numeric business id to state code
id_to_state = {}
state_pattern = re.compile(r',\s*([A-Z]{2})(?:\b|,)', re.IGNORECASE)
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    if not bid:
        continue
    parts = bid.split('_')
    if len(parts) < 2:
        continue
    num = parts[-1]
    # Try to find state as two-letter code
    m = state_pattern.search(desc)
    state = None
    if m:
        state = m.group(1).upper()
    id_to_state[num] = state

# Process reviews: map to business numeric id and collect ratings per state
state_ratings = {}
state_counts = {}
for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    if bref is None or rating is None:
        continue
    parts = str(bref).split('_')
    if len(parts) < 2:
        continue
    num = parts[-1]
    state = id_to_state.get(num)
    if state is None:
        continue
    try:
        rating_val = float(rating)
    except:
        continue
    state_counts[state] = state_counts.get(state, 0) + 1
    state_ratings.setdefault(state, []).append(rating_val)

# Find state with highest number of reviews
if not state_counts:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    max_state = max(state_counts.items(), key=lambda x: x[1])[0]
    max_count = state_counts[max_state]
    avg_rating = mean(state_ratings[max_state]) if state_ratings.get(max_state) else None
    # Round average rating to 3 decimal places
    if avg_rating is not None:
        avg_rating = round(avg_rating, 3)
    result = {"state": max_state, "review_count": max_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EkXVNfSNqsRi0iBzk8Yu1sir': ['checkin', 'business'], 'var_call_UJma4d1DZDPV95MDTEKNWc8q': ['review', 'tip', 'user'], 'var_call_xkoVjzxXHbeGfHh6aW6ERGFi': 'file_storage/call_xkoVjzxXHbeGfHh6aW6ERGFi.json', 'var_call_4lgLaNEZ0r13ONlJibRlezfH': 'file_storage/call_4lgLaNEZ0r13ONlJibRlezfH.json'}

exec(code, env_args)
