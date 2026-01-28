code = """import json
import pandas as pd

# Load data
with open(var_call_1uii8pNZd1IBGrZIeeZbTb8Z, 'r') as f:
    businesses = json.load(f)
with open(var_call_4GZQ1vFcyPhN3EeL2n8BFb59, 'r') as f:
    reviews = json.load(f)

# Simple helper to check credit card acceptance
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return str(val).lower() == 'true'
    s = str(attr)
    if 'BusinessAcceptsCreditCards' in s:
        return 'True' in s or "'True'" in s or 'true' in s
    return False

# Simple category extraction from description
def extract_categories(desc):
    if not desc:
        return []
    desc = desc.replace('\n', ' ')
    # Find 'in ' and take up to next period
    idx = desc.lower().find(' in ')
    if idx == -1:
        # fallback: try 'including '
        idx = desc.lower().find('including ')
        if idx == -1:
            return []
        start = idx + len('including ')
    else:
        start = idx + len(' in ')
    sub = desc[start:]
    # Cut at first period
    end = sub.find('.')
    if end != -1:
        sub = sub[:end]
    # Split by commas and ' and '
    parts = [p.strip() for p in sub.replace(' and ', ',').split(',') if p.strip()]
    # Clean parts
    parts = [p.strip("'\" ") for p in parts]
    return parts

# Build list
rows = []
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    accepts = accepts_cc(attrs)
    cats = b.get('categories')
    cat_list = []
    if cats:
        if isinstance(cats, list):
            cat_list = cats
        elif isinstance(cats, str):
            cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    if not cat_list:
        cat_list = extract_categories(b.get('description', ''))
    rows.append({'business_id': bid, 'accepts_cc': accepts, 'categories': cat_list})

biz_df = pd.DataFrame(rows)
if biz_df.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    biz_df = biz_df.explode('categories')
    biz_df['categories'] = biz_df['categories'].fillna('').astype(str).str.strip()
    cc_biz = biz_df[(biz_df['accepts_cc']==True) & (biz_df['categories']!='')].copy()
    cc_biz['category_norm'] = cc_biz['categories']
    cc_biz['business_ref'] = cc_biz['business_id'].str.replace('businessid_', 'businessref_')

    # reviews df
    rev_df = pd.DataFrame(reviews)
    if not rev_df.empty:
        rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    else:
        rev_df['rating'] = pd.Series(dtype=float)

    # counts
    cat_counts = cc_biz.groupby('category_norm')['business_ref'].nunique().reset_index().rename(columns={'business_ref':'business_count'})

    # merge reviews
    biz_cat = cc_biz[['business_ref','category_norm']].drop_duplicates()
    if not rev_df.empty:
        rev_join = rev_df.merge(biz_cat, on='business_ref', how='inner')
        cat_avg = rev_join.groupby('category_norm')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})
    else:
        cat_avg = pd.DataFrame(columns=['category_norm','avg_rating'])

    summary = cat_counts.merge(cat_avg, on='category_norm', how='left')
    if summary.empty:
        result = {'category': None, 'business_count': 0, 'average_rating': None}
    else:
        # round avg
        summary['avg_rating'] = summary['avg_rating'].round(2)
        max_count = int(summary['business_count'].max())
        top = summary[summary['business_count']==max_count]
        # choose highest avg_rating where available
        top = top.sort_values(['avg_rating','category_norm'], ascending=[False, True]).iloc[0]
        avg = None if pd.isna(top['avg_rating']) else float(top['avg_rating'])
        result = {'category': top['category_norm'], 'business_count': int(top['business_count']), 'average_rating': avg}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ryydk2OydyICGOkK0fdQmodU': ['business', 'checkin'], 'var_call_s0HAPJstiC6duixg4yD27A9v': ['review', 'tip', 'user'], 'var_call_1uii8pNZd1IBGrZIeeZbTb8Z': 'file_storage/call_1uii8pNZd1IBGrZIeeZbTb8Z.json', 'var_call_4GZQ1vFcyPhN3EeL2n8BFb59': 'file_storage/call_4GZQ1vFcyPhN3EeL2n8BFb59.json'}

exec(code, env_args)
