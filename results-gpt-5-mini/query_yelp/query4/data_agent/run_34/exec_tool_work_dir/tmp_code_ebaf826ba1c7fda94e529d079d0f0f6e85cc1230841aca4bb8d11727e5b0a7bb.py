code = """import json
from collections import defaultdict

# Load query results from storage variables
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
    except Exception:
        rc = 0
    try:
        sr = float(r.get('sum_rating'))
    except Exception:
        sr = 0.0
    review_map[br] = {'review_count': rc, 'sum_rating': sr}

# Prepare category aggregations
cat_businesses = defaultdict(set)
cat_sum_rating = defaultdict(float)
cat_review_count = defaultdict(int)

for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes') or {}
    accept = attrs.get('BusinessAcceptsCreditCards')
    if accept is None:
        continue
    # normalize accept value
    val_str = str(accept).lower()
    val_str = val_str.replace("u'", "").replace("'", "").replace('"', "").strip()
    accepts = False
    if val_str in ('true', 't', '1', 'yes'):
        accepts = True
    elif val_str in ('false', 'f', '0', 'no'):
        accepts = False
    else:
        # if original was boolean True
        if isinstance(accept, bool) and accept:
            accepts = True
    if not accepts:
        continue
    cats = b.get('categories')
    if not cats:
        continue
    # Normalize categories
    cat_list = []
    if isinstance(cats, list):
        cat_list = cats
    elif isinstance(cats, str):
        parts = [p.strip() for p in cats.split(',') if p.strip()]
        cat_list = parts
    else:
        continue
    br = None
    if isinstance(bid, str):
        br = bid.replace('businessid_', 'businessref_')
    for c in cat_list:
        if not isinstance(c, str):
            continue
        c_norm = c.strip().strip('"').strip("'")
        if not c_norm:
            continue
        if br is not None:
            cat_businesses[c_norm].add(br)
        else:
            # skip if no mapping
            continue
        if br in review_map:
            cat_sum_rating[c_norm] += review_map[br]['sum_rating']
            cat_review_count[c_norm] += review_map[br]['review_count']

# Compile results
results = []
for c in cat_businesses:
    count = len(cat_businesses[c])
    total_reviews = cat_review_count.get(c, 0)
    total_sum = cat_sum_rating.get(c, 0.0)
    avg_rating = None
    if total_reviews > 0:
        avg_rating = total_sum / total_reviews
    results.append({'category': c, 'business_count': count, 'total_reviews': total_reviews, 'avg_rating': round(avg_rating, 4) if avg_rating is not None else None})

if not results:
    out = {'top_category': None, 'business_count': 0, 'avg_rating': None}
else:
    results_sorted = sorted(results, key=lambda x: (-x['business_count'], -(x['avg_rating'] or 0)))
    top = results_sorted[0]
    out = {'top_category': top['category'], 'business_count': top['business_count'], 'avg_rating': top['avg_rating']}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_D7CD2DQCTa8jHGewhSkVZids': ['business', 'checkin'], 'var_call_oegT4QrYcZ0vHVix0AWApWFP': ['review', 'tip', 'user'], 'var_call_NAqUUrEjnmpiDdYHYZai6POw': 'file_storage/call_NAqUUrEjnmpiDdYHYZai6POw.json', 'var_call_ew33PuycLWh81QohJv7XOYLK': 'file_storage/call_ew33PuycLWh81QohJv7XOYLK.json'}

exec(code, env_args)
