code = """import json
import pandas as pd

# Load data
with open(var_call_By0YsQSKO0TUH7HYGOuh2IE3, 'r') as f:
    businesses = json.load(f)
with open(var_call_TlPasEwRwrpoipslO3NtzTX9, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# detect accepts credit cards
def accepts_credit(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return 'true' in str(val).lower()
    s = str(attr).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# build categories list
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
    # find ' offers' then ' in '
    pos = low.find(' offers')
    if pos != -1:
        pos2 = low.find(' in ', pos)
        if pos2 != -1:
            subs = s[pos2+4:]
            dot = subs.find('.')
            if dot != -1:
                subs = subs[:dot]
            subs = subs.replace('&', ',').replace('/', ',')
            parts = [p.strip() for p in subs.split(',') if p.strip()]
            return parts
    # try 'category of '
    key = 'category of '
    kpos = low.find(key)
    if kpos != -1:
        subs = s[kpos+len(key):]
        dot = subs.find('.')
        if dot != -1:
            subs = subs[:dot]
        subs = subs.replace('&', ',').replace('/', ',')
        parts = [p.strip() for p in subs.split(',') if p.strip()]
        return parts
    return []

df_b['category_list'] = df_b.apply(categories_from_row, axis=1)

# map business_id to business_ref
def to_ref(bid):
    if isinstance(bid, str):
        return bid.replace('businessid_', 'businessref_')
    return None

df_b['business_ref'] = df_b['business_id'].apply(to_ref)

# filter businesses that accept credit cards
df_acc = df_b[df_b['accepts_cc'] == True].copy()

# explode categories
if 'category_list' not in df_acc.columns:
    df_acc['category_list'] = [[] for _ in range(len(df_acc))]

df_expl = df_acc.explode('category_list')
if df_expl.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_expl['category_list'] = df_expl['category_list'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list'] != '')]
    if df_expl.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        counts = df_expl.groupby('category_list')['business_id'].nunique()
        counts = counts.sort_values(ascending=False)
        top_cat = counts.index[0]
        top_count = int(counts.iloc[0])
        refs = set(df_expl[df_expl['category_list'] == top_cat]['business_ref'].dropna().tolist())
        # prepare reviews
        if not df_r.empty:
            df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        else:
            df_r['rating'] = pd.Series(dtype=float)
        sel = df_r[df_r['business_ref'].isin(refs)]
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
