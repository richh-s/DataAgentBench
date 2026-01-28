code = """import json, pandas as pd, re

# load business
biz_src = var_call_A1GsIb5otu5FJBZemJyHr0dr
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev_src = var_call_wrUkebJg677Q8FvIM4b4eN6k
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# parse state from description: assume ' in City, ST,' pattern
state_pat = re.compile(r"\b([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # prefer pattern ', ST,'
    m = re.search(r",\s*([A-Z]{2})\s*,", desc)
    if m:
        return m.group(1)
    # fallback: ' in City, ST' end
    m = re.search(r"\b([A-Z]{2})\b", desc)
    if m:
        return m.group(1)
    return None

biz_df['state'] = biz_df['description'].map(extract_state)
# coerce review_count to int
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce')

# compute state with highest number of reviews (sum of business review_count)
state_reviews = biz_df.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()
state_top = state_reviews.sort_values('review_count', ascending=False).head(1)
if state_top.empty:
    out = {"state": None, "total_reviews": None, "avg_business_rating_in_state": None}
else:
    top_state = state_top.iloc[0]['state']
    total_reviews = int(state_top.iloc[0]['review_count'])

    # map ids and join to reviews to compute avg rating for businesses in that state
    biz_state = biz_df[biz_df['state']==top_state][['business_id']].copy()
    biz_state['business_ref'] = biz_state['business_id'].str.replace('businessid_', 'businessref_', regex=False)

    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
    merged = rev_df.merge(biz_state[['business_ref']], on='business_ref', how='inner')
    avg_rating = float(merged['rating'].mean()) if not merged.empty else None

    out = {"state": top_state, "total_reviews": total_reviews, "avg_business_rating_in_state": avg_rating}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_A1GsIb5otu5FJBZemJyHr0dr': 'file_storage/call_A1GsIb5otu5FJBZemJyHr0dr.json', 'var_call_wrUkebJg677Q8FvIM4b4eN6k': 'file_storage/call_wrUkebJg677Q8FvIM4b4eN6k.json'}

exec(code, env_args)
