code = """import json
import pandas as pd

businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

rows = []
keywords = [" in the category of ", " offers a range of services in ", " offers a diverse range of services and products in ", " offers a range of services in ", " offers a range of services in the fields of ", " offers a range of services and products in ", " offers ", " including ", " provides ", " provides services in ", " in "]

for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    desc = desc.strip()
    # Take last sentence for relevance
    sentences = [s.strip() for s in desc.split('.') if s.strip()]
    last_sentence = sentences[-1] if sentences else desc
    segment = None
    lower = last_sentence.lower()
    for kw in keywords:
        idx = lower.find(kw.strip())
        if idx != -1:
            segment = last_sentence[idx + len(kw.strip()):]
            break
    if segment is None:
        # fallback to whole description
        segment = last_sentence
    # split into potential categories
    parts = []
    # split by comma first
    for part in segment.split(','):
        # further split by ' & ' and ' and '
        sub = part.split(' & ')
        for s in sub:
            for s2 in s.split(' and '):
                parts.append(s2.strip())
    cats = []
    for p in parts:
        if not p:
            continue
        lowp = p.lower()
        # discard if looks like address or contains 'located' or 'offers' or 'in ' with numbers
        if any(x in lowp for x in ['located at', 'located', 'offers', 'to meet', 'address', 'ste ', 'in ']) and len(p) > 40:
            continue
        # cut off trailing words like 'to meet all your travel and transportation needs'
        if ' to ' in lowp:
            p = p[:lowp.find(' to ')].strip()
        # remove leading 'this', 'the', 'a'
        if p.lower().startswith(('this ', 'the ', 'a ')):
            p = p.split(' ', 1)[1]
        # remove parentheses content
        import re
        p = re.sub(r"\(.*?\)", "", p).strip()
        # strip quotes
        p = p.strip(' "\'')
        if p:
            cats.append(p)
    # dedupe cats
    cats = [c for i, c in enumerate(cats) if c and c not in cats[:i]]
    rows.append({'business_id': bid, 'categories': cats})

# Build df
df = pd.DataFrame(rows)
if df.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    df_ex = df.explode('categories')
    df_ex = df_ex[df_ex['categories'].notna()]
    df_ex['categories'] = df_ex['categories'].str.strip()
    if df_ex.empty:
        result = {"category": None, "business_count": 0, "average_rating": None}
    else:
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
        def ref2id(r):
            if not isinstance(r, str):
                return None
            return r.replace('businessref_', 'businessid_')
        df_r['business_id'] = df_r['business_ref'].apply(ref2id)
        df_r_cat = df_r[df_r['business_id'].isin(biz_ids)]
        if df_r_cat.empty:
            avg = None
        else:
            avg = round(float(df_r_cat['rating'].mean()), 2)
        result = {"category": top_category, "business_count": top_count, "average_rating": (None if avg is None else avg)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json', 'var_call_YjJC0VopQuMgq5f2rYcJ7a7n': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_5lJRX3ne1c6ql1kvUOPQTGXF': [], 'var_call_A9JencJUo1qHNPTfBWZ42ph7': 'file_storage/call_A9JencJUo1qHNPTfBWZ42ph7.json'}

exec(code, env_args)
