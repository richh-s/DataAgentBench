code = """import json
import pandas as pd

# Load data files from storage
with open(var_call_1uii8pNZd1IBGrZIeeZbTb8Z, 'r') as f:
    businesses = json.load(f)
with open(var_call_4GZQ1vFcyPhN3EeL2n8BFb59, 'r') as f:
    reviews = json.load(f)

# Helper to determine if business accepts credit cards
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return str(val).strip().lower() == 'true'
    s = str(attr)
    if 'BusinessAcceptsCreditCards' in s:
        return 'True' in s or "'True'" in s or 'true' in s
    return False

# Helper to extract categories from business fields
def get_categories(b):
    cats = b.get('categories')
    if cats:
        if isinstance(cats, list):
            return [c.strip() for c in cats if c and str(c).strip()]
        if isinstance(cats, str):
            return [c.strip() for c in cats.split(',') if c.strip()]
    desc = b.get('description') or ''
    if not desc:
        return []
    text = desc
    # look for 'in ' first occurrence
    low = text.lower()
    idx = low.find(' in ')
    start = 0
    if idx != -1:
        start = idx + 4
    else:
        idx = low.find('including ')
        if idx != -1:
            start = idx + len('including ')
        else:
            # fallback: try after 'offers ' or 'offers a range of services in '
            idx = low.find('offers a range of services in ')
            if idx != -1:
                start = idx + len('offers a range of services in ')
            else:
                return []
    sub = text[start:]
    # cut at period
    if '.' in sub:
        sub = sub.split('.',1)[0]
    # cut at ' to ' if appears early
    if ' to ' in sub:
        # keep part before ' to '
        sub = sub.split(' to ',1)[0]
    # replace ' and ' with comma
    sub = sub.replace(' and ', ',')
    parts = [p.strip().strip("'\"") for p in sub.split(',') if p.strip()]
    return parts

# Build dataframe of businesses that accept cc with categories
rows = []
for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    if accepts_cc(b.get('attributes')):
        cats = get_categories(b)
        for c in cats:
            if c:
                rows.append({'business_id': bid, 'category': c})

biz_cc_df = pd.DataFrame(rows)
if biz_cc_df.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # count unique businesses per category
    biz_cc_df['business_ref'] = biz_cc_df['business_id'].str.replace('businessid_', 'businessref_')
    counts = biz_cc_df.groupby('category')['business_ref'].nunique().reset_index().rename(columns={'business_ref':'business_count'})

    # prepare reviews
    rev_df = pd.DataFrame(reviews)
    if not rev_df.empty:
        rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    else:
        rev_df['rating'] = pd.Series(dtype=float)

    # map reviews to categories via business_ref
    biz_cat = biz_cc_df[['business_ref','category']].drop_duplicates()
    rev_join = rev_df.merge(biz_cat, on='business_ref', how='inner') if not rev_df.empty else pd.DataFrame(columns=['business_ref','rating','category'])
    avg = rev_join.groupby('category')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

    summary = counts.merge(avg, on='category', how='left')
    summary['avg_rating'] = summary['avg_rating'].round(2)
    # pick category with max business_count, tie-breaker by higher avg_rating
    max_count = int(summary['business_count'].max())
    top = summary[summary['business_count']==max_count].sort_values('avg_rating', ascending=False).iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': (None if pd.isna(top['avg_rating']) else float(top['avg_rating']))}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Ryydk2OydyICGOkK0fdQmodU': ['business', 'checkin'], 'var_call_s0HAPJstiC6duixg4yD27A9v': ['review', 'tip', 'user'], 'var_call_1uii8pNZd1IBGrZIeeZbTb8Z': 'file_storage/call_1uii8pNZd1IBGrZIeeZbTb8Z.json', 'var_call_4GZQ1vFcyPhN3EeL2n8BFb59': 'file_storage/call_4GZQ1vFcyPhN3EeL2n8BFb59.json', 'var_call_Da3AGLLQqDg6FPTJG5GiDHq9': {'ok': True}}

exec(code, env_args)
