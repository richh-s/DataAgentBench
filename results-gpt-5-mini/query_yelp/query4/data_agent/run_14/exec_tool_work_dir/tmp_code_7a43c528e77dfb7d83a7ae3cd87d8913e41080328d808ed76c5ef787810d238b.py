code = """import json
import ast
from collections import defaultdict

# Load data from storage-provided file paths
biz_path = var_call_zenaF9gAgfmTXB50cZZX9sgh
rev_path = var_call_qlkHo3dF8SjDijFURBwJADSJ

with open(biz_path, 'r') as f:
    businesses = json.load(f)
with open(rev_path, 'r') as f:
    reviews = json.load(f)

# Helper to parse attributes which may be dict, None, or string representation
def parse_attributes(attr):
    if attr is None:
        return {}
    if isinstance(attr, dict):
        return attr
    if isinstance(attr, str):
        s = attr.strip()
        if s.lower() == 'none' or s == '':
            return {}
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, dict):
                return parsed
            else:
                return {}
        except Exception:
            return {}
    return {}

# Build mapping of business_ref -> categories for businesses that accept credit cards
bizref_to_categories = {}
category_to_businesses = defaultdict(set)
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    attrs = parse_attributes(b.get('attributes'))
    accepts = False
    val = attrs.get('BusinessAcceptsCreditCards')
    if isinstance(val, bool):
        accepts = val
    elif isinstance(val, str):
        if val.strip().lower() == 'true':
            accepts = True
    # If attribute not present, treat as False
    if not accepts:
        continue
    # get categories
    cats = b.get('categories')
    if cats is None:
        continue
    # categories might be a list or a string
    if isinstance(cats, list):
        cat_list = [c.strip() for c in cats if c and c.strip()]
    else:
        # string, split by comma
        cat_list = [c.strip() for c in str(cats).split(',') if c and c.strip()]
    if not cat_list:
        continue
    # convert businessid_ -> businessref_
    bizref = bid.replace('businessid_', 'businessref_')
    bizref_to_categories[bizref] = cat_list
    for c in cat_list:
        category_to_businesses[c].add(bizref)

# Build category -> list of ratings (from reviews of businesses in that category)
category_ratings = defaultdict(list)
for r in reviews:
    bref = r.get('business_ref')
    if bref in bizref_to_categories:
        rating_raw = r.get('rating')
        try:
            rating = float(rating_raw)
        except Exception:
            continue
        for c in bizref_to_categories[bref]:
            category_ratings[c].append(rating)

# Compute counts and average ratings
results = []
for c, bizset in category_to_businesses.items():
    count = len(bizset)
    ratings = category_ratings.get(c, [])
    avg = None
    if ratings:
        avg = sum(ratings) / len(ratings)
    results.append({'category': c, 'business_count': count, 'average_rating': avg})

# Find category with largest number of businesses (tie-breaker: higher avg rating, then alphabetical)
if not results:
    out = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # sort by business_count desc, average_rating desc (None treated as -inf), category asc
    def avg_key(x):
        return x['average_rating'] if x['average_rating'] is not None else -999
    results_sorted = sorted(results, key=lambda x: (-x['business_count'], -avg_key(x), x['category']))
    top = results_sorted[0]
    # round average_rating to 2 decimals if not None
    if top['average_rating'] is not None:
        top['average_rating'] = round(top['average_rating'], 2)
    out = top

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_0QTDBTRd8H2RpxhSyMvftFu1': ['checkin', 'business'], 'var_call_VJcMYyiV5SnGv91Ebp3eBv6h': ['review', 'tip', 'user'], 'var_call_zenaF9gAgfmTXB50cZZX9sgh': 'file_storage/call_zenaF9gAgfmTXB50cZZX9sgh.json', 'var_call_qlkHo3dF8SjDijFURBwJADSJ': 'file_storage/call_qlkHo3dF8SjDijFURBwJADSJ.json'}

exec(code, env_args)
