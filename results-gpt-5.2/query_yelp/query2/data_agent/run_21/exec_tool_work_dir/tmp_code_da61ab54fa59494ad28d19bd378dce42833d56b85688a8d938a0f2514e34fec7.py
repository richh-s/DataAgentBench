code = """import json, re, pandas as pd

# Load business data
b = var_call_mbiPeEcSJERzYMFYbFc1xa3n
if isinstance(b, str):
    with open(b, 'r') as f:
        b = json.load(f)

db = pd.DataFrame(b)

# parse state from description: last ', ST,' or ', ST ' patterns
pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if desc is None:
        return None
    ms = pat.findall(desc)
    if not ms:
        return None
    # prefer last match (closest to end)
    return ms[-1]

db['state'] = db['description'].map(extract_state)
# clean review_count numeric
db['review_count'] = pd.to_numeric(db['review_count'], errors='coerce')

# keep US states only (2-letter, excluding common non-state like 'US') - but dataset appears US
biz_state = db.dropna(subset=['state','review_count'])[['business_id','state','review_count']]

# total reviews by state
state_reviews = biz_state.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

top_state = state_reviews.iloc[0].to_dict() if len(state_reviews) else {'state': None, 'review_count': None}

# Load reviews (business_ref, rating)
r = var_call_hPv0Fw6go1L457TQZ7YRhRr0
if isinstance(r, str):
    with open(r, 'r') as f:
        r = json.load(f)
dr = pd.DataFrame(r)
dr['rating'] = pd.to_numeric(dr['rating'], errors='coerce')

# map businessref_ -> businessid_
dr['business_id'] = dr['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

# average rating of businesses in that state (mean of review ratings for businesses located in that state)
bs = set(biz_state.loc[biz_state['state']==top_state['state'], 'business_id'])

dr_top = dr[dr['business_id'].isin(bs)].dropna(subset=['rating'])
avg_rating = float(dr_top['rating'].mean()) if len(dr_top) else None

out = {
    'state': top_state['state'],
    'total_reviews_in_state': int(top_state['review_count']) if pd.notna(top_state['review_count']) else None,
    'average_business_rating_in_state': round(avg_rating, 4) if avg_rating is not None else None
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mbiPeEcSJERzYMFYbFc1xa3n': 'file_storage/call_mbiPeEcSJERzYMFYbFc1xa3n.json', 'var_call_hPv0Fw6go1L457TQZ7YRhRr0': 'file_storage/call_hPv0Fw6go1L457TQZ7YRhRr0.json'}

exec(code, env_args)
