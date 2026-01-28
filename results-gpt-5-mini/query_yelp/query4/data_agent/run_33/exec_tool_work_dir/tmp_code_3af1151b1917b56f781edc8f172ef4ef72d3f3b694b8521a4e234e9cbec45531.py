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
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return 'true' in str(v).lower()
    s = str(attrs).lower()
    return ('businessacceptscreditcards' in s and 'true' in s)

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# build categories list
def categories_from_row(row):
    c = row.get('categories')
    if c and not (isinstance(c, str) and c.lower()=='none'):
        if isinstance(c, list):
            return [str(x).strip() for x in c if str(x).strip()]
        s = str(c)
        return [p.strip() for p in s.split(',') if p.strip()]
    desc = row.get('description')
    if not isinstance(desc, str):
        return []
    s = desc
    sl = s.lower()
    # try to find ' in ' after 'offers'
    offers_pos = sl.find(' offers')
    if offers_pos != -1:
        in_pos = sl.find(' in ', offers_pos)
        if in_pos != -1:
            subs = s[in_pos+4:]
            # cut at first period
            dot = subs.find('.')
            if dot != -1:
                subs = subs[:dot]
            # split by common separators
            parts = [p.strip().strip("'\"") for p in subs.replace('&', ',').replace('/', ',').split(',')]
            parts = [p for p in parts if p]
            return parts
    # try 'category of'
    key = 'category of '
    kpos = sl.find(key)
    if kpos != -1:
        subs = s[kpos+len(key):]
        dot = subs.find('.')
        if dot != -1:
            subs = subs[:dot]
        parts = [p.strip() for p in subs.replace('&', ',').replace('/', ',').split(',')]
        parts = [p for p in parts if p]
        return parts
    return []


df_b['category_list'] = df_b.apply(categories_from_row, axis=1)

# business_ref
def to_ref(bid):
    if isinstance(bid, str):
        return bid.replace('businessid_', 'businessref_')
    return None

df_b['business_ref'] = df_b['business_id'].apply(to_ref)

# filter businesses accepting CC
df_acc = df_b[df_b['accepts_cc']==True].copy()

# explode
if 'category_list' not in df_acc.columns:
    df_acc['category_list'] = [[] for _ in range(len(df_acc))]

df_expl = df_acc.explode('category_list')
if df_expl.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    df_expl['category_list'] = df_expl['category_list'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list']!='')]
    if df_expl.empty:
        result = {"category": None, "business_count": 0, "average_rating": None}
    else:
        counts = df_expl.groupby('category_list')['business_id'].nunique()
        counts = counts.sort_values(ascending=False)
        top_cat = counts.index[0]
        top_count = int(counts.iloc[0])
        refs_in_top = set(df_expl[df_expl['category_list']==top_cat]['business_ref'].dropna().tolist())
        # reviews numeric
        if not df_r.empty:
            df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
        else:
            df_r['rating'] = pd.Series(dtype=float)
        df_sel = df_r[df_r['business_ref'].isin(refs_in_top)]
        if len(df_sel)>0:
            avg_rating = round(float(df_sel['rating'].mean()),2)
        else:
            avg_rating = None
        result = {"category": top_cat, "business_count": top_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zYWWfxdtpjIy5owlOM4SaGDn': ['business', 'checkin'], 'var_call_mHA3vgr16eyfCZYaS9qPg3uP': ['review', 'tip', 'user'], 'var_call_By0YsQSKO0TUH7HYGOuh2IE3': 'file_storage/call_By0YsQSKO0TUH7HYGOuh2IE3.json', 'var_call_TlPasEwRwrpoipslO3NtzTX9': 'file_storage/call_TlPasEwRwrpoipslO3NtzTX9.json', 'var_call_y3E5KsRHzfEDIvVCCDQoNDKU': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_4EyBBhMx0IX87GBMEIVF9q5X': 'file_storage/call_4EyBBhMx0IX87GBMEIVF9q5X.json'}

exec(code, env_args)
