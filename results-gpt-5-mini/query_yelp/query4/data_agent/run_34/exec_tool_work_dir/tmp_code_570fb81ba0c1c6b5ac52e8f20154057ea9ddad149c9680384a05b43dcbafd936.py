code = """import json
from collections import defaultdict

# Load the full results from the stored JSON files
with open(var_call_NAqUUrEjnmpiDdYHYZai6POw, 'r') as f:
    businesses = json.load(f)
with open(var_call_ew33PuycLWh81QohJv7XOYLK, 'r') as f:
    reviews_agg = json.load(f)

# Build review aggregates map: business_ref -> (sum_rating, review_count)
review_map = {}
for r in reviews_agg:
    br = r.get('business_ref')
    try:
        rc = int(r.get('review_count'))
    except:
        rc = 0
    try:
        sr = float(r.get('sum_rating'))
    except:
        sr = 0.0
    review_map[br] = {'review_count': rc, 'sum_rating': sr}

# For each business that accepts credit cards, extract categories
cat_stats = {}
# We'll keep a set of business_refs per category to count unique businesses
cat_businesses = defaultdict(set)
cat_sum_rating = defaultdict(float)
cat_review_count = defaultdict(int)

for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes') or {}
    # Confirm BusinessAcceptsCreditCards truthy in various forms
    accept = attrs.get('BusinessAcceptsCreditCards')
    if accept is None:
        continue
    if isinstance(accept, bool):
        accepts = accept
    else:
        # String variants
        accepts = str(accept).lower() in ('true', "'true'", 't', '1')
    if not accepts:
        continue
    # Get categories; try multiple possible field names
    cats = b.get('categories')
    if not cats:
        # try 'category' or look in description? skip if none
        continue
    # Normalize categories into list
    cat_list = []
    if isinstance(cats, list):
        cat_list = cats
    else:
        # some entries are comma-separated strings
        if isinstance(cats, str):
            # remove surrounding brackets or quotes
            s = cats.strip()
            # split by comma
            parts = [p.strip() for p in s.split(',') if p.strip()]
            cat_list = parts
        else:
            # unknown format, skip
            continue
    # Map business_id to business_ref
    br = bid.replace('businessid_', 'businessref_') if isinstance(bid, str) else None
    for c in cat_list:
        # normalize category by stripping quotes
        c_norm = c.strip().strip("'\" ")
        if not c_norm:
            continue
        cat_businesses[c_norm].add(br)
        rv = review_map.get(br)
        if rv:
            cat_sum_rating[c_norm] += rv['sum_rating']
            cat_review_count[c_norm] += rv['review_count']

# Compute counts and average ratings
results = []
for c in cat_businesses:
    count = len(cat_businesses[c])
    total_reviews = cat_review_count.get(c, 0)
    total_sum = cat_sum_rating.get(c, 0.0)
    avg_rating = None
    if total_reviews > 0:
        avg_rating = total_sum / total_reviews
    results.append({'category': c, 'business_count': count, 'total_reviews': total_reviews, 'avg_rating': avg_rating})

# Find category with largest business_count
if not results:
    out = {'top_category': None, 'business_count': 0, 'avg_rating': None}
else:
    results_sorted = sorted(results, key=lambda x: (-x['business_count'], -(x['avg_rating'] or 0)))
    top = results_sorted[0]
    # Round avg_rating to 4 decimals if not None
    if top['avg_rating'] is not None:
        top_avg = round(top['avg_rating'], 4)
    else:
        top_avg = None
    out = {'top_category': top['category'], 'business_count': top['business_count'], 'avg_rating': top_avg}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_D7CD2DQCTa8jHGewhSkVZids': ['business', 'checkin'], 'var_call_oegT4QrYcZ0vHVix0AWApWFP': ['review', 'tip', 'user'], 'var_call_NAqUUrEjnmpiDdYHYZai6POw': 'file_storage/call_NAqUUrEjnmpiDdYHYZai6POw.json', 'var_call_ew33PuycLWh81QohJv7XOYLK': 'file_storage/call_ew33PuycLWh81QohJv7XOYLK.json'}

exec(code, env_args)
