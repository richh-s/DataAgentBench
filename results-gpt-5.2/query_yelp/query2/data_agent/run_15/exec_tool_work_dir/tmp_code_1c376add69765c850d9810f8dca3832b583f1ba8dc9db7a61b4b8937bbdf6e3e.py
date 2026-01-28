code = """import json, re, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

biz = load_records(var_call_AYyXv9LsIzsqcL0IvI0qZ9In)
rev = load_records(var_call_mvUTq4R7LE2uFfV6ZMMwzuo4)

biz_df = pd.DataFrame(biz)
rev_df = pd.DataFrame(rev)

# parse state from description like ' in City, ST,' or ' in City, ST location'
pat = re.compile(r'\b([A-Z][A-Za-z .\'\-]+),\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = pat.search(desc)
    if m:
        return m.group(2)
    return None

biz_df['state'] = biz_df['description'].map(extract_state)

# review_count in sample appears as string
biz_df['review_count'] = pd.to_numeric(biz_df['review_count'], errors='coerce')

state_reviews = biz_df.groupby('state', dropna=True)['review_count'].sum().sort_values(ascending=False)

top_state = state_reviews.index[0]

top_state_biz = biz_df.loc[biz_df['state']==top_state, ['business_id']].copy()

# map business_id -> business_ref
# businessid_123 -> businessref_123

def id_to_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_', 1)

top_state_biz['business_ref'] = top_state_biz['business_id'].map(id_to_ref)

rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

merged = rev_df.merge(top_state_biz[['business_ref']], on='business_ref', how='inner')
avg_rating = float(merged['rating'].mean()) if len(merged) else None

a = {
    'state': top_state,
    'total_reviews_business_metadata_sum_review_count': int(state_reviews.loc[top_state]) if pd.notna(state_reviews.loc[top_state]) else None,
    'average_rating_from_reviews_table': round(avg_rating, 4) if avg_rating is not None else None,
    'num_reviews_rows_used_for_avg': int(merged['rating'].notna().sum())
}

print('__RESULT__:')
print(json.dumps(a))"""

env_args = {'var_call_AYyXv9LsIzsqcL0IvI0qZ9In': 'file_storage/call_AYyXv9LsIzsqcL0IvI0qZ9In.json', 'var_call_mvUTq4R7LE2uFfV6ZMMwzuo4': 'file_storage/call_mvUTq4R7LE2uFfV6ZMMwzuo4.json'}

exec(code, env_args)
