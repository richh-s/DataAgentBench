code = """import json, re
import pandas as pd

# Load full business records
biz_src = var_call_Fx3zc4SX715SxNjOvTSO9HDX
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev_src = var_call_Xhl59CkWW932oOi0YFE0AWd0
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# Parse state abbreviation from description (look for ', XX' where XX is state)
state_pat = re.compile(r',\s*([A-Z]{2})(?:\s|\.|,|$)')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Coerce counts/ratings to numeric
biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce')
rev_df['rating'] = pd.to_numeric(rev_df.get('rating'), errors='coerce')

# Map businessref_# -> businessid_#
rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

# Highest number of reviews by state: sum business.review_count
state_reviews = biz_df.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()
state_reviews = state_reviews.sort_values(['review_count','state'], ascending=[False, True]).reset_index(drop=True)

top_state = state_reviews.iloc[0]['state'] if len(state_reviews) else None

def avg_rating_for_state(st):
    if st is None:
        return None
    biz_ids = set(biz_df.loc[biz_df['state']==st, 'business_id'].dropna().astype(str))
    st_reviews = rev_df[rev_df['business_id'].isin(biz_ids)].dropna(subset=['rating'])
    if len(st_reviews)==0:
        return None
    return float(st_reviews['rating'].mean())

avg_rating = avg_rating_for_state(top_state)

total_reviews = float(state_reviews.iloc[0]['review_count']) if len(state_reviews) else None

out = {
    'state': top_state,
    'total_reviews_in_state': int(total_reviews) if total_reviews is not None and pd.notna(total_reviews) else None,
    'average_business_rating_in_state': round(avg_rating, 3) if avg_rating is not None else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Fx3zc4SX715SxNjOvTSO9HDX': 'file_storage/call_Fx3zc4SX715SxNjOvTSO9HDX.json', 'var_call_Xhl59CkWW932oOi0YFE0AWd0': 'file_storage/call_Xhl59CkWW932oOi0YFE0AWd0.json'}

exec(code, env_args)
