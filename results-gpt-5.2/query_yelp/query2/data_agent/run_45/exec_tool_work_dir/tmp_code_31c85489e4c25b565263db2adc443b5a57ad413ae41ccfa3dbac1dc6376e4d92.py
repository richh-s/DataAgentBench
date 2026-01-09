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

us_states = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])

# stricter regex: ', ST,' or ', ST ' or ', ST.'
state_re = re.compile(r',\s*([A-Z]{2})(?=\s*(?:,|\.|\b))')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = state_re.findall(desc)
    for s in reversed(matches):
        if s in us_states:
            return s
    return None

biz_df['state'] = biz_df['description'].map(extract_state)

# debug counts
state_nonnull = int(biz_df['state'].notna().sum())

biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce').fillna(0).astype(int)
state_reviews = biz_df.dropna(subset=['state']).groupby('state')['review_count'].sum().sort_values(ascending=False)

out = {'state_parse_nonnull_businesses': state_nonnull, 'states_found': list(state_reviews.index[:10])}
if not state_reviews.empty:
    out['top_state'] = state_reviews.index[0]
    out['top_state_total_reviews'] = int(state_reviews.iloc[0])

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0K6EcTcadeFmPEh43zGf9oGi': 'file_storage/call_0K6EcTcadeFmPEh43zGf9oGi.json', 'var_call_oqb0AsdwVa0oyoU3WykFgu8K': 'file_storage/call_oqb0AsdwVa0oyoU3WykFgu8K.json', 'var_call_iPyuOUoZtwR9cJ7bNZF6BOho': {'error': 'Could not extract any state from business.description'}, 'var_call_dCcGZJmcThQQJULUYD2PFYXe': 'file_storage/call_dCcGZJmcThQQJULUYD2PFYXe.json'}

exec(code, env_args)
