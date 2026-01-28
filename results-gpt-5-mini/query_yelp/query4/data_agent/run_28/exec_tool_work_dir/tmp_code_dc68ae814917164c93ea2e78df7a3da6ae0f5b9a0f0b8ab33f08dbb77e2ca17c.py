code = """import json
from collections import defaultdict

# Load data from storage-provided file paths
businesses = json.load(open(var_call_ou0kDmsEGophro3skhOhh6QK, 'r'))
reviews = json.load(open(var_call_svDbO7SbTNBU2g0AkksEFtMr, 'r'))

# Helper to determine if a business accepts credit cards
def accepts_credit(attributes):
    if attributes is None:
        return False
    # sometimes attributes is the string "None"
    if isinstance(attributes, str):
        if attributes.lower() == 'none':
            return False
        try:
            # sometimes it's a string representation of a dict? we'll try to parse minimal
            return 'businessacceptscreditcards' in attributes.lower() and "true" in attributes.lower()
        except Exception:
            return False
    if isinstance(attributes, dict):
        # key may exist
        for key in attributes.keys():
            if key.lower() == 'businessacceptscreditcards':
                val = attributes[key]
                if isinstance(val, bool):
                    return val
                if val is None:
                    return False
                return str(val).lower().strip() == 'true'
        return False
    return False

# Build category -> set(business_ref) for businesses that accept credit
cat_to_biz = defaultdict(set)

for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    attrs = b.get('attributes')
    if not accepts_credit(attrs):
        continue
    # get categories; some docs may have 'categories' key
    cats = b.get('categories')
    if not cats:
        # try to infer from 'name' or skip
        continue
    # categories could be a list or a string
    parsed = []
    if isinstance(cats, list):
        parsed = [str(x).strip() for x in cats if x]
    else:
        # string possibly comma-separated
        parsed = [c.strip() for c in str(cats).split(',') if c.strip()]
    if not parsed:
        continue
    # convert businessid_ to businessref_
    bref = bid.replace('businessid_', 'businessref_')
    for c in parsed:
        cat_to_biz[c].add(bref)

# Compute counts and find max
if not cat_to_biz:
    result = {"category": None, "business_count": 0, "average_rating": None, "num_reviews_used": 0}
else:
    counts = {c: len(s) for c, s in cat_to_biz.items()}
    max_count = max(counts.values())
    # get categories with max_count
    top_cats = sorted([c for c, cnt in counts.items() if cnt == max_count])
    top_cat = top_cats[0]
    top_biz_refs = cat_to_biz[top_cat]

    # collect ratings for reviews matching these business refs
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        if bref in top_biz_refs:
            try:
                ratings.append(float(r.get('rating')))
            except Exception:
                pass
    avg = None
    if ratings:
        avg = sum(ratings)/len(ratings)
    result = {"category": top_cat, "business_count": max_count, "average_rating": round(avg, 2) if avg is not None else None, "num_reviews_used": len(ratings)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Tr7v1meRsP00OcMGJDl6aa2F': 'file_storage/call_Tr7v1meRsP00OcMGJDl6aa2F.json', 'var_call_ou0kDmsEGophro3skhOhh6QK': 'file_storage/call_ou0kDmsEGophro3skhOhh6QK.json', 'var_call_svDbO7SbTNBU2g0AkksEFtMr': 'file_storage/call_svDbO7SbTNBU2g0AkksEFtMr.json'}

exec(code, env_args)
