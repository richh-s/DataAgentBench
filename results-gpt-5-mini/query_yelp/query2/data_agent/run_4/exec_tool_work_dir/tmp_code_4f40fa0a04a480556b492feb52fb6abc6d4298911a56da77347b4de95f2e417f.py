code = """import json, re

# Load data from storage-provided file paths
with open(var_call_UdvcaEGMRioHNIw0eVlpesbL, 'r') as f:
    businesses = json.load(f)
with open(var_call_I2mwhJf9JHTS9DzIjs8VssKp, 'r') as f:
    reviews = json.load(f)

# Build mapping from business numeric id to state and review_count
id_to_state = {}
for b in businesses:
    bid = b.get('business_id')
    rc = b.get('review_count')
    desc = b.get('description') or ''
    # extract numeric suffix
    suf = None
    if isinstance(bid, str) and '_' in bid:
        suf = bid.split('_', 1)[1]
    # extract state code from description
    state = None
    m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
    if m:
        state = m.group(1)
    # convert review_count to int if possible
    try:
        rc_int = int(rc)
    except Exception:
        rc_int = 0
    if suf is not None:
        id_to_state[suf] = {'state': state, 'review_count': rc_int}

# Aggregate total review_count by state
from collections import defaultdict
state_review_totals = defaultdict(int)
for suf, info in id_to_state.items():
    st = info['state']
    if st:
        state_review_totals[st] += info['review_count']

# Find state with highest number of reviews
if not state_review_totals:
    result = {'state': None, 'total_reviews': 0, 'average_rating': None}
else:
    top_state = max(state_review_totals.items(), key=lambda x: x[1])[0]
    total_reviews = state_review_totals[top_state]

    # Collect ratings for reviews whose business_ref maps to top_state
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if isinstance(bref, str) and '_' in bref:
            suf = bref.split('_', 1)[1]
            info = id_to_state.get(suf)
            if info and info.get('state') == top_state:
                try:
                    ratings.append(float(r.get('rating')))
                except Exception:
                    pass
    avg_rating = None
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
    result = {'state': top_state, 'total_reviews': total_reviews, 'average_rating': round(avg_rating, 4) if avg_rating is not None else None}

# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SbFyBSfytkx44ItkNQ2PEtB4': ['checkin', 'business'], 'var_call_gLQGPQP2MLPaFdU5r8wjflqs': ['review', 'tip', 'user'], 'var_call_UdvcaEGMRioHNIw0eVlpesbL': 'file_storage/call_UdvcaEGMRioHNIw0eVlpesbL.json', 'var_call_I2mwhJf9JHTS9DzIjs8VssKp': 'file_storage/call_I2mwhJf9JHTS9DzIjs8VssKp.json'}

exec(code, env_args)
