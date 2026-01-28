code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business = load(var_call_wFB96nMbTQEmmYp5NBX1WEjy)
reviews = load(var_call_dVBhWgXVvikQHQ7OhGQ5uGcP)

dfb = pd.DataFrame(business)
if 'review_count' in dfb.columns:
    dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce').fillna(0).astype(int)

# extract state as last ', ST' in description
state_re = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    ms = state_re.findall(desc)
    if ms:
        return ms[-1]
    return None

dfb['state'] = dfb['description'].apply(extract_state) if 'description' in dfb.columns else None

dfb_valid = dfb.dropna(subset=['state'])
state_totals = dfb_valid.groupby('state')['review_count'].sum().sort_values(ascending=False)

if state_totals.empty:
    out = {'error':'Could not extract any state from business.description'}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    top_state = state_totals.index[0]
    dfr = pd.DataFrame(reviews)
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
    suffix = dfr['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
    dfr['business_id'] = 'businessid_' + suffix
    biz_in_state = set(dfb_valid.loc[dfb_valid['state']==top_state, 'business_id'].astype(str))
    avg_rating = dfr.loc[dfr['business_id'].isin(biz_in_state), 'rating'].mean()
    result = {
        'state': top_state,
        'total_reviews': int(state_totals.loc[top_state]),
        'average_business_rating': None if pd.isna(avg_rating) else float(avg_rating)
    }
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_call_wFB96nMbTQEmmYp5NBX1WEjy': 'file_storage/call_wFB96nMbTQEmmYp5NBX1WEjy.json', 'var_call_dVBhWgXVvikQHQ7OhGQ5uGcP': 'file_storage/call_dVBhWgXVvikQHQ7OhGQ5uGcP.json'}

exec(code, env_args)
