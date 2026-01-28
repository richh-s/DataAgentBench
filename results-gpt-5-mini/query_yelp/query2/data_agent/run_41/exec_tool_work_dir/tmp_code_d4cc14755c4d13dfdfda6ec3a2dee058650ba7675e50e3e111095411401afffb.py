code = """import json, re

# Load tool results from storage files
with open(var_call_BLzEee95SoWiadwUuVQrCSAx) as f:
    businesses = json.load(f)
with open(var_call_MqzCh3vxz7RPrNkOmKWLP9E4) as f:
    reviews = json.load(f)

# Helper to extract state from description
state_map = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    # extract id number after underscore
    id_num = None
    if bid and '_' in bid:
        id_num = bid.split('_', 1)[1]
    # attempt to find two-letter state code in description
    state = None
    if desc:
        # common patterns: 'City, ST,' or 'City, ST' or 'in City, ST,'
        m = re.search(r',\s*([A-Z]{2})(?:\b|,)', desc)
        if m:
            state = m.group(1)
        else:
            # fallback: find last two-letter uppercase token
            tokens = re.findall(r'\b([A-Z]{2})\b', desc)
            if tokens:
                state = tokens[-1]
    if id_num:
        state_map[id_num] = state

# Sum review_count per state using business review_count
state_review_counts = {}
for b in businesses:
    bid = b.get('business_id')
    rc = b.get('review_count')
    # normalize
    try:
        rc_int = int(rc)
    except:
        try:
            rc_int = int(float(rc))
        except:
            rc_int = 0
    if bid and '_' in bid:
        id_num = bid.split('_',1)[1]
        state = state_map.get(id_num)
        if state:
            state_review_counts[state] = state_review_counts.get(state, 0) + rc_int

# Determine state with highest reviews
if not state_review_counts:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    max_state = max(state_review_counts.items(), key=lambda x: x[1])[0]
    total_reviews = state_review_counts[max_state]
    # Collect ratings for reviews that belong to businesses in that state
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        rating = r.get('rating')
        if not bref or '_' not in bref or rating is None:
            continue
        id_num = bref.split('_',1)[1]
        if state_map.get(id_num) == max_state:
            try:
                ratings.append(float(rating))
            except:
                pass
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
    else:
        avg_rating = None
    result = {"state": max_state, "total_reviews": total_reviews, "average_rating": round(avg_rating, 2) if avg_rating is not None else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lm4cunTDjD22IXrIVpaMTmMC': ['checkin', 'business'], 'var_call_BLzEee95SoWiadwUuVQrCSAx': 'file_storage/call_BLzEee95SoWiadwUuVQrCSAx.json', 'var_call_hWthTzHVoARoBw6gr6Cbrx2A': ['review', 'tip', 'user'], 'var_call_MqzCh3vxz7RPrNkOmKWLP9E4': 'file_storage/call_MqzCh3vxz7RPrNkOmKWLP9E4.json'}

exec(code, env_args)
