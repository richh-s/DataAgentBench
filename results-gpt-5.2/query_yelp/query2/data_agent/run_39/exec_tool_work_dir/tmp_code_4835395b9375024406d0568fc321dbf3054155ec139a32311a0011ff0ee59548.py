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
if 'review_count' in dfb.columns:
    dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce')
if 'rating' in dfr.columns:
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

state_pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb.get('description', pd.Series([None]*len(dfb))).map(extract_state)

state_reviews = dfb.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    out = {'state': None, 'total_review_count': None, 'average_business_rating_in_state': None}
else:
    state_reviews = state_reviews.sort_values('review_count', ascending=False)
    top_state = state_reviews.iloc[0]['state']
    total_reviews = state_reviews.iloc[0]['review_count']
    total_reviews = int(total_reviews) if pd.notna(total_reviews) else None

    dfb['business_ref'] = dfb['business_id'].astype(str).str.replace('businessid_', 'businessref_', regex=False)
    state_biz_refs = set(dfb.loc[dfb['state']==top_state, 'business_ref'].dropna().tolist())
    dfr_state = dfr[dfr['business_ref'].isin(state_biz_refs)].dropna(subset=['rating'])
    avg_rating = float(dfr_state['rating'].mean()) if len(dfr_state) else None

    out = {
        'state': top_state,
        'total_review_count': total_reviews,
        'average_business_rating_in_state': None if avg_rating is None else round(avg_rating, 4)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NduHWfREmhHf1IfnpjdzGQu4': 'file_storage/call_NduHWfREmhHf1IfnpjdzGQu4.json', 'var_call_13zbTIgugNKqhUJvAucMiHGz': 'file_storage/call_13zbTIgugNKqhUJvAucMiHGz.json'}

exec(code, env_args)
