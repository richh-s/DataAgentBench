code = """import json
import pandas as pd

# Load files
with open(var_call_v4PFAHXQgeJFQhadysNlv4rK, 'r') as f:
    businesses = json.load(f)
with open(var_call_tV5Ysp0Q7UR4tdGymlUigNb5, 'r') as f:
    reviews = json.load(f)

# helpers
def extract_num_id(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_')
    return parts[-1]

def accepts_cc(attr):
    if attr is None:
        return False
    s = str(attr).lower()
    if 'businessacceptscreditcards' in s and 'true' in s:
        return True
    return False

def extract_categories(b):
    cat = b.get('categories', None)
    if cat and isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if cat and isinstance(cat, str):
        return [c.strip().strip("'\"") for c in cat.split(',') if c.strip()]
    desc = b.get('description', '')
    if not isinstance(desc, str) or not desc:
        return []
    low = desc.lower()
    idx = low.find(' in ')
    if idx != -1:
        seg = desc[idx+4:]
        seg = seg.split('.')[0]
        seg = seg.replace(' & ', ',').replace(' and ', ',')
        parts = [p.strip().strip("'\"") for p in seg.split(',') if p.strip()]
        return parts
    return []

rows = []
for b in businesses:
    biz_id = b.get('business_id')
    biz_num = extract_num_id(biz_id)
    acc = accepts_cc(b.get('attributes', None))
    cats = extract_categories(b)
    rows.append({'biz_num': biz_num, 'accepts_cc': acc, 'categories': cats})

bdf = pd.DataFrame(rows)

# filter accepting cc
cc_biz = bdf[bdf['accepts_cc'] == True].copy()
if cc_biz.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cc_biz_expl = cc_biz.explode('categories')
    cc_biz_expl = cc_biz_expl[cc_biz_expl['categories'].notna() & (cc_biz_expl['categories'] != '')]
    if cc_biz_expl.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        cat_counts = cc_biz_expl.groupby('categories')['biz_num'].nunique().reset_index()
        cat_counts = cat_counts.rename(columns={'categories':'category','biz_num':'business_count'})
        cat_counts = cat_counts.sort_values(['business_count','category'], ascending=[False, True])
        top = cat_counts.iloc[0]
        top_cat = top['category']
        top_count = int(top['business_count'])
        biz_nums_in_top = cc_biz_expl[cc_biz_expl['categories'] == top_cat]['biz_num'].unique().tolist()
        rdf = pd.DataFrame(reviews)
        rdf['biz_num'] = rdf['business_ref'].apply(extract_num_id)
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        revs_top = rdf[rdf['biz_num'].isin(biz_nums_in_top)]
        if revs_top.empty:
            avg_rating = None
        else:
            avg_rating = round(float(revs_top['rating'].mean()), 2)
        result = {'category': top_cat, 'business_count': top_count, 'average_rating': avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WxTjm8yJBKjgiFdZopzR8a8o': 'file_storage/call_WxTjm8yJBKjgiFdZopzR8a8o.json', 'var_call_tV5Ysp0Q7UR4tdGymlUigNb5': 'file_storage/call_tV5Ysp0Q7UR4tdGymlUigNb5.json', 'var_call_6SH0MDadi61uDz9mR8tLuNgV': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_v4PFAHXQgeJFQhadysNlv4rK': 'file_storage/call_v4PFAHXQgeJFQhadysNlv4rK.json'}

exec(code, env_args)
