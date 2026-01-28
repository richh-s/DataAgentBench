code = """import json
import pandas as pd

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

keywords = [
    'offers a diverse range of services and products in',
    'offers a range of services in the fields of',
    'offers a wide range of services including',
    'offers a range of services including',
    'offers a range of services and products in',
    'in the category of',
    'offers a range of services in',
    'offers a wide range of services',
    'this facility offers',
    'this establishment offers',
    'offers a range of services',
    'offers a range',
    'offers',
    'including',
    'provides',
    'in'
]

rows = []
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    if not desc:
        rows.append({'business_id': bid, 'categories': []})
        continue
    desc_lower = desc.lower()
    best_pos = -1
    best_kw = None
    for kw in keywords:
        pos = desc_lower.find(kw)
        if pos > best_pos:
            best_pos = pos
            best_kw = kw
    if best_pos != -1:
        start = best_pos + len(best_kw)
        seg = desc[start:]
    else:
        seg = desc
    # take only up to first period
    if '.' in seg:
        seg = seg.split('.', 1)[0]
    parts = [p.strip() for p in seg.split(',') if p.strip()]
    cats = []
    for part in parts:
        subparts = []
        if ' & ' in part:
            subparts = [s.strip() for s in part.split(' & ') if s.strip()]
        else:
            subparts = [s.strip() for s in part.split(' and ') if s.strip()]
        for p in subparts:
            if not p:
                continue
            pl = p.lower()
            if 'located' in pl:
                continue
            if any(ch.isdigit() for ch in p):
                continue
            if len(p) > 80:
                continue
            # remove leading articles
            if p.lower().startswith('the '):
                p = p[4:]
            if p.lower().startswith('a '):
                p = p[2:]
            p = p.strip(" '\"")
            if p:
                cats.append(p)
    # dedupe while preserving order
    seen = set()
    cats_u = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            cats_u.append(c)
    rows.append({'business_id': bid, 'categories': cats_u})

# create dataframe
df = pd.DataFrame(rows)
if df.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_ex = df.explode('categories')
    if 'categories' not in df_ex.columns:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        df_ex = df_ex[df_ex['categories'].notna()]
        if df_ex.empty:
            result = {'category': None, 'business_count': 0, 'average_rating': None}
        else:
            df_ex['categories'] = df_ex['categories'].str.strip()
            cat_counts = df_ex.groupby('categories')['business_id'].nunique().reset_index()
            cat_counts = cat_counts.rename(columns={'categories':'category','business_id':'business_count'})
            cat_counts = cat_counts.sort_values(by=['business_count','category'], ascending=[False, True])
            top = cat_counts.iloc[0]
            top_category = top['category']
            top_count = int(top['business_count'])
            biz_ids = set(df_ex[df_ex['categories']==top_category]['business_id'].unique())

            # process reviews
            df_r = pd.DataFrame(reviews)
            if 'rating' in df_r.columns:
                df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
            else:
                df_r['rating'] = pd.Series(dtype='float')
            if 'business_ref' in df_r.columns:
                df_r['business_id'] = df_r['business_ref'].apply(lambda x: x.replace('businessref_','businessid_') if isinstance(x, str) else None)
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
