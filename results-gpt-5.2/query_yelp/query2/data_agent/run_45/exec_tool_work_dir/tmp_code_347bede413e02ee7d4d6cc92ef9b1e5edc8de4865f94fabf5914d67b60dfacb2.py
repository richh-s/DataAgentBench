code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_0K6EcTcadeFmPEh43zGf9oGi)
rev = load_records(var_call_oqb0AsdwVa0oyoU3WykFgu8K)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# parse state abbreviation from description: look for ", ST," pattern
state_re = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if desc is None:
        return None
    m = state_re.findall(desc)
    if not m:
        return None
    # choose last 2-letter token; filter to US states list
    return m[-1]

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

biz_df['state'] = biz_df['description'].map(extract_state)
biz_df.loc[~biz_df['state'].isin(us_states), 'state'] = None
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)

state_reviews = biz_df.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)
top_state = state_reviews.index[0]
top_state_total_reviews = int(state_reviews.iloc[0])

# map businessref_* -> businessid_*
rev_df['biz_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

biz_state_map = biz_df[['business_id','state']].dropna().drop_duplicates()
merged = rev_df.merge(biz_state_map, left_on='biz_id', right_on='business_id', how='inner')

avg_rating_top_state = float(merged.loc[merged['state']==top_state, 'rating'].mean())

out = {
    'state': top_state,
    'total_reviews_in_state': top_state_total_reviews,
    'average_business_rating_in_state': round(avg_rating_top_state, 4)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0K6EcTcadeFmPEh43zGf9oGi': 'file_storage/call_0K6EcTcadeFmPEh43zGf9oGi.json', 'var_call_oqb0AsdwVa0oyoU3WykFgu8K': 'file_storage/call_oqb0AsdwVa0oyoU3WykFgu8K.json'}

exec(code, env_args)
