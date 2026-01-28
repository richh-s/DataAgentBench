code = """import json, re, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

business = load(var_call_wFB96nMbTQEmmYp5NBX1WEjy)
reviews = load(var_call_dVBhWgXVvikQHQ7OhGQ5uGcP)

dfb = pd.DataFrame(business)
# normalize types
if 'review_count' in dfb.columns:
    dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce').fillna(0).astype(int)

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r'\b([A-Z]{2})\b', desc)
    # better: find pattern ' in City, ST' or 'City, ST'
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

dfb['state'] = dfb.get('description', pd.Series([None]*len(dfb))).apply(extract_state)

# total reviews per state from business.review_count
state_totals = dfb.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)

top_state = state_totals.index[0]

dfr = pd.DataFrame(reviews)
dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')
# map businessref_N -> businessid_N
# extract suffix after last underscore
suffix = dfr['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
dfr['business_id'] = 'businessid_' + suffix

# businesses in top_state
biz_in_state = set(dfb.loc[dfb['state']==top_state, 'business_id'].astype(str))

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
