code = """import json
import pandas as pd
import re

# Load files
businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g
with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

rows = []
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    if not desc:
        rows.append({'business_id': bid, 'categories': []})
        continue
    # split into sentences and take last
    sents = re.split(r'[\.\!\?]+', desc)
    sents = [s.strip() for s in sents if s.strip()]
    last = sents[-1] if sents else desc
    # split by commas
    parts = [p.strip() for p in last.split(',') if p.strip()]
    cats = []
    for p in parts:
        low = p.lower()
        # skip if looks like address or contains digits
        if re.search(r'\d', p):
            continue
        if low.startswith('located') or low.startswith('located at'):
            continue
        if any(x in low for x in ['ste ', 'suite', 'blvd', 'road', 'rd', 'ave', 'street', 'lane', 'in ']):
            # 'in ' might appear in category names but many addresses have 'in', so skip only if contains ' in ' and has short length? We'll be conservative and skip parts that contain ' in ' and also contain lowercase words like 'the' or 'at'
            if ' in ' in low and any(w in low for w in ['the', 'at', 'offers', 'located']):
                continue
        # remove leading generic phrases
        p = re.sub(r'^(this establishment|this business|this facility|offers a range of services in|offers a wide range of services in)\s+', '', p, flags=re.IGNORECASE)
        p = p.strip(" '\"")
        if not p:
            continue
        if len(p) > 80:
            continue
        cats.append(p)
    # dedupe preserve order
    seen = set()
    cats_u = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            cats_u.append(c)
    rows.append({'business_id': bid, 'categories': cats_u})

# Build DataFrame
df = pd.DataFrame(rows)
if df.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_ex = df.explode('categories')
    df_ex = df_ex[df_ex['categories'].notna()]
    if df_ex.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        df_ex['categories'] = df_ex['categories'].str.strip()
        cat_counts = df_ex.groupby('categories')['business_id'].nunique().reset_index()
        cat_counts = cat_counts.rename(columns={'categories': 'category', 'business_id': 'business_count'})
        cat_counts = cat_counts.sort_values(by=['business_count', 'category'], ascending=[False, True])
        top = cat_counts.iloc[0]
        top_category = top['category']
        top_count = int(top['business_count'])
        biz_ids = set(df_ex[df_ex['categories'] == top_category]['business_id'].unique())

        # process reviews
        df_r = pd.DataFrame(reviews)
        if 'rating' in df_r.columns:
            df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        else:
            df_r['rating'] = pd.Series(dtype='float')
        if 'business_ref' in df_r.columns:
            df_r['business_id'] = df_r['business_ref'].apply(lambda x: x.replace('businessref_', 'businessid_') if isinstance(x, str) else None)
        else:
            df_r['business_id'] = None
        df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
        if df_r_cat.empty:
            avg = None
        else:
            avg = round(float(df_r_cat['rating'].mean()), 2)
        result = {'category': top_category, 'business_count': top_count, 'average_rating': (None if avg is None else avg)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json'}

exec(code, env_args)
