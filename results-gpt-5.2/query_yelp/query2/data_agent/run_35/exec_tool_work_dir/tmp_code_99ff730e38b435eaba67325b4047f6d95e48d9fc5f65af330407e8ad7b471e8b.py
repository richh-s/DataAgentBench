code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_4ocRhn2alhqrognZjJO3mvwM)
rev = load_records(var_call_e8vh3vrf2HapSuLE8VVpkH89)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# parse state from description: last occurrence of ', XX' where XX is 2-letter
state_pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb['description'].map(extract_state)

dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce')

# sum business review_count by state
state_reviews = dfb.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]

# average rating of businesses in that state: compute avg rating per business from reviews, then average across businesses in state
# align ids: businessid_X <-> businessref_X
id_map = dfb[['business_id','state']].copy()
id_map['business_ref'] = id_map['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# reviews for businesses in top_state
biz_in_state = id_map[id_map['state'] == top_state][['business_ref']]
state_review_rows = dfr.merge(biz_in_state, on='business_ref', how='inner')
state_review_rows['rating'] = pd.to_numeric(state_review_rows['rating'], errors='coerce')

per_biz_avg = state_review_rows.groupby('business_ref', dropna=True)['rating'].mean()
state_business_avg_rating = float(per_biz_avg.mean()) if len(per_biz_avg) else None

out = {
    'state': top_state,
    'total_reviews': int(state_reviews.iloc[0]) if pd.notna(state_reviews.iloc[0]) else None,
    'avg_business_rating': None if state_business_avg_rating is None else round(state_business_avg_rating, 4),
    'num_businesses_in_state_with_reviews': int(per_biz_avg.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4ocRhn2alhqrognZjJO3mvwM': 'file_storage/call_4ocRhn2alhqrognZjJO3mvwM.json', 'var_call_e8vh3vrf2HapSuLE8VVpkH89': 'file_storage/call_e8vh3vrf2HapSuLE8VVpkH89.json'}

exec(code, env_args)
