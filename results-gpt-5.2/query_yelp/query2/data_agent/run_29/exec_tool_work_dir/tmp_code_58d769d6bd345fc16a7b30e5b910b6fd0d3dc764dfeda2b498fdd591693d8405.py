code = """import json, re, pandas as pd

def load_records(maybe_path):
    if isinstance(maybe_path, str) and maybe_path.endswith('.json'):
        with open(maybe_path, 'r') as f:
            return json.load(f)
    return maybe_path

biz = load_records(var_call_dxH3ZaVrO5kpAUXl7q603S3X)
rev = load_records(var_call_hCyjCZ7GLM4nSogB9BTRfbJm)

biz_df = pd.DataFrame(biz)
# parse state from description: last ', ST' before end (allow trailing text)
state_pat = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = list(state_pat.finditer(desc))
    if not m:
        return None
    # choose last occurrence; often city, ST
    return m[-1].group(1)

biz_df['state'] = biz_df['description'].map(extract_state)
# normalize types
biz_df['review_count'] = pd.to_numeric(biz_df.get('review_count'), errors='coerce').fillna(0).astype(int)

# total reviews by state using business.review_count
state_totals = biz_df.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)

top_state = state_totals.index[0]

top_total_reviews = int(state_totals.iloc[0])

# average rating of businesses in that state based on review table ratings
rev_df = pd.DataFrame(rev)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
# map businessref_# -> businessid_#
rev_df['business_id'] = rev_df['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)

# join reviews to biz state
joined = rev_df.merge(biz_df[['business_id','state']], on='business_id', how='left')

avg_rating_top_state = joined.loc[joined['state']==top_state, 'rating'].mean()

out = {
    'state': top_state,
    'total_reviews': top_total_reviews,
    'average_rating': None if pd.isna(avg_rating_top_state) else float(round(avg_rating_top_state, 4))
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dxH3ZaVrO5kpAUXl7q603S3X': 'file_storage/call_dxH3ZaVrO5kpAUXl7q603S3X.json', 'var_call_hCyjCZ7GLM4nSogB9BTRfbJm': 'file_storage/call_hCyjCZ7GLM4nSogB9BTRfbJm.json'}

exec(code, env_args)
