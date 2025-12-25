code = """import json, pandas as pd, re

# Load full results from files
with open(var_call_ihqx03l2OCdcJJmYygmjcHMn, 'r') as f:
    business_data = json.load(f)
with open(var_call_3oen0i3AsCfxSqBXIh6sPscE, 'r') as f:
    review_data = json.load(f)

biz_df = pd.DataFrame(business_data)
rev_df = pd.DataFrame(review_data)

# Extract state from description, assuming pattern like ', XX,' or ', XX ' before ZIP
state_pattern = re.compile(r',\s*([A-Z]{2})\s*(?:\d{5})?[, ]')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    # Also handle leading 'This CITY, ST ' pattern
    m = re.search(r'\b([A-Z][a-zA-Z]+),\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(2)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Map business_ref to business_id using numeric suffix
rev_df['num'] = rev_df['business_ref'].str.replace('businessref_', '', regex=False)

biz_df['num'] = biz_df['business_id'].str.replace('businessid_', '', regex=False)

merged = pd.merge(rev_df, biz_df[['num','state']], on='num', how='left')

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'])

state_group = merged.dropna(subset=['state']).groupby('state').agg(
    review_count=('rating','size'),
    avg_rating=('rating','mean')
).reset_index()

# Find state with max review_count
idx = state_group['review_count'].idxmax()
row = state_group.loc[idx]

result = {
    'state_with_most_reviews': row['state'],
    'number_of_reviews': int(row['review_count']),
    'average_rating_in_state': round(float(row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_ihqx03l2OCdcJJmYygmjcHMn': 'file_storage/call_ihqx03l2OCdcJJmYygmjcHMn.json', 'var_call_3oen0i3AsCfxSqBXIh6sPscE': 'file_storage/call_3oen0i3AsCfxSqBXIh6sPscE.json'}

exec(code, env_args)
