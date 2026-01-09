code = """import json, re, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r') as f:
            return json.load(f)
    return maybe_path_or_list

biz = load_records(var_call_pao436vq04C7IK0fiIv8POaJ)
rev = load_records(var_call_zoHurNmxhO3P7Bd2NuhxY0Hl)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# Extract state from description: try ' in City, ST' then fallback to first ', ST'
desc = biz_df['description'].fillna('')
state1 = desc.str.extract(r'\bin\s+[^,]+,\s*([A-Z]{2})\b', expand=False)
state2 = desc.str.extract(r',\s*([A-Z]{2})\b', expand=False)
state = state1.fillna(state2)
biz_df = biz_df.assign(state=state)

biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce').fillna(0).astype(int)

state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if len(state_reviews)==0:
    out = {'error':'Could not extract any state codes from business.description'}
else:
    top_state = state_reviews.index[0]
    top_state_total_reviews = int(state_reviews.iloc[0])

    biz_df['business_ref'] = biz_df['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

    state_biz_refs = set(biz_df.loc[biz_df['state']==top_state, 'business_ref'].dropna().astype(str))
    state_rev = rev_df[rev_df['business_ref'].astype(str).isin(state_biz_refs)].copy()
    avg_rating = float(state_rev['rating'].mean()) if len(state_rev) else None

    out = {
        'state': top_state,
        'total_reviews_in_state': top_state_total_reviews,
        'average_rating_in_state': None if avg_rating is None else round(avg_rating, 4),
        'rating_review_count_used': int(state_rev['rating'].notna().sum())
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pao436vq04C7IK0fiIv8POaJ': 'file_storage/call_pao436vq04C7IK0fiIv8POaJ.json', 'var_call_zoHurNmxhO3P7Bd2NuhxY0Hl': 'file_storage/call_zoHurNmxhO3P7Bd2NuhxY0Hl.json'}

exec(code, env_args)
