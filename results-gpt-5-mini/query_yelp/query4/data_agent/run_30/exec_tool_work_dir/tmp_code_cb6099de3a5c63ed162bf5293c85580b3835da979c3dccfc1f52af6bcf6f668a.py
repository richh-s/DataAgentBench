code = """import json
import re
from collections import defaultdict

# Load large results from files referenced by storage variables
with open(var_call_DYOmUKWQbTEskr11JQeVelj7, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_2m0iQ5foTc1FNVIoZVdOohmI, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Build mapping from business_id to list of ratings
ratings_map = defaultdict(list)
for r in reviews:
    br = r.get('business_ref')
    if not br:
        continue
    # convert businessref_N -> businessid_N
    bid = br.replace('businessref_', 'businessid_')
    try:
        rating = int(r.get('rating'))
    except Exception:
        # skip if rating invalid
        continue
    ratings_map[bid].append(rating)

# Function to determine if BusinessAcceptsCreditCards is True

def accepts_credit(attributes):
    if attributes is None:
        return False
    # If it's a dict
    if isinstance(attributes, dict):
        v = attributes.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        s = str(v).lower()
        return 'true' in s
    # If it's a string
    if isinstance(attributes, str):
        s = attributes.lower()
        # check presence of the key and true
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        # sometimes attributes string is "None"
        return False
    return False

# Collect categories counts and list of business ids per category
cat_to_biz = defaultdict(set)
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    attrs = b.get('attributes')
    if accepts_credit(attrs):
        cats = b.get('categories')
        if not cats:
            continue
        # categories may be a single string with comma-separated values
        if isinstance(cats, list):
            cat_list = [str(x).strip() for x in cats if x]
        else:
            # split by comma
            cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
        for c in cat_list:
            cat_to_biz[c].add(bid)

# Find category with largest number of businesses
if not cat_to_biz:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    # compute counts
    counts = [(c, len(bset)) for c, bset in cat_to_biz.items()]
    # sort by count desc then name asc for deterministic
    counts.sort(key=lambda x: (-x[1], x[0]))
    top_cat, top_count = counts[0]

    # collect all ratings for businesses in this category
    all_ratings = []
    for bid in sorted(cat_to_biz[top_cat]):
        all_ratings.extend(ratings_map.get(bid, []))
    if all_ratings:
        avg = sum(all_ratings) / len(all_ratings)
        avg_rounded = round(avg, 2)
    else:
        avg_rounded = None

    result = {"category": top_cat, "business_count": top_count, "average_rating": avg_rounded}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_AvP883aTMuAN0HLKUSywbHjl': ['business', 'checkin'], 'var_call_90pYhkxqqwG6X642xvBZDreX': ['review', 'tip', 'user'], 'var_call_DYOmUKWQbTEskr11JQeVelj7': 'file_storage/call_DYOmUKWQbTEskr11JQeVelj7.json', 'var_call_2m0iQ5foTc1FNVIoZVdOohmI': 'file_storage/call_2m0iQ5foTc1FNVIoZVdOohmI.json'}

exec(code, env_args)
