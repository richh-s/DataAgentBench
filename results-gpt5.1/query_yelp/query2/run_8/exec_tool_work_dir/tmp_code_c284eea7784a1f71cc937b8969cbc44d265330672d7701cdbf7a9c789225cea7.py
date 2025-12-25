code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_MS8qm5fkTDbVcbGUzz2lcAo2, 'r') as f:
    business_data = json.load(f)
with open(var_call_t8poD59fT2UqBUW2T4w6w68o, 'r') as f:
    review_data = json.load(f)

# Extract state from description using regex looking for ', XX' where XX is 2 uppercase letters
state_pattern = re.compile(r',\s*([A-Z]{2})[\s,]')

biz_rows = []
for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    state = m.group(1) if m else None
    biz_rows.append({'business_id': b['business_id'], 'state': state})

biz_df = pd.DataFrame(biz_rows)

# Map business_ref to business_id by replacing prefix
rev_df = pd.DataFrame(review_data)
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'])

# Merge reviews with business states
merged = rev_df.merge(biz_df, on='business_id', how='left')

# Drop rows without a state
merged = merged.dropna(subset=['state'])

# Compute total review counts per state and average rating
state_stats = merged.groupby('state').agg(
    review_count=('rating', 'size'),
    avg_rating=('rating', 'mean')
).reset_index()

# Find state with highest number of reviews
top = state_stats.sort_values('review_count', ascending=False).iloc[0]

result = {
    'state_with_most_reviews': top['state'],
    'number_of_reviews': int(top['review_count']),
    'average_rating_in_state': round(float(top['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_MS8qm5fkTDbVcbGUzz2lcAo2': 'file_storage/call_MS8qm5fkTDbVcbGUzz2lcAo2.json', 'var_call_t8poD59fT2UqBUW2T4w6w68o': 'file_storage/call_t8poD59fT2UqBUW2T4w6w68o.json'}

exec(code, env_args)
