code = """import json

# Load data from previous tool results
with open(var_call_F4cpcLsVLk6o6bMKnniDw6Im, 'r') as f:
    businesses = json.load(f)
with open(var_call_qDys7vlegvauaC4FyvXgJxAV, 'r') as f:
    reviews = json.load(f)

# Helper to extract numeric id from businessid_ or businessref_
def extract_num(s):
    if not isinstance(s, str):
        return None
    parts = s.split('_')
    if len(parts) < 2:
        return None
    return parts[-1]

# Build business info
biz_info = {}
for b in businesses:
    bid = b.get('business_id')
    num = extract_num(bid)
    if num is None:
        continue
    attrs = b.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            accepts = val
        elif isinstance(val, str):
            if val.lower() == 'true' or val == "True":
                accepts = True
    # categories may be missing or null
    cats = b.get('categories')
    cat_list = []
    if isinstance(cats, str):
        # split by comma
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    elif isinstance(cats, list):
        cat_list = [str(c).strip() for c in cats if c]
    # store
    biz_info[num] = {
        'business_id': bid,
        'accepts_credit': accepts,
        'categories': cat_list
    }

# Build reviews mapping: business num -> list of ratings
reviews_by_biz = {}
for r in reviews:
    bref = r.get('business_ref')
    num = extract_num(bref)
    if num is None:
        continue
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    reviews_by_biz.setdefault(num, []).append(rating)

# For each category, collect unique businesses that accept credit
from collections import defaultdict
cat_businesses = defaultdict(set)
for num, info in biz_info.items():
    if not info['accepts_credit']:
        continue
    for cat in info['categories']:
        cat_businesses[cat].add(num)

# If no categories found, exit with empty result
if not cat_businesses:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    # Compute counts
    counts = {cat: len(bset) for cat, bset in cat_businesses.items()}
    # Find category with max count (tie-breaker: lexicographically smallest)
    max_count = max(counts.values())
    max_cats = [cat for cat, cnt in counts.items() if cnt == max_count]
    chosen_cat = sorted(max_cats)[0]
    # Compute average rating across all reviews for businesses in this category
    biz_set = cat_businesses[chosen_cat]
    all_ratings = []
    for bnum in biz_set:
        all_ratings.extend(reviews_by_biz.get(bnum, []))
    if all_ratings:
        avg = sum(all_ratings) / len(all_ratings)
        avg = round(avg, 2)
    else:
        avg = None
    result = {"category": chosen_cat, "business_count": max_count, "average_rating": avg}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JyUYVsueP42n2gO3CzQygFBv': ['business', 'checkin'], 'var_call_Q3QQtlxyfI0mIzMBvJQyUDgX': ['review', 'tip', 'user'], 'var_call_F4cpcLsVLk6o6bMKnniDw6Im': 'file_storage/call_F4cpcLsVLk6o6bMKnniDw6Im.json', 'var_call_qDys7vlegvauaC4FyvXgJxAV': 'file_storage/call_qDys7vlegvauaC4FyvXgJxAV.json'}

exec(code, env_args)
