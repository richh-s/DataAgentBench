code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_Bxs950sZ5rio9iVFYpZeb92a, 'r') as f:
    business_data = json.load(f)
with open(var_call_PKusBbTTfo6UnBTeje8wlkuZ, 'r') as f:
    review_data = json.load(f)

# Extract state from description using regex like ", XX" or "City, XX" or standalone "XX" before country/end
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

rows = []
for b in business_data:
    desc = b.get('description') or ''
    m = state_pattern.search(desc)
    if not m:
        continue
    state = m.group(1)
    rows.append({'business_id': b['business_id'], 'state': state})

biz_df = pd.DataFrame(rows)

# Map business_ref -> business_id
# businessid_XX corresponds to businessref_XX
review_rows = []
for r in review_data:
    bref = r['business_ref']
    num = bref.replace('businessref_', '')
    bid = 'businessid_' + num
    review_rows.append({'business_id': bid, 'rating': int(r['rating'])})

rev_df = pd.DataFrame(review_rows)

# Join reviews with business states
merged = rev_df.merge(biz_df, on='business_id', how='inner')

# Aggregate by state
agg = merged.groupby('state').agg(review_count=('rating', 'size'), avg_rating=('rating', 'mean')).reset_index()

# Find state with highest number of reviews
top = agg.sort_values(['review_count', 'state'], ascending=[False, True]).iloc[0]

result = {
    'state': top['state'],
    'review_count': int(top['review_count']),
    'average_rating': round(float(top['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Bxs950sZ5rio9iVFYpZeb92a': 'file_storage/call_Bxs950sZ5rio9iVFYpZeb92a.json', 'var_call_PKusBbTTfo6UnBTeje8wlkuZ': 'file_storage/call_PKusBbTTfo6UnBTeje8wlkuZ.json'}

exec(code, env_args)
