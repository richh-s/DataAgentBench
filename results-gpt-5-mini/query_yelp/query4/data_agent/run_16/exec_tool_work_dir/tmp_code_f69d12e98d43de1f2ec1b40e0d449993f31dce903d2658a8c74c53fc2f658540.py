code = """import json
import pandas as pd

# Load data
with open(var_call_kUMHHQgNcnp9xcqV7AbjenPP, 'r') as f:
    businesses = json.load(f)
with open(var_call_su679fGqLS4nfmXoMdtNWGxu, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Helper to detect credit card acceptance
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        return str(val).lower() == 'true'
    s = str(attr).lower()
    return ('businessacceptscreditcards' in s) and ('true' in s)

if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# Simple category extraction from description: take words/phrases after keywords
def extract_cats(desc):
    if not isinstance(desc, str):
        return []
    s = desc
    # Find the position of keywords
    keywords = ['offers a range of services in', 'offers a wide range of services, including',
                'offers a diverse range of services and products in the fields of', 'providing a range of services in',
                'in the category of', 'in the fields of', "including", 'including a range of services such as']
    low = s.lower()
    pos = -1
    key = None
    for k in keywords:
        p = low.find(k)
        if p != -1:
            pos = p + len(k)
            key = k
            break
    if pos == -1:
        # fallback: after 'offers a' or 'this establishment offers a'
        fallback_keys = ['this establishment offers a', 'this business offers a', 'this facility offers', 'this establishment offers']
        for k in fallback_keys:
            p = low.find(k)
            if p != -1:
                pos = p + len(k)
                key = k
                break
    if pos == -1:
        # last resort: use text after last comma
        parts = s.split(',')
        if len(parts) >= 2:
            tail = parts[-1]
        else:
            return []
    else:
        tail = s[pos:]
    # Trim after first period
    tail = tail.split('.')[0]
    # Split by common separators
    parts = [p.strip() for p in tail.replace(';',',').replace(' & ',',').split(',')]
    # Clean and filter
    cats = []
    for p in parts:
        p2 = p
        # remove leading words like 'including', 'such as'
        for prefix in ['including', 'such as', 'including a range of services like', 'including a range of services']:
            if p2.lower().startswith(prefix):
                p2 = p2[len(prefix):].strip()
        if len(p2) > 2:
            cats.append(p2)
    return cats

if 'description' not in df_b.columns:
    df_b['description'] = None

df_b['categories'] = df_b['description'].apply(extract_cats)

# Filter businesses accepting CC and with categories
df_cc = df_b[df_b['accepts_cc'] & df_b['categories'].map(lambda x: len(x)>0)].copy()

from collections import defaultdict
cat_to_biz = defaultdict(set)
for _, row in df_cc.iterrows():
    bid = row.get('business_id')
    cats = row.get('categories') or []
    for c in cats:
        cat_to_biz[c].add(bid)

# Prepare reviews
if df_r.empty:
    df_r = pd.DataFrame(columns=['business_ref','rating'])
else:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

results = []
for cat, biz_set in cat_to_biz.items():
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_set]
    mask = df_r['business_ref'].isin(biz_refs)
    ratings = df_r[mask]['rating'].dropna().astype(float)
    avg_rating = float(ratings.mean()) if not ratings.empty else None
    results.append({'category': cat, 'business_count': len(biz_set), 'average_rating': avg_rating})

if not results:
    out = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    results_sorted = sorted(results, key=lambda x: (x['business_count'], x['average_rating'] if x['average_rating'] is not None else -1), reverse=True)
    top = results_sorted[0]
    avg = None if top['average_rating'] is None else round(top['average_rating'], 2)
    out = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': avg}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kUMHHQgNcnp9xcqV7AbjenPP': 'file_storage/call_kUMHHQgNcnp9xcqV7AbjenPP.json', 'var_call_su679fGqLS4nfmXoMdtNWGxu': 'file_storage/call_su679fGqLS4nfmXoMdtNWGxu.json'}

exec(code, env_args)
