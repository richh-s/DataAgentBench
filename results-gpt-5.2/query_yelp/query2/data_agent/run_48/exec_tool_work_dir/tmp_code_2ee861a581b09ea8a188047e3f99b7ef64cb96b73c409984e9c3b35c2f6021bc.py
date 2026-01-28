code = """import json, re
import pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

biz = load_records(var_call_aDTor3rVtWKCnZdlGqBeokT5)
rev = load_records(var_call_OWvNFzatYMzoHgYYRe3nOaXy)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

state_pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = state_pat.findall(desc)
    return matches[-1] if matches else None

dfb['state'] = dfb.get('description', pd.Series([None]*len(dfb))).map(extract_state)
dfb['review_count'] = pd.to_numeric(dfb.get('review_count'), errors='coerce')

dfr['rating'] = pd.to_numeric(dfr.get('rating'), errors='coerce')

def to_businessref(businessid):
    if not isinstance(businessid, str):
        return None
    return businessid.replace('businessid_', 'businessref_', 1)

dfb['business_ref'] = dfb.get('business_id', pd.Series([None]*len(dfb))).map(to_businessref)

state_totals = dfb.dropna(subset=['state','review_count'])
if len(state_totals)==0:
    out = {'error':'Could not derive state totals from business descriptions.'}
else:
    state_totals = state_totals.groupby('state', as_index=False)['review_count'].sum().sort_values(['review_count','state'], ascending=[False, True])
    top_state = state_totals.iloc[0]['state']
    top_state_total_reviews = float(state_totals.iloc[0]['review_count'])

    biz_ratings = dfr.dropna(subset=['business_ref','rating']).groupby('business_ref', as_index=False)['rating'].mean().rename(columns={'rating':'business_avg_rating'})
    df_top = dfb[dfb['state']==top_state][['business_ref']].dropna().drop_duplicates()
    merged = df_top.merge(biz_ratings, on='business_ref', how='left').dropna(subset=['business_avg_rating'])
    state_business_avg_rating = None if len(merged)==0 else float(merged['business_avg_rating'].mean())

    out = {
        'state': top_state,
        'total_reviews_in_state': int(top_state_total_reviews) if top_state_total_reviews.is_integer() else top_state_total_reviews,
        'average_business_rating_in_state': None if state_business_avg_rating is None else round(state_business_avg_rating, 4)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aDTor3rVtWKCnZdlGqBeokT5': 'file_storage/call_aDTor3rVtWKCnZdlGqBeokT5.json', 'var_call_OWvNFzatYMzoHgYYRe3nOaXy': 'file_storage/call_OWvNFzatYMzoHgYYRe3nOaXy.json'}

exec(code, env_args)
