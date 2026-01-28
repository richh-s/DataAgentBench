code = """import json, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r') as f:
            return json.load(f)
    return maybe_path_or_list

biz = load_records(var_call_pao436vq04C7IK0fiIv8POaJ)
rev = load_records(var_call_zoHurNmxhO3P7Bd2NuhxY0Hl)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

desc = biz_df['description'].fillna('')
# better regex: match US state code preceded by comma and followed by comma or end/space
state = desc.str.extract(r',\s*([A-Z]{2})(?:\s*,|\s+\d{5}|\b)', expand=False)
# also handle 'City, ST location'
state = state.fillna(desc.str.extract(r'\b([A-Z]{2})\s+location\b', expand=False))

biz_df = biz_df.assign(state=state)

biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce').fillna(0).astype(int)
state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

if len(state_reviews)==0:
    out={'error':'Could not extract any state codes'}
else:
    top_state = state_reviews.index[0]
    top_total = int(state_reviews.iloc[0])

    biz_df['business_ref'] = biz_df['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

    state_refs = set(biz_df.loc[biz_df['state']==top_state, 'business_ref'].dropna().astype(str))
    state_rev = rev_df[rev_df['business_ref'].astype(str).isin(state_refs)]
    avg_rating = float(state_rev['rating'].mean()) if len(state_rev) else None

    out={
        'state': top_state,
        'total_reviews_in_state': top_total,
        'average_rating_in_state': None if avg_rating is None else round(avg_rating,4)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_pao436vq04C7IK0fiIv8POaJ': 'file_storage/call_pao436vq04C7IK0fiIv8POaJ.json', 'var_call_zoHurNmxhO3P7Bd2NuhxY0Hl': 'file_storage/call_zoHurNmxhO3P7Bd2NuhxY0Hl.json', 'var_call_XBxE419JlGhOBGDPmAWK3soq': {'error': 'Could not extract any state codes from business.description'}, 'var_call_3RsfTIoz9HuTlwpMaqGy0znz': 'file_storage/call_3RsfTIoz9HuTlwpMaqGy0znz.json'}

exec(code, env_args)
