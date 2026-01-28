code = """import json
import pandas as pd

# Load data from provided storage keys
with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

# DataFrames
b = pd.DataFrame(businesses)
r = pd.DataFrame(reviews)

# Ensure columns exist
if 'attributes' not in b.columns:
    b['attributes'] = None
if 'categories' not in b.columns:
    b['categories'] = None

# Detect accepts credit cards
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attr).lower()
    return 'businessacceptscreditcards' in s and 'true' in s

b['accepts_cc'] = b['attributes'].apply(accepts_cc)

# Build category list from categories field or description
def categories_from_row(row):
    c = row.get('categories')
    if c and not (isinstance(c, str) and c.lower() == 'none'):
        if isinstance(c, list):
            return [str(x).strip() for x in c if str(x).strip()]
        return [p.strip() for p in str(c).split(',') if p.strip()]
    desc = row.get('description')
    if not isinstance(desc, str):
        return []
    s = desc
    low = s.lower()
    # Look for patterns
    # pattern: 'offers ... in X, Y, Z.'
    idx = low.find(' offers')
    if idx != -1:
        idx2 = low.find(' in ', idx)
        if idx2 != -1:
            subs = s[idx2+4:]
            dot = subs.find('.')
            if dot != -1:
                subs = subs[:dot]
            parts = [p.strip().strip("\"\'") for p in subs.replace('&', ',').replace('/', ',').split(',')]
            return [p for p in parts if p]
    # pattern: 'category of '
    key = 'category of '
    kpos = low.find(key)
    if kpos != -1:
        subs = s[kpos+len(key):]
        dot = subs.find('.')
        if dot != -1:
            subs = subs[:dot]
        parts = [p.strip() for p in subs.replace('&', ',').replace('/', ',').split(',')]
        return [p for p in parts if p]
    # fallback empty
    return []

b['category_list'] = b.apply(categories_from_row, axis=1)

# Map business_id to business_ref
def to_ref(bid):
    if isinstance(bid, str):
        return bid.replace('businessid_', 'businessref_')
    return None

b['business_ref'] = b['business_id'].apply(to_ref)

# Filter businesses accepting credit cards
acc = b[b['accepts_cc'] == True].copy()

# Explode categories
if 'category_list' not in acc.columns:
    acc['category_list'] = [[] for _ in range(len(acc))]
expl = acc.explode('category_list')

# Clean categories
expl['category_list'] = expl['category_list'].apply(lambda x: x.strip() if isinstance(x, str) else x)
expl = expl[expl['category_list'].notna() & (expl['category_list'] != '')]

result = {'category': None, 'business_count': 0, 'average_rating': None}

if not expl.empty:
    counts = expl.groupby('category_list')['business_id'].nunique()
    counts = counts.sort_values(ascending=False)
    top_cat = counts.index[0]
    top_count = int(counts.iloc[0])
    refs = set(expl[expl['category_list'] == top_cat]['business_ref'].dropna().tolist())

    # Prepare reviews
    if not r.empty:
        r['rating'] = pd.to_numeric(r['rating'], errors='coerce')
    else:
        r['rating'] = pd.Series(dtype=float)
    sel = r[r['business_ref'].isin(refs)]
    if len(sel) > 0:
        avg = round(float(sel['rating'].mean()), 2)
    else:
        avg = None
    result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json'}

exec(code, env_args)
