code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_oKBjiky7ugl5mkFZxoSM4UOy)
rev = load_records(var_call_1owFHRVlFVEdG6D1fY6LjENE)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

# Match " in City, ST" optionally followed by punctuation
pat_in = re.compile(r'\bin\s+[^,]+,\s*([A-Z]{2})\b')
pat_comma = re.compile(r',\s*([A-Z]{2})\b')


def get_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat_in.search(desc)
    if m and m.group(1) in states:
        return m.group(1)
    ms = pat_comma.findall(desc)
    for s in reversed(ms):
        if s in states:
            return s
    return None

biz_df['state'] = biz_df['description'].map(get_state)

biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)
state_reviews = biz_df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

if state_reviews.empty:
    out = {"state": None, "total_reviews": 0, "average_business_rating": None}
else:
    top = state_reviews.sort_values(['review_count','state'], ascending=[False, True]).iloc[0]
    top_state = top['state']
    total_reviews = int(top['review_count'])

    biz_df['suffix'] = biz_df['business_id'].str.replace('businessid_', '', regex=False)
    rev_df['suffix'] = rev_df['business_ref'].str.replace('businessref_', '', regex=False)
    merged = rev_df.merge(biz_df[biz_df['state']==top_state][['suffix']], on='suffix', how='inner')
    merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')
    avg_rating = float(merged['rating'].mean()) if len(merged) else None

    out = {"state": top_state, "total_reviews": total_reviews, "average_business_rating": (None if avg_rating is None else round(avg_rating, 4))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oKBjiky7ugl5mkFZxoSM4UOy': 'file_storage/call_oKBjiky7ugl5mkFZxoSM4UOy.json', 'var_call_1owFHRVlFVEdG6D1fY6LjENE': 'file_storage/call_1owFHRVlFVEdG6D1fY6LjENE.json', 'var_call_hHZLfBDcqG1GOuqkmlZAbZME': {'state': None, 'total_reviews': 0, 'average_business_rating': None}, 'var_call_hWIswGR6JexBKJm2uT8dk34M': {'null': 100}, 'var_call_em0ji9mGJmgNWzilPIMBJPkK': 'file_storage/call_em0ji9mGJmgNWzilPIMBJPkK.json'}

exec(code, env_args)
