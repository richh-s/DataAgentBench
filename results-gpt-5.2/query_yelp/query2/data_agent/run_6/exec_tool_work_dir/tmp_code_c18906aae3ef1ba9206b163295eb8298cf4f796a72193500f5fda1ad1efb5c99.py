code = """import json, re, pandas as pd

biz_src = var_call_lNfQKLT3HTZl2mmF2RHMdl2D
if isinstance(biz_src, str):
    with open(biz_src, 'r') as f:
        biz = json.load(f)
else:
    biz = biz_src

rev_src = var_call_i9Nqza4MOzDHHYXFmk4Zxmxa
if isinstance(rev_src, str):
    with open(rev_src, 'r') as f:
        rev = json.load(f)
else:
    rev = rev_src

biz_df = pd.DataFrame(biz)
state_re = re.compile(r'\b([A-Z]{2})\b')

# extract state as token after last comma
state_after_comma = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_after_comma.findall(desc)
    return m[-1] if m else None

biz_df['state'] = biz_df.get('description', pd.Series(dtype=object)).map(extract_state)
biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count', 0), errors='coerce').fillna(0).astype(int)

state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)
if state_reviews.empty:
    out = {"error":"Could not extract any state codes from business.description"}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    top_state = state_reviews.index[0]
    top_state_reviews = int(state_reviews.iloc[0])

    rev_df = pd.DataFrame(rev)
    rev_df['rating'] = pd.to_numeric(rev_df.get('rating', None), errors='coerce')
    rev_df['business_id'] = rev_df.get('business_ref', pd.Series(dtype=str)).astype(str).str.replace('businessref_', 'businessid_', regex=False)

    joined = rev_df.merge(biz_df[['business_id','state']], on='business_id', how='left')
    state_ratings = joined.loc[joined['state'] == top_state, 'rating'].dropna()
    avg_rating = float(state_ratings.mean()) if len(state_ratings) else None

    out = {
        "state": top_state,
        "total_reviews_in_state": top_state_reviews,
        "average_rating_in_state": None if avg_rating is None else round(avg_rating, 4)
    }
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_lNfQKLT3HTZl2mmF2RHMdl2D': 'file_storage/call_lNfQKLT3HTZl2mmF2RHMdl2D.json', 'var_call_i9Nqza4MOzDHHYXFmk4Zxmxa': 'file_storage/call_i9Nqza4MOzDHHYXFmk4Zxmxa.json'}

exec(code, env_args)
