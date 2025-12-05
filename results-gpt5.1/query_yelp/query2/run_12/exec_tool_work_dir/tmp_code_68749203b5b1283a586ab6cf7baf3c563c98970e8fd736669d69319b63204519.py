code = """import json, pandas as pd, re

# Load full results from files
with open(var_call_c5BruYoMx792ij1Yi8Yxxz2d, 'r') as f:
    business_data = json.load(f)
with open(var_call_u3pqfVKoJtqLjaBYzIeXCyLg, 'r') as f:
    review_data = json.load(f)

biz_df = pd.DataFrame(business_data)
rev_df = pd.DataFrame(review_data)

# Extract state abbreviation from description using regex pattern like ', XX,' or ', XX ' before ZIP
# We'll look for ', XX ' where XX are 2 uppercase letters
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Map business_id to state
biz_state = biz_df[['business_id','state']].dropna()

# Normalize IDs: businessid_# -> businessref_#
rev_df['business_id'] = rev_df['business_ref'].str.replace('businessref_','businessid_', regex=False)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Merge reviews with business states
merged = rev_df.merge(biz_state, on='business_id', how='inner')

# Aggregate reviews per state
state_group = merged.groupby('state').agg(review_count=('rating','size'), avg_rating=('rating','mean')).reset_index()

# Find state with max reviews
top = state_group.sort_values('review_count', ascending=False).iloc[0]
result = {
    'state': top['state'],
    'review_count': int(top['review_count']),
    'average_rating': round(float(top['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_c5BruYoMx792ij1Yi8Yxxz2d': 'file_storage/call_c5BruYoMx792ij1Yi8Yxxz2d.json', 'var_call_u3pqfVKoJtqLjaBYzIeXCyLg': 'file_storage/call_u3pqfVKoJtqLjaBYzIeXCyLg.json'}

exec(code, env_args)
