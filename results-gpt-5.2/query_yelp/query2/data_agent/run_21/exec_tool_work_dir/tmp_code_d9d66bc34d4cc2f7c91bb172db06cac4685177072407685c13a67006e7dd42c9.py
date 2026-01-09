code = """import json, re, pandas as pd

b = var_call_mbiPeEcSJERzYMFYbFc1xa3n
if isinstance(b, str):
    with open(b, 'r') as f:
        b = json.load(f)
db = pd.DataFrame(b)

db['review_count'] = pd.to_numeric(db['review_count'], errors='coerce')

# Better state extraction: match two-letter after ' in ' and before comma: ' in City, ST,'
pat1 = re.compile(r'\bin\s+[^,]+,\s*([A-Z]{2})\b')
pat2 = re.compile(r'\b([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat1.search(desc)
    if m:
        return m.group(1)
    # fallback: last 2-letter token preceded by comma
    m2 = re.findall(r',\s*([A-Z]{2})\b', desc)
    return m2[-1] if m2 else None

db['state'] = db['description'].map(extract_state)

biz_state = db.dropna(subset=['state','review_count'])[['business_id','state','review_count']]

state_reviews = biz_state.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)

top_state = state_reviews.iloc[0].to_dict() if len(state_reviews) else {'state': None, 'review_count': None}

# Load reviews
r = var_call_hPv0Fw6go1L457TQZ7YRhRr0
if isinstance(r, str):
    with open(r, 'r') as f:
        r = json.load(f)
dr = pd.DataFrame(r)
dr['rating'] = pd.to_numeric(dr['rating'], errors='coerce')
dr['business_id'] = dr['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

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

env_args = {'var_call_mbiPeEcSJERzYMFYbFc1xa3n': 'file_storage/call_mbiPeEcSJERzYMFYbFc1xa3n.json', 'var_call_hPv0Fw6go1L457TQZ7YRhRr0': 'file_storage/call_hPv0Fw6go1L457TQZ7YRhRr0.json', 'var_call_AzqdJv3Ap6l5HZdKKsRoBNnv': {'state': None, 'total_reviews_in_state': None, 'average_business_rating_in_state': None}}

exec(code, env_args)
