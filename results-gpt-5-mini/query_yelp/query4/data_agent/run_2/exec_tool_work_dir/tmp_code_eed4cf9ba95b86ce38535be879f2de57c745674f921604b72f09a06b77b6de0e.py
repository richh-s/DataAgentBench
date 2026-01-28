code = """import json
from collections import defaultdict

# Load the business query result JSON file
p = var_call_KABRrtqNUlTcXdQMb8MB38mC
with open(p, 'r') as f:
    docs = json.load(f)

# Build category -> set(business_id) for businesses that accept credit cards
cat_to_biz = defaultdict(set)
accepting_biz = set()
for d in docs:
    biz_id = d.get('business_id')
    attrs = d.get('attributes')
    if not attrs or not isinstance(attrs, dict):
        continue
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        continue
    # Normalize value to boolean
    sval = str(val).lower()
    if 'true' in sval:
        accepting_biz.add(biz_id)
        cats = d.get('categories')
        if not cats:
            continue
        # categories may be string or list
        if isinstance(cats, list):
            parts = cats
        else:
            parts = [c.strip() for c in str(cats).split(',') if c.strip()]
        for c in parts:
            cat_to_biz[c].add(biz_id)

# Compute counts per category but only counting businesses that accept credit cards
cat_counts = {c: len(bset) for c, bset in cat_to_biz.items()}
if not cat_counts:
    result = {"top_category": None, "top_count": 0, "business_ids": [], "business_refs": []}
else:
    # find top category (max count, tie break by alphabetical)
    top_category = sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))[0][0]
    top_count = cat_counts[top_category]
    biz_ids = sorted(list(cat_to_biz[top_category]))
    biz_refs = [bid.replace('businessid_', 'businessref_') for bid in biz_ids]
    result = {"top_category": top_category, "top_count": top_count, "business_ids": biz_ids, "business_refs": biz_refs}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7ZgO1JmiFzKIX0XDrSGqVpq3': ['checkin', 'business'], 'var_call_tn6yro8Bzk11NeQZGFUQjmNo': ['review', 'tip', 'user'], 'var_call_KABRrtqNUlTcXdQMb8MB38mC': 'file_storage/call_KABRrtqNUlTcXdQMb8MB38mC.json'}

exec(code, env_args)
