code = """import json
import pandas as pd
import re

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

rows = []
keyword_list = [
    'offers a diverse range of services and products in',
    'offers a range of services in the fields of',
    'offers a wide range of services including',
    'offers a range of services including',
    'offers a range of services and products in',
    'in the category of',
    'in the category of',
    'including',
    'offers',
    'provides',
    'provides services in',
    'offers a range of services in',
    'offers a wide range of services',
]

for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    if not desc:
        rows.append({'business_id': bid, 'categories': []})
        continue
    # split into sentences
    sentences = [s.strip() for s in re.split(r'[\.\!\?]+', desc) if s.strip()]
    # pick sentence with most commas as candidate
    if sentences:
        cand = max(sentences, key=lambda s: s.count(','))
    else:
        cand = desc
    cand_lower = cand.lower()
    start_idx = None
    matched_kw = None
    for kw in keyword_list:
        idx = cand_lower.find(kw)
        if idx != -1:
            start_idx = idx + len(kw)
            matched_kw = kw
            break
    if start_idx is not None:
        seg = cand[start_idx:]
    else:
        # if no keyword, try to remove leading 'Located at ...' patterns
        seg = re.sub(r'located at [^,\.]+[,\.]?', '', cand, flags=re.IGNORECASE).strip()
    if not seg:
        seg = cand
    # split segment into items
    parts = re.split(r',|/|;|\sand\s|\s&\s', seg)
    cats = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        # remove parenthetical content
        p = re.sub(r"\(.*?\)", '', p).strip()
        # remove leading phrases like 'this establishment' or 'this business'
        p = re.sub(r'^(this establishment|this business|this facility|the establishment|the business)\s+','', p, flags=re.IGNORECASE).strip()
        # remove trailing phrases like 'to meet all your travel and transportation needs'
        p = re.split(r' to\s', p, flags=re.IGNORECASE)[0].strip()
        # remove leading articles
        p = re.sub(r'^(the |a |an )', '', p, flags=re.IGNORECASE).strip()
        # strip quotes
        p = re.sub(r'^[\'\"]+|[\'\"]+$', '', p).strip()
        # filter out if looks like address (contains digits and 'st' or 'rd' etc) or too long
        if len(p) > 80:
            continue
        if re.search(r'\d', p) and len(p) < 40:
            # likely still an address, skip
            continue
        # skip generic verbs
        if re.search(r'\b(offe?rs|provides|located)\b', p, flags=re.IGNORECASE):
            continue
        if p:
            cats.append(p)
    # dedupe while preserving order
    seen = set()
    cats_unique = []
    for c in cats:
        if c not in seen:
            seen.add(c)
            cats_unique.append(c)
    rows.append({'business_id': bid, 'categories': cats_unique})

# Build dataframe
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
        cat_counts = cat_counts.rename(columns={'categories':'category','business_id':'business_count'})
        cat_counts = cat_counts.sort_values(by=['business_count','category'], ascending=[False,True])
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
            df_r['business_id'] = df_r['business_ref'].apply(lambda x: x.replace('businessref_','businessid_') if isinstance(x,str) else None)
        else:
            df_r['business_id'] = None
        df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
        if df_r_cat.empty:
            avg = None
        else:
            avg = round(float(df_r_cat['rating'].mean()),2)
        result = {'category': top_category, 'business_count': top_count, 'average_rating': (None if avg is None else avg)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json'}

exec(code, env_args)
