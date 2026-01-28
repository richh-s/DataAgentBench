code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_S2zuCHmhggl6c0g3JVnsCV3S, 'r') as f:
    businesses = json.load(f)
with open(var_call_yro9FRCCc3lUv55SCI5jPHkG, 'r') as f:
    reviews = json.load(f)

# Normalize businesses
rows = []
for b in businesses:
    bid = b.get('business_id')
    attr = b.get('attributes')
    cats = b.get('categories') if 'categories' in b else None
    accepts = False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if isinstance(v, str):
            if 'true' in v.lower():
                accepts = True
        elif isinstance(v, bool):
            accepts = bool(v)
    elif isinstance(attr, str):
        low = attr.lower()
        if 'businessacceptscreditcards' in low and 'true' in low:
            accepts = True
    # parse categories into list
    cats_list = []
    if cats and isinstance(cats, str):
        # clean weird unicode markers and quotes
        s = cats
        s = s.replace("u'", "'")
        s = s.replace('u"', '"')
        # remove surrounding brackets if present
        if s.startswith('[') and s.endswith(']'):
            try:
                parsed = json.loads(s.replace("'", '"'))
                if isinstance(parsed, list):
                    cats_list = [c.strip() for c in parsed]
                else:
                    cats_list = [s.strip()]
            except Exception:
                cats_list = [c.strip().strip("'\"") for c in s.split(',')]
        else:
            cats_list = [c.strip().strip("'\"") for c in s.split(',') if c.strip()]
    elif isinstance(cats, list):
        cats_list = cats
    rows.append({'business_id': bid, 'business_ref': bid.replace('businessid_','businessref_') if isinstance(bid,str) else None, 'accepts_credit': accepts, 'categories': cats_list})

biz_df = pd.DataFrame(rows)

# Filter businesses that accept credit
cc_biz = biz_df[biz_df['accepts_credit'] == True].copy()

# Build mapping category -> set of business_refs
from collections import defaultdict
cat_to_biz = defaultdict(set)
for _, r in cc_biz.iterrows():
    refs = r['business_ref']
    cats = r['categories']
    if not cats:
        continue
    for c in cats:
        if c and isinstance(c, str):
            cat_to_biz[c].add(refs)

# Load reviews into DataFrame
rev_df = pd.DataFrame(reviews)
if not rev_df.empty:
    # convert rating to numeric
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
else:
    rev_df['rating'] = pd.Series(dtype=float)

# For each category compute business count and average rating across all reviews of those businesses
results = []
for c, bizset in cat_to_biz.items():
    count = len(bizset)
    if count == 0:
        continue
    # filter reviews where business_ref in bizset
    subset = rev_df[rev_df['business_ref'].isin(bizset)]
    if not subset.empty:
        avg_rating = float(subset['rating'].mean())
    else:
        avg_rating = None
    results.append({'category': c, 'business_count': count, 'average_rating': avg_rating})

# Find category with largest business_count
if results:
    results_sorted = sorted(results, key=lambda x: (x['business_count'], x['category']), reverse=True)
    best = results_sorted[0]
else:
    best = {'category': None, 'business_count': 0, 'average_rating': None}

# Prepare output
out = {
    'category': best['category'],
    'business_count': best['business_count'],
    'average_rating': round(best['average_rating'], 2) if best['average_rating'] is not None else None
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d7w2bomFdJCav34AlVZstfqh': ['business', 'checkin'], 'var_call_eZ7MDOj0Zdn0YwI5SRy8qChp': ['review', 'tip', 'user'], 'var_call_S2zuCHmhggl6c0g3JVnsCV3S': 'file_storage/call_S2zuCHmhggl6c0g3JVnsCV3S.json', 'var_call_yro9FRCCc3lUv55SCI5jPHkG': 'file_storage/call_yro9FRCCc3lUv55SCI5jPHkG.json'}

exec(code, env_args)
