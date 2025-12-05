code = """import json, re, pandas as pd
from collections import defaultdict

# Load full results if they are file paths
business_data = var_call_lz9H7PpnjZmk4I1kOv0RyUnU
if isinstance(business_data, str):
    with open(business_data, 'r') as f:
        business_data = json.load(f)

review_data = var_call_xDekiNvSWWwWFtZ7npi6r3wh
if isinstance(review_data, str):
    with open(review_data, 'r') as f:
        review_data = json.load(f)

# Extract state from description assuming pattern "<city>, <ST>" or "in <City>, <ST>"
state_map = {}
state_pattern = re.compile(r",\s*([A-Z]{2})[\s,]")

for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    bid = b.get('business_id')
    if bid:
        state_map[bid] = state

# Map business_ref to business_id by replacing prefix
reviews_by_state = defaultdict(list)
for r in review_data:
    bref = r.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    state = state_map.get(bid)
    if not state:
        continue
    try:
        rating = float(r.get('rating'))
    except (TypeError, ValueError):
        continue
    reviews_by_state[state].append(rating)

# Compute counts and average ratings
summary = []
for state, ratings in reviews_by_state.items():
    count = len(ratings)
    avg = sum(ratings) / count if count else None
    summary.append({'state': state, 'review_count': count, 'avg_rating': avg})

# Find state with max reviews
if summary:
    summary_sorted = sorted(summary, key=lambda x: x['review_count'], reverse=True)
    top = summary_sorted[0]
    result = {
        'state_with_most_reviews': top['state'],
        'number_of_reviews': top['review_count'],
        'average_rating_in_state': top['avg_rating']
    }
else:
    result = {
        'error': 'No states with reviews found'
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lz9H7PpnjZmk4I1kOv0RyUnU': 'file_storage/call_lz9H7PpnjZmk4I1kOv0RyUnU.json', 'var_call_xDekiNvSWWwWFtZ7npi6r3wh': 'file_storage/call_xDekiNvSWWwWFtZ7npi6r3wh.json'}

exec(code, env_args)
