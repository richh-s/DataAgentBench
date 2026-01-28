code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_44Cn1NqLrUUZjlPvYwfp0qYg, 'r') as f:
    businesses = json.load(f)
with open(var_call_0S2DHKv0gJ86NbwZcKhWpGcp, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure necessary columns
if 'business_id' not in df_b.columns:
    df_b['business_id'] = df_b.get('business_id')

# Helper to determine if business accepts credit cards
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        val_str = str(val)
        return 'true' in val_str.lower()
    # sometimes stored as string representation of dict
    s = str(attr).lower()
    return 'businessacceptscreditcards' in s and 'true' in s

# Extract categories heuristically
# If 'categories' present and non-null, try to parse it; otherwise extract from description

def extract_categories(rec):
    cats = []
    if 'categories' in rec and rec['categories']:
        c = rec['categories']
        if isinstance(c, list):
            cats = [x.strip() for x in c if x]
        else:
            # string possibly comma-separated
            cats = [x.strip() for x in str(c).split(',') if x.strip()]
        if cats:
            return cats
    # fallback to description
    desc = rec.get('description') or ''
    if not desc:
        return []
    # common patterns to find categories list
    patterns = [
        r'offers a range of services in (.+?)\.',
        r'offers a wide range of services, including (.+?)\.',
        r'offers a diverse range of options ranging from (.+?)\.',
        r'offers a diverse selection of (.+?)\.',
        r'offers a range of services and products in the fields of (.+?)\.',
        r'offers a variety of services including (.+?)\.',
        r'offers a range of services, including (.+?)\.',
        r'offers a range of services in the categories of (.+?)\.',
        r'offers services in (.+?)\.',
        r'making it a must-visit for anyone seeking (.+?)\.',
        r'this establishment offers a delightful array of options ranging from (.+?)\.',
    ]
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            chunk = m.group(1)
            # replace ' and ' with comma to split
            chunk = chunk.replace(' and ', ', ')
            parts = [p.strip() for p in re.split(r',|/|;|\band\b', chunk) if p.strip()]
            # Clean trailing words like 'Food' etc
            cleaned = []
            for p in parts:
                # remove leading words like 'the category of'
                p = re.sub(r"^(including|the|a|an)\s+", '', p, flags=re.IGNORECASE)
                # remove trailing phrases like 'for all your home and decorative needs' after comma
                p = re.sub(r"for .*", '', p, flags=re.IGNORECASE)
                p = p.strip().strip('"').strip('.')
                if p:
                    cleaned.append(p)
            if cleaned:
                return cleaned
    # as last resort, try to find capitalized sequences separated by commas in desc
    parts = [p.strip() for p in re.split(r',|;|/| and ', desc) if p.strip()]
    # pick parts that contain capitalized words (heuristic)
    candidates = []
    for p in parts:
        # if contains uppercase letters and words (heuristic)
        words = p.split()
        cap_words = sum(1 for w in words if w and w[0].isupper())
        if cap_words >= 1 and len(p) < 60:
            candidates.append(p)
    return candidates

# Apply
df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)
# extract categories list
cats_list = []
for rec in businesses:
    bids = rec.get('business_id')
    cats = extract_categories(rec)
    cats_list.append({'business_id': bids, 'categories': cats})

df_cats = pd.DataFrame(cats_list)
# Merge into df_b
df_b = df_b.merge(df_cats, on='business_id', how='left')

# Explode categories
df_b['categories'] = df_b['categories'].apply(lambda x: x if isinstance(x, list) else ([] if pd.isna(x) else [x]))
df_exp = df_b.explode('categories')
# Clean category strings
df_exp['category'] = df_exp['categories'].apply(lambda x: x.strip() if isinstance(x, str) else x)

# Filter businesses that accept credit cards and have a non-null category
df_accept = df_exp[(df_exp['accepts_cc']==True) & (df_exp['category'].notnull())]

# Count unique businesses per category
group = df_accept.groupby('category')['business_id'].nunique().reset_index()
if group.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    group = group.sort_values('business_id', ascending=False)
    top = group.iloc[0]
    top_category = top['category']
    top_count = int(top['business_id'])

    # Get businesses in that category
    biz_ids = df_accept[df_accept['category']==top_category]['business_id'].unique().tolist()
    # convert to business_ref format
    biz_refs = set([b.replace('businessid_', 'businessref_') for b in biz_ids])

    # filter reviews for these business refs
    if df_r.empty:
        avg_rating = None
    else:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        df_cat_reviews = df_r[df_r['business_ref'].isin(biz_refs)]
        if df_cat_reviews.empty:
            avg_rating = None
        else:
            avg_rating = float(df_cat_reviews['rating'].mean())

    result = {'category': top_category, 'business_count': top_count, 'average_rating': round(avg_rating, 2) if avg_rating is not None else None}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_n1vhqBOpB8tFjSmtWPHCMyoT': ['business', 'checkin'], 'var_call_oJYiFtBVgN521I395eomJvvm': ['review', 'tip', 'user'], 'var_call_VPHgAKEYoMWD9yxajGFNq4rQ': 'file_storage/call_VPHgAKEYoMWD9yxajGFNq4rQ.json', 'var_call_44Cn1NqLrUUZjlPvYwfp0qYg': 'file_storage/call_44Cn1NqLrUUZjlPvYwfp0qYg.json', 'var_call_0S2DHKv0gJ86NbwZcKhWpGcp': 'file_storage/call_0S2DHKv0gJ86NbwZcKhWpGcp.json'}

exec(code, env_args)
