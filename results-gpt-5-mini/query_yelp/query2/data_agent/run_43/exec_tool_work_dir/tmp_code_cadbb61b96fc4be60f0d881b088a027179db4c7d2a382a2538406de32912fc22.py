code = """import json, re

# Load data files from storage variables
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)
with open(var_call_n0S2syUfDJf7pjVSheCo8pDc, 'r') as f:
    reviews = json.load(f)

# Build mapping from businessref to state, and collect business review_counts
ref_to_state = {}
state_reviewcount = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    rc = b.get('review_count')
    # normalize review_count
    try:
        rc_int = int(rc)
    except:
        try:
            rc_int = int(float(rc))
        except:
            rc_int = 0
    if bid and '_' in bid:
        suffix = bid.split('_',1)[1]
        bref = 'businessref_' + suffix
    else:
        continue
    # extract state (two uppercase letters) from description
    state = None
    # common pattern: "in City, ST" or ", ST," or ", ST"
    m = re.search(r"in [^,]+,\s*([A-Z]{2})\b", desc)
    if not m:
        m = re.search(r",\s*([A-Z]{2})\b", desc)
    if m:
        state = m.group(1)
    if state:
        ref_to_state[bref] = state
        state_reviewcount[state] = state_reviewcount.get(state, 0) + rc_int

# Determine state with highest number of reviews (by business.review_count sum)
if not state_reviewcount:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    state_max = max(state_reviewcount.items(), key=lambda x: x[1])[0]
    total_reviews = state_reviewcount[state_max]
    # collect ratings for reviews linked to businesses in that state
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if bref in ref_to_state and ref_to_state[bref] == state_max:
            try:
                ratings.append(float(r.get('rating')))
            except:
                pass
    if ratings:
        avg_rating = sum(ratings)/len(ratings)
    else:
        avg_rating = None
    result = {"state": state_max, "total_reviews": total_reviews, "average_rating": round(avg_rating, 3) if avg_rating is not None else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json'}

exec(code, env_args)
