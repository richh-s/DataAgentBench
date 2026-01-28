code = """import json, re
import pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_0FCafEWNzDCyxFVfMTQjn1fl)
rev = load_records(var_call_d2B8rtRoEAk1d7rH7WdBrch3)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

# parse state from description: last occurrence of ', XX' where XX is 2-letter state code
pat = re.compile(r',\s*([A-Z]{2})\b')
def get_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.findall(desc)
    return m[-1] if m else None

dfb['state'] = dfb['description'].map(get_state)
# normalize types
for c in ['review_count']:
    dfb[c] = pd.to_numeric(dfb[c], errors='coerce')

dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

# total reviews by state from business metadata
state_reviews = dfb.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()
if state_reviews.empty:
    out = {"error":"No state/review_count data parsed"}
else:
    top_state = state_reviews.sort_values('review_count', ascending=False).iloc[0]['state']

    # map businessref -> businessid
    dfr['business_id'] = dfr['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

    # join reviews to businesses in that state and compute avg rating (across reviews)
    df_join = dfr.merge(dfb[['business_id','state']], on='business_id', how='inner')
    avg_rating = df_join.loc[df_join['state']==top_state, 'rating'].mean()

    total_reviews = float(state_reviews.loc[state_reviews['state']==top_state, 'review_count'].iloc[0])

    out = {
        "state": top_state,
        "total_review_count_sum": int(total_reviews),
        "average_rating_in_state": None if pd.isna(avg_rating) else float(avg_rating)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0FCafEWNzDCyxFVfMTQjn1fl': 'file_storage/call_0FCafEWNzDCyxFVfMTQjn1fl.json', 'var_call_d2B8rtRoEAk1d7rH7WdBrch3': 'file_storage/call_d2B8rtRoEAk1d7rH7WdBrch3.json'}

exec(code, env_args)
