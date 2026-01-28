code = """import json
import pandas as pd
import re

# Load data files from storage
with open(var_call_1uii8pNZd1IBGrZIeeZbTb8Z, 'r') as f:
    businesses = json.load(f)
with open(var_call_4GZQ1vFcyPhN3EeL2n8BFb59, 'r') as f:
    reviews = json.load(f)

# Helper to detect credit card acceptance
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
    else:
        # sometimes attributes might be string representation of dict
        # quick check for substring
        s = str(attr)
        if 'BusinessAcceptsCreditCards' in s:
            # try to find True/False after key
            m = re.search(r"BusinessAcceptsCreditCards\s*[:=]?[\"']?(True|False|true|false|u'no'|u'yes')", s)
            if m:
                v = m.group(1)
                return str(v).lower() == 'true'
            # fallback: look for BusinessAcceptsCreditCards followed by True
            return 'BusinessAcceptsCreditCards"True"' in s or "BusinessAcceptsCreditCards': 'True'" in s
        return False
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    return str(val).lower() == 'true'

# Helper to extract categories from description

def extract_categories(desc):
    if not desc:
        return []
    desc = desc.replace('\n', ' ')
    # Try patterns
    patterns = [r"in the category of (.+?)(?:\.|$)", r"in (.+?)(?:\.|$)", r"including (.+?)(?:\.|$)", r"offers a range of services in (.+?)(?:\.|$)", r"offers a diverse range of services (?:and )?in (.+?)(?:\.|$)"]
    match = None
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            candidate = m.group(1).strip()
            # if candidate is too short, continue
            if len(candidate) > 2:
                match = candidate
                break
    if not match:
        return []
    s = match
    # Remove trailing phrases like 'to meet all your travel and transportation needs' by cutting after first location-like phrase? Hard.
    # Truncate at 'to meet' or 'to ' if present
    s = re.split(r" to meet | to ", s, maxsplit=1)[0]
    # Replace ' and ' between items with comma, but keep ' & '
    # Only replace ' and ' if there is at least one comma in string (likely list)
    if ',' in s:
        s = re.sub(r"\s+and\s+", ", ", s)
    # Now split on commas
    parts = [p.strip().strip("'\" ") for p in s.split(',') if p.strip()]
    # Further split parts that contain '/' or ' & '
    final = []
    for p in parts:
        # keep ' & ' as part of category
        # but split on '/'
        for sub in p.split('/'):
            sub = sub.strip()
            if sub:
                final.append(sub)
    # Normalize
    final = [re.sub(r"\s+&\s+", " & ", c) for c in final]
    return final

# Build DataFrame for businesses
biz_rows = []
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    accepts = accepts_cc(attrs)
    desc = b.get('description') or ''
    cats = b.get('categories')
    # if categories field exists and is non-empty and is list or string, use it
    extracted = []
    if cats:
        if isinstance(cats, list):
            extracted = cats
        elif isinstance(cats, str):
            # split by comma
            extracted = [c.strip() for c in cats.split(',') if c.strip()]
    if not extracted:
        extracted = extract_categories(desc)
    biz_rows.append({'business_id': bid, 'accepts_cc': accepts, 'categories': extracted})

biz_df = pd.DataFrame(biz_rows)
# explode categories
biz_df = biz_df.explode('categories')
biz_df['categories'] = biz_df['categories'].fillna('').astype(str).str.strip()
# Filter businesses that accept credit cards and have a non-empty category
cc_biz = biz_df[(biz_df['accepts_cc']==True) & (biz_df['categories']!='')].copy()
# Normalize category casing
cc_biz['category_norm'] = cc_biz['categories'].str.strip()

# Prepare reviews dataframe
rev_df = pd.DataFrame(reviews)
# convert rating to numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
# Map business_id to business_ref by replacing prefix
cc_biz['business_ref'] = cc_biz['business_id'].str.replace('businessid_', 'businessref_')

# For each category, count distinct businesses
cat_counts = cc_biz.groupby('category_norm')['business_ref'].nunique().reset_index()
cat_counts = cat_counts.rename(columns={'business_ref': 'business_count'})

# Merge reviews on business_ref to compute avg rating per category (only reviews for businesses that accept cc)
# First join cc_biz unique mapping of business_ref -> categories
biz_cat = cc_biz[['business_ref','category_norm']].drop_duplicates()
rev_join = rev_df.merge(biz_cat, on='business_ref', how='inner')

# Compute average rating per category
cat_avg = rev_join.groupby('category_norm')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Combine counts and averages
summary = cat_counts.merge(cat_avg, on='category_norm', how='left')
# Fill NaN avg_rating with None
summary['avg_rating'] = summary['avg_rating'].round(2)

# Find category with max business_count
if summary.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    max_count = summary['business_count'].max()
    top = summary[summary['business_count']==max_count].sort_values('avg_rating', ascending=False).iloc[0]
    result = {'category': top['category_norm'], 'business_count': int(top['business_count']), 'average_rating': (None if pd.isna(top['avg_rating']) else float(top['avg_rating']))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ryydk2OydyICGOkK0fdQmodU': ['business', 'checkin'], 'var_call_s0HAPJstiC6duixg4yD27A9v': ['review', 'tip', 'user'], 'var_call_1uii8pNZd1IBGrZIeeZbTb8Z': 'file_storage/call_1uii8pNZd1IBGrZIeeZbTb8Z.json', 'var_call_4GZQ1vFcyPhN3EeL2n8BFb59': 'file_storage/call_4GZQ1vFcyPhN3EeL2n8BFb59.json'}

exec(code, env_args)
