code = """import json
import pandas as pd

# Load data from previous tool calls
with open(var_call_351upF9ajrDuDXdWaZJ20Gro, 'r') as f:
    businesses = json.load(f)
with open(var_call_IfhiaA91o51YlbHgHKpGLQfP, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize attributes: some are strings 'None'
def accepts_credit(attrs):
    if not isinstance(attrs, dict):
        return False
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        return False
    # handle various representations
    if isinstance(val, bool):
        return val
    s = str(val)
    return s.lower().find('true') != -1

bdf['accepts_cc'] = bdf['attributes'].apply(accepts_credit)

# Normalize categories: may be missing or null
def extract_categories(cat):
    if pd.isna(cat):
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        # sometimes null-like strings
        if cat.strip().lower() in ('none','null',''):
            return []
        return [c.strip() for c in cat.split(',') if c.strip()]
    return []

bdf['categories_list'] = bdf.get('categories', pd.Series([None]*len(bdf))).apply(extract_categories)

# Filter businesses that accept credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()

# Explode categories and count per category
cc_biz_exploded = cc_biz.explode('categories_list')
cc_biz_exploded = cc_biz_exploded[cc_biz_exploded['categories_list'].notna()]

if cc_biz_exploded.empty:
    result = {'top_category': None, 'business_count': 0, 'average_rating': None}
else:
    counts = cc_biz_exploded['categories_list'].value_counts()
    top_category = counts.index[0]
    biz_count = int(counts.iloc[0])

    # Map businessid_x to businessref_x
    def to_businessref(bid):
        if not isinstance(bid, str):
            return None
        parts = bid.split('_', 1)
        if len(parts) == 2:
            return 'businessref_' + parts[1]
        return None

    top_biz_ids = cc_biz_exploded[cc_biz_exploded['categories_list'] == top_category]['business_id'].unique()
    top_biz_refs = set([to_businessref(b) for b in top_biz_ids if to_businessref(b) is not None])

    # Prepare reviews DataFrame
    if rdf.empty:
        avg_rating = None
    else:
        # ensure rating numeric
        rdf = rdf[rdf['business_ref'].notna() & rdf['rating'].notna()]
        rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
        sel = rdf[rdf['business_ref'].isin(top_biz_refs)]
        if sel.empty:
            avg_rating = None
        else:
            avg_rating = float(sel['rating'].mean())

    result = {'top_category': top_category, 'business_count': biz_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Cg65ZFW3PzhemgDYJz86wogR': ['checkin', 'business'], 'var_call_dlwQ63ehFVPelzf5TTRSOp3r': ['review', 'tip', 'user'], 'var_call_351upF9ajrDuDXdWaZJ20Gro': 'file_storage/call_351upF9ajrDuDXdWaZJ20Gro.json', 'var_call_IfhiaA91o51YlbHgHKpGLQfP': 'file_storage/call_IfhiaA91o51YlbHgHKpGLQfP.json'}

exec(code, env_args)
