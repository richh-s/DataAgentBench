code = """import json, re, pandas as pd

# Load full results (may be file paths)

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

biz = load_records(var_call_oKBjiky7ugl5mkFZxoSM4UOy)
rev = load_records(var_call_1owFHRVlFVEdG6D1fY6LjENE)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# Extract 2-letter state code from description like "in City, ST" or "City, ST," or "City, ST location"
pat = re.compile(r'\bin\s+[A-Za-z .\-]+,\s*([A-Z]{2})\b')

def get_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.search(desc)
    return m.group(1) if m else None

biz_df['state'] = biz_df['description'].map(get_state)

# Ensure numeric review_count
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce').fillna(0).astype(int)

# Sum review_count by state to find state with highest number of reviews
state_reviews = biz_df.dropna(subset=['state']).groupby('state', as_index=False)['review_count'].sum()

top_row = state_reviews.sort_values(['review_count','state'], ascending=[False, True]).head(1)
if top_row.empty:
    out = {"state": None, "total_reviews": 0, "average_business_rating": None}
else:
    top_state = top_row.iloc[0]['state']
    total_reviews = int(top_row.iloc[0]['review_count'])

    # Join reviews to businesses in that state (map businessref_ -> businessid_)
    # Extract numeric suffix
    biz_df['suffix'] = biz_df['business_id'].str.replace('businessid_', '', regex=False)
    rev_df['suffix'] = rev_df['business_ref'].str.replace('businessref_', '', regex=False)

    merged = rev_df.merge(biz_df[biz_df['state'] == top_state][['suffix']], on='suffix', how='inner')
    merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')
    avg_rating = float(merged['rating'].mean()) if len(merged) else None

    out = {"state": top_state, "total_reviews": total_reviews, "average_business_rating": (None if avg_rating is None else round(avg_rating, 4))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oKBjiky7ugl5mkFZxoSM4UOy': 'file_storage/call_oKBjiky7ugl5mkFZxoSM4UOy.json', 'var_call_1owFHRVlFVEdG6D1fY6LjENE': 'file_storage/call_1owFHRVlFVEdG6D1fY6LjENE.json'}

exec(code, env_args)
