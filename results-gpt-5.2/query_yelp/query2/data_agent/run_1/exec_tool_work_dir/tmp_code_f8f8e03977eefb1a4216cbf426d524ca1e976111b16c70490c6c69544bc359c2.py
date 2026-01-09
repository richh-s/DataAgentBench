code = """import json, re, pandas as pd
path = var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ
with open(path, 'r', encoding='utf-8') as f:
    biz = json.load(f)

def parse_state(desc):
    if not desc:
        return None
    m = re.search(r"\b([A-Z]{2})\b", desc)
    if not m:
        return None
    # better: state appears after last comma before 'this' sometimes; but simple match ok.
    # restrict to US states list
    states = {
        'AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'
    }
    # choose first match that is a state
    for mm in re.finditer(r"\b([A-Z]{2})\b", desc):
        st = mm.group(1)
        if st in states:
            return st
    return None

rows=[]
for r in biz:
    st = parse_state(r.get('description'))
    rc = r.get('review_count')
    try:
        rc_i = int(rc)
    except Exception:
        rc_i = None
    stars = r.get('stars')
    try:
        stars_f = float(stars) if stars is not None else None
    except Exception:
        stars_f = None
    rows.append({'state': st, 'review_count': rc_i, 'stars': stars_f})

df = pd.DataFrame(rows)
df = df.dropna(subset=['state','review_count'])
state_reviews = df.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
top = state_reviews.iloc[0].to_dict() if len(state_reviews) else None
if top is None:
    out = {'error':'no data'}
else:
    top_state = top['state']
    # average rating of businesses in that state; use stars if exists else compute from review table (not available)
    avg_rating = None
    if 'stars' in df.columns and df['stars'].notna().any():
        avg_rating = float(df.loc[df.state==top_state, 'stars'].dropna().mean()) if df.loc[df.state==top_state,'stars'].dropna().shape[0]>0 else None
    out = {'state': top_state, 'total_reviews': int(top['review_count']), 'avg_business_rating': avg_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json', 'var_call_2KcQNtpgWpdSy1Ok7ZD7VufB': [{'ok': '1'}]}

exec(code, env_args)
