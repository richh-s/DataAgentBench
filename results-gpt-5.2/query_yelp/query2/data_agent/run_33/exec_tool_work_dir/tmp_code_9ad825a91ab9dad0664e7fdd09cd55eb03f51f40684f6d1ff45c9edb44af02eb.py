code = """import json, re, pandas as pd
from pathlib import Path

# load full business collection extract
p = Path(var_call_HyyvRxS3PLqxHpN0DQ9tGJtw)
records = json.loads(p.read_text())

df = pd.DataFrame(records)
# coerce review_count numeric
if 'review_count' in df.columns:
    df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce').fillna(0).astype(int)

# extract state from description using ', XX' pattern
pat = re.compile(r",\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.search(desc)
    return m.group(1) if m else None

df['state'] = df['description'].apply(extract_state)

df2 = df.dropna(subset=['state'])

# total reviews by state
state_reviews = df2.groupby('state', as_index=False)['review_count'].sum().sort_values('review_count', ascending=False)
if len(state_reviews)==0:
    out = {"state": None, "total_reviews": 0, "avg_rating_businesses_in_state": None}
else:
    top_state = state_reviews.iloc[0]['state']
    total_reviews = int(state_reviews.iloc[0]['review_count'])
    # avg rating: use 'stars' if present, else approximate from review table not available here
    avg_rating = None
    if 'stars' in df2.columns and df2['stars'].notna().any():
        avg_rating = float(pd.to_numeric(df2.loc[df2['state']==top_state,'stars'], errors='coerce').mean())
    out = {"state": top_state, "total_reviews": total_reviews, "avg_rating_businesses_in_state": (None if avg_rating is None or pd.isna(avg_rating) else round(avg_rating,4))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_HyyvRxS3PLqxHpN0DQ9tGJtw': 'file_storage/call_HyyvRxS3PLqxHpN0DQ9tGJtw.json', 'var_call_4sSC9KgC6JHii0hyJlyKW58q': [{'ok': '1'}]}

exec(code, env_args)
