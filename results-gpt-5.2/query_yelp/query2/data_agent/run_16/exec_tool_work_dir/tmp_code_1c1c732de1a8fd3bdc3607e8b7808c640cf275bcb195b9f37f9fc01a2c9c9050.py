code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

biz = load_records(var_call_NFEvdMmwAZrZR9o392X4YuFv)
rev = load_records(var_call_S7DU8KadOMgbH0YSvnrEUPHf)

dfb = pd.DataFrame(biz)
dfr = pd.DataFrame(rev)

pat = re.compile(r"\bin\s+[^,]+,\s*([A-Z]{2})\b")
dfb['state'] = dfb['description'].astype(str).str.extract(pat, expand=False)
dfb['review_count'] = pd.to_numeric(dfb['review_count'], errors='coerce')

state_reviews = dfb.dropna(subset=['state','review_count']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    out = {'state': None, 'total_review_count': None, 'average_rating': None}
else:
    state_top = state_reviews.sort_values('review_count', ascending=False).head(1)
    top_state = state_top.iloc[0]['state']
    total_reviews = int(state_top.iloc[0]['review_count'])

    dfr['business_id'] = dfr['business_ref'].astype(str).str.replace('businessref_','businessid_', regex=False)
    dfr['rating'] = pd.to_numeric(dfr['rating'], errors='coerce')

    joined = dfr.merge(dfb[['business_id','state']], on='business_id', how='inner')
    state_joined = joined[(joined['state']==top_state)].dropna(subset=['rating'])
    avg_rating = float(state_joined['rating'].mean()) if len(state_joined) else None

    out = {
        'state': top_state,
        'total_review_count': total_reviews,
        'average_rating': None if avg_rating is None else round(avg_rating, 4)
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NFEvdMmwAZrZR9o392X4YuFv': 'file_storage/call_NFEvdMmwAZrZR9o392X4YuFv.json', 'var_call_S7DU8KadOMgbH0YSvnrEUPHf': 'file_storage/call_S7DU8KadOMgbH0YSvnrEUPHf.json'}

exec(code, env_args)
