code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_9CQTLa2tPxMrbUPXKsYcua73, 'r') as f:
    businesses = json.load(f)
with open(var_call_ujuxQXIXFWHgYM3XRFcu7bhu, 'r') as f:
    reviews = json.load(f)

biz_df = pd.DataFrame(businesses)
rev_df = pd.DataFrame(reviews)

# Helper to determine if a business accepts credit cards
def accepts_credit(attr):
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() == 'true' or "'true'" in val.lower() or 'u"true"' in val.lower()
        return False
    if isinstance(attr, str):
        # check for substring indicating acceptance
        if 'BusinessAcceptsCreditCards' in attr and 'True' in attr:
            return True
        # sometimes the string could literally be "True"
        return attr.lower() == 'true'
    return False

# Ensure columns exist
if 'attributes' not in biz_df.columns:
    biz_df['attributes'] = None
if 'categories' not in biz_df.columns:
    biz_df['categories'] = None

# Filter businesses that accept credit cards
biz_df['accepts_cc'] = biz_df['attributes'].apply(accepts_credit)
cc_biz = biz_df[biz_df['accepts_cc'] == True].copy()

# Build mapping of category -> set of business_refs
from collections import defaultdict
cat_to_biz = defaultdict(set)

for _, row in cc_biz.iterrows():
    biz_id = row.get('business_id')
    if not isinstance(biz_id, str):
        continue
    # convert to business_ref format
    biz_ref = biz_id.replace('businessid_', 'businessref_')
    cats = row.get('categories')
    if not cats or (isinstance(cats, float) and pd.isna(cats)):
        continue
    # sometimes categories might be a list; handle strings
    if isinstance(cats, list):
        cat_list = [c.strip() for c in cats if isinstance(c, str) and c.strip()]
    else:
        # split by comma
        cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
    for c in cat_list:
        cat_to_biz[c].add(biz_ref)

# If no categories found, return empty result
if not cat_to_biz:
    output = {"category": None, "business_count": 0, "average_rating": None}
else:
    # find category with largest number of businesses
    max_count = -1
    max_cats = []
    for c, s in cat_to_biz.items():
        cnt = len(s)
        if cnt > max_count:
            max_count = cnt
            max_cats = [c]
        elif cnt == max_count:
            max_cats.append(c)
    # choose first category in alphabetical order if tie
    chosen_cat = sorted(max_cats)[0]
    chosen_biz_refs = cat_to_biz[chosen_cat]

    # compute average rating across reviews for these businesses
    if rev_df.empty:
        avg_rating = None
    else:
        # ensure business_ref and rating columns exist
        if 'business_ref' not in rev_df.columns or 'rating' not in rev_df.columns:
            avg_rating = None
        else:
            # filter reviews for chosen businesses
            mask = rev_df['business_ref'].isin(chosen_biz_refs)
            filtered = rev_df[mask].copy()
            if filtered.empty:
                avg_rating = None
            else:
                # convert rating to numeric
                filtered['rating'] = pd.to_numeric(filtered['rating'], errors='coerce')
                avg = float(filtered['rating'].mean())
                avg_rating = round(avg, 2)

    output = {"category": chosen_cat, "business_count": int(max_count), "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_KJh4DBlhRfS7CFVVu8Hpsc9W': ['checkin', 'business'], 'var_call_qeaXw5PFvk6LbmOqVkjK6sii': ['review', 'tip', 'user'], 'var_call_9CQTLa2tPxMrbUPXKsYcua73': 'file_storage/call_9CQTLa2tPxMrbUPXKsYcua73.json', 'var_call_ujuxQXIXFWHgYM3XRFcu7bhu': 'file_storage/call_ujuxQXIXFWHgYM3XRFcu7bhu.json'}

exec(code, env_args)
