code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_NduHWfREmhHf1IfnpjdzGQu4)
rev = load_records(var_call_13zbTIgugNKqhUJvAucMiHGz)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# normalize types
for c in ['review_count']:
    if c in dfb.columns:
        dfb[c] = pd.to_numeric(dfb[c], errors='coerce')
if 'rating' in dfr.columns:
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

# extract state from description: last occurrence of ", XX" where XX are two letters
state_pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb['description'].map(extract_state)

# total reviews per state from business.review_count
state_reviews = dfb.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()
state_reviews = state_reviews.sort_values('review_count', ascending=False)

top_state = state_reviews.iloc[0]['state']

# map business_ref -> business_id
# businessid_X <-> businessref_X

dfb['business_ref'] = dfb['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

# average rating of businesses in that state (using review table ratings for businesses in that state)
state_biz_refs = set(dfb.loc[dfb['state']==top_state, 'business_ref'].dropna().tolist())
dfr_state = dfr[dfr['business_ref'].isin(state_biz_refs)].dropna(subset=['rating'])
avg_rating = float(dfr_state['rating'].mean()) if len(dfr_state) else None

total_reviews = int(state_reviews.iloc[0]['review_count']) if pd.notna(state_reviews.iloc[0]['review_count']) else None

out = {
    'state': top_state,
    'total_review_count': total_reviews,
    'average_business_rating_in_state': None if avg_rating is None else round(avg_rating, 4)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NduHWfREmhHf1IfnpjdzGQu4': 'file_storage/call_NduHWfREmhHf1IfnpjdzGQu4.json', 'var_call_13zbTIgugNKqhUJvAucMiHGz': 'file_storage/call_13zbTIgugNKqhUJvAucMiHGz.json'}

exec(code, env_args)
