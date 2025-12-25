code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_NQDXevD9lhHUqEi7ItoVrUhh, 'r') as f:
    business_data = json.load(f)
with open(var_call_H08v7eYAAKC28ADSQOKm6Ez9, 'r') as f:
    review_data = json.load(f)

# Extract state from description, assuming pattern like ", XX" where XX is state code before ZIP or city
state_pattern = re.compile(r',\s*([A-Z]{2})[\s,]')

biz_records = []
for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    biz_id = b['business_id']
    # map businessid_# to businessref_#
    biz_ref = 'businessref_' + biz_id.split('_',1)[1]
    biz_records.append({'business_ref': biz_ref, 'state': state})

biz_df = pd.DataFrame(biz_records)
rev_df = pd.DataFrame(review_data)
rev_df['rating'] = pd.to_numeric(rev_df['rating'])

# join reviews with business states
merged = rev_df.merge(biz_df, on='business_ref', how='inner')

# compute total reviews and average rating per state
state_stats = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# find state with max reviews
max_row = state_stats.sort_values('review_count', ascending=False).iloc[0]
result = {
    'state': max_row['state'],
    'total_reviews': int(max_row['review_count']),
    'average_rating': round(float(max_row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NQDXevD9lhHUqEi7ItoVrUhh': 'file_storage/call_NQDXevD9lhHUqEi7ItoVrUhh.json', 'var_call_H08v7eYAAKC28ADSQOKm6Ez9': 'file_storage/call_H08v7eYAAKC28ADSQOKm6Ez9.json'}

exec(code, env_args)
