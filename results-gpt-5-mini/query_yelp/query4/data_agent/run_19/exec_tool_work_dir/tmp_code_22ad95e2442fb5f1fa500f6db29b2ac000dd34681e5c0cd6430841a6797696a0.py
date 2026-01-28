code = """import json, os
from collections import defaultdict

# Load business data
bvar = var_call_q48RY1T7FvRnav9ZALijmUUy
if isinstance(bvar, str) and os.path.exists(bvar):
    with open(bvar, 'r', encoding='utf-8') as f:
        businesses = json.load(f)
else:
    businesses = bvar

# Load reviews data
rvar = var_call_dzON48RfddMU1hmCaWPTf0kE
if isinstance(rvar, str) and os.path.exists(rvar):
    with open(rvar, 'r', encoding='utf-8') as f:
        reviews = json.load(f)
else:
    reviews = rvar

# Helper to extract numeric id
def norm_id(s):
    if s is None:
        return None
    if '_' in s:
        return s.split('_',1)[1]
    return s

# Build set of businesses that accept credit cards and map to categories
cat_to_biz = defaultdict(set)
accepting_businesses = set()
biz_id_to_name = {}
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    biz_num = norm_id(bid)
    biz_id_to_name[biz_num] = b.get('name')
    attrs = b.get('attributes')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is True or (isinstance(val, str) and val.lower().strip()=='true'):
            accepts = True
    # handle string 'None' or other forms
    # Some entries may have attributes as string 'None' or other; already covered
    if accepts:
        accepting_businesses.add(biz_num)
        cats = b.get('categories')
        if cats is None:
            continue
        # categories may be list or comma-separated string
        if isinstance(cats, list):
            cat_list = cats
        else:
            # sometimes categories have unicode prefixes like u'...'
            try:
                cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
            except:
                cat_list = []
        for c in cat_list:
            cat_to_biz[c].add(biz_num)

# If no categories found (empty), try to infer from names? but proceed
if not cat_to_biz:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # find category with largest number of businesses
    max_cat = None
    max_count = 0
    for c,s in cat_to_biz.items():
        if len(s) > max_count:
            max_count = len(s)
            max_cat = c

    # Compute average rating for businesses in that category
    target_biz_nums = set(cat_to_biz[max_cat])
    total = 0.0
    count = 0
    for r in reviews:
        bref = r.get('business_ref')
        if not bref:
            continue
        bref_num = norm_id(bref)
        if bref_num in target_biz_nums:
            # rating may be string
            try:
                rating = float(r.get('rating'))
            except:
                continue
            total += rating
            count += 1
    avg = None
    if count>0:
        avg = total/count
    result = {'category': max_cat, 'business_count': max_count, 'average_rating': round(avg, 3) if avg is not None else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_kO5syuL1LsUQnhXBy0rFpI3f': ['business', 'checkin'], 'var_call_jXQ5r6YvxcGSGqRI5ZzOM04h': ['review', 'tip', 'user'], 'var_call_q48RY1T7FvRnav9ZALijmUUy': 'file_storage/call_q48RY1T7FvRnav9ZALijmUUy.json', 'var_call_dzON48RfddMU1hmCaWPTf0kE': 'file_storage/call_dzON48RfddMU1hmCaWPTf0kE.json'}

exec(code, env_args)
