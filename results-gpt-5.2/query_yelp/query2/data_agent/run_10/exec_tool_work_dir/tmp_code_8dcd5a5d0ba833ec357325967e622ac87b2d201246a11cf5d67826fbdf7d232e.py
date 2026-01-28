code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

biz = load_records(var_call_BFmvWrcIdYM6QoXWZpkihIGs)
rev = load_records(var_call_PGyxSg78QMqSzUmhQZqKiMla)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# normalize types
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# extract state from description: look for ', XX' where XX is 2-letter
state_pat = re.compile(r'\b([A-Z][a-zA-Z .]+),\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.search(desc)
    if m:
        return m.group(2)
    return None

biz_df['state'] = biz_df['description'].map(extract_state)

# sum business review_count by state
state_reviews = biz_df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()
state_reviews = state_reviews.sort_values('review_count', ascending=False)

if state_reviews.empty:
    out = {"state": None, "total_reviews": 0, "avg_business_rating": None}
else:
    top_state = state_reviews.iloc[0]['state']
    total_reviews = int(state_reviews.iloc[0]['review_count'])

    # join reviews to businesses to get state
    biz_df2 = biz_df[['business_id','state']].dropna(subset=['state']).copy()
    # map businessid_X <-> businessref_X
    biz_df2['business_ref'] = biz_df2['business_id'].str.replace('businessid_', 'businessref_', regex=False)

    merged = rev_df.merge(biz_df2[['business_ref','state']], on='business_ref', how='inner')
    avg_rating = float(merged.loc[merged['state']==top_state, 'rating'].mean()) if (merged['state']==top_state).any() else None

    out = {"state": top_state, "total_reviews": total_reviews, "avg_business_rating": None if avg_rating is None else round(avg_rating, 4)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BFmvWrcIdYM6QoXWZpkihIGs': 'file_storage/call_BFmvWrcIdYM6QoXWZpkihIGs.json', 'var_call_PGyxSg78QMqSzUmhQZqKiMla': 'file_storage/call_PGyxSg78QMqSzUmhQZqKiMla.json'}

exec(code, env_args)
