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

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.findall(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m[-1]
    m2 = re.findall(r'\bin\s+[^,\n]+,\s*([A-Z]{2})\b', desc)
    if m2:
        return m2[-1]
    return None

dfb['state'] = dfb['description'].map(extract_state)

dfb['review_count'] = pd.to_numeric(dfb.get('review_count'), errors='coerce')

dfb_state = dfb.dropna(subset=['state'])

if dfb_state.empty:
    out = {'error': 'Could not extract state from business.description for any business.'}
    print('__RESULT__:')
    print(json.dumps(out))
    raise SystemExit

state_reviews = dfb_state.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]

a = dfb_state[['business_id','state']].copy()
a['business_ref'] = a['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)

biz_in_state = a[a['state'] == top_state][['business_ref']]

dfr['rating'] = pd.to_numeric(dfr.get('rating'), errors='coerce')
state_review_rows = dfr.merge(biz_in_state, on='business_ref', how='inner').dropna(subset=['rating'])

per_biz_avg = state_review_rows.groupby('business_ref')['rating'].mean()
state_business_avg_rating = float(per_biz_avg.mean()) if len(per_biz_avg) else None

out = {
    'state': top_state,
    'total_reviews': int(state_reviews.iloc[0]) if pd.notna(state_reviews.iloc[0]) else None,
    'avg_business_rating': None if state_business_avg_rating is None else round(state_business_avg_rating, 4),
    'num_businesses_in_state': int((a['state'] == top_state).sum()),
    'num_businesses_in_state_with_reviews': int(per_biz_avg.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4ocRhn2alhqrognZjJO3mvwM': 'file_storage/call_4ocRhn2alhqrognZjJO3mvwM.json', 'var_call_e8vh3vrf2HapSuLE8VVpkH89': 'file_storage/call_e8vh3vrf2HapSuLE8VVpkH89.json'}

exec(code, env_args)
