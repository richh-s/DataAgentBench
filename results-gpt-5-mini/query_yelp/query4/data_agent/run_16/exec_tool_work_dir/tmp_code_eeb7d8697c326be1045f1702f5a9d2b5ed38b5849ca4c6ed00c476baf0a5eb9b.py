code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_kUMHHQgNcnp9xcqV7AbjenPP, 'r') as f:
    businesses = json.load(f)
with open(var_call_su679fGqLS4nfmXoMdtNWGxu, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize types
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

# Determine if business accepts credit cards
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    # attr might be a dict or a string representation of dict
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
    else:
        # try to parse if it's a string representation like "{'BusinessAcceptsCreditCards': 'True', ...}"
        s = str(attr)
        m = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*'?(True|False|true|false|None)'?", s)
        if m:
            val = m.group(1)
        else:
            # also try simple key look
            if 'BusinessAcceptsCreditCards' in s:
                # extract after it
                m2 = re.search(r"BusinessAcceptsCreditCards\W*(True|False|true|false)")
                val = m2.group(1) if m2 else None
            else:
                val = None
    if val is None:
        return False
    return str(val).lower() == 'true'

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# Extract categories from description heuristically
patterns = [
    r'in the category of (.*)',
    r'in the fields of (.*)',
    r'in the category (.*)',
    r'including (.*)',
    r'offers a range of services in (.*)',
    r'offers a wide range of services, including (.*)',
    r'offers a diverse range of services and products in the fields of (.*)',
    r'providing a range of services in (.*)',
    r'offers a delightful array of dishes in the category of (.*)',
    r'this establishment offers a variety of services including (.*)',
    r'this business offers a diverse range of services and products in the fields of (.*)',
    r'offers a wide range of services including (.*)'
]

def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    s = s.replace('\n', ' ')
    # Only consider the part after the last occurrence of 'offers' or 'offers a' to avoid location parts
    # But we'll use patterns first
    for p in patterns:
        m = re.search(p, s, flags=re.IGNORECASE)
        if m:
            tail = m.group(1)
            # trim after first period
            tail = tail.split('.')[0]
            # remove trailing clauses like 'to meet all your ...'
            tail = re.split(r'to meet|that includes|for all your|for all', tail, flags=re.IGNORECASE)[0]
            # Now split by commas and ' and '
            parts = re.split(r',| and | & |;|\band\b', tail)
            cats = [re.sub(r"[^\w\s&\-/']", '', p).strip() for p in parts]
            cats = [c for c in cats if c]
            return cats
    # fallback: take phrases after last comma (assume categories near end)
    parts = s.split(',')
    if len(parts) > 2:
        tail = ','.join(parts[-3:])
        tail = tail.split('.')[0]
        parts2 = re.split(r',| and | & ', tail)
        cats = [re.sub(r"[^\w\s&\-/']", '', p).strip() for p in parts2]
        cats = [c for c in cats if len(c)>2]
        return cats
    return []

# Apply to dataframe
df_b['categories'] = df_b['description'].apply(extract_cats)

# Filter businesses that accept credit cards and have at least one category
df_cc = df_b[(df_b['accepts_cc']) & df_b['categories'].map(lambda x: len(x)>0)].copy()

# Build mapping category -> set of business_ids
from collections import defaultdict
cat_to_biz = defaultdict(set)
for _, row in df_cc.iterrows():
    bid = row.get('business_id')
    cats = row.get('categories') or []
    for c in cats:
        cat_to_biz[c].add(bid)

# Prepare reviews dataframe
if df_r.empty:
    # no reviews
    df_r = pd.DataFrame(columns=['business_ref','rating'])
else:
    # ensure rating numeric
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# For each category compute business count and average rating across all reviews for those businesses
results = []
for cat, biz_set in cat_to_biz.items():
    # convert businessid_X to businessref_X
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_set]
    # filter reviews
    mask = df_r['business_ref'].isin(biz_refs)
    ratings = df_r[mask]['rating'].dropna().astype(float)
    avg_rating = ratings.mean() if not ratings.empty else None
    results.append({'category': cat, 'business_count': len(biz_set), 'average_rating': avg_rating})

# Find category with largest number of businesses
if not results:
    out = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # sort by business_count desc, then by average_rating desc (None -> -inf)
    def sort_key(x):
        ar = x['average_rating'] if x['average_rating'] is not None else -1
        return (x['business_count'], ar)
    results_sorted = sorted(results, key=sort_key, reverse=True)
    top = results_sorted[0]
    # Round average_rating to 2 decimals if not None
    if top['average_rating'] is None:
        avg = None
    else:
        avg = round(float(top['average_rating']), 2)
    out = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': avg}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_kUMHHQgNcnp9xcqV7AbjenPP': 'file_storage/call_kUMHHQgNcnp9xcqV7AbjenPP.json', 'var_call_su679fGqLS4nfmXoMdtNWGxu': 'file_storage/call_su679fGqLS4nfmXoMdtNWGxu.json'}

exec(code, env_args)
