code = """import json, re, pandas as pd

# Load full results from files
with open(var_call_f7fdarCrZpeM5z65nIxcoNCC, 'r') as f:
    business_data = json.load(f)
with open(var_call_CG3ZySBTjUiAP0WUxrLqqKzy, 'r') as f:
    review_data = json.load(f)

bdf = pd.DataFrame(business_data)
rdf = pd.DataFrame(review_data)

# Extract state abbreviation from description using common pattern ' City, ST' or ' in City, ST,' etc.
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for ', ST' where ST is two uppercase letters
    m = re.search(r',\s*([A-Z]{2})\b', desc)
    if m:
        return m.group(1)
    return None

bdf['state'] = bdf['description'].apply(extract_state)

# Map business_id -> state
b_state = bdf[['business_id', 'state']].dropna()

# Normalize IDs: businessid_X -> X, businessref_X -> X
b_state['key'] = b_state['business_id'].str.replace('businessid_', '', regex=False)

rdf['key'] = rdf['business_ref'].str.replace('businessref_', '', regex=False)

# Merge reviews with state info
merged = rdf.merge(b_state[['key', 'state']], on='key', how='inner')

# Ensure rating numeric
merged['rating'] = pd.to_numeric(merged['rating'])

# Aggregate by state
agg = merged.groupby('state').agg(review_count=('rating', 'size'), avg_rating=('rating', 'mean')).reset_index()

# Get state with max review_count
idx = agg['review_count'].idxmax()
row = agg.loc[idx]

result = {
    'state': row['state'],
    'review_count': int(row['review_count']),
    'average_rating': round(float(row['avg_rating']), 3)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_f7fdarCrZpeM5z65nIxcoNCC': 'file_storage/call_f7fdarCrZpeM5z65nIxcoNCC.json', 'var_call_CG3ZySBTjUiAP0WUxrLqqKzy': 'file_storage/call_CG3ZySBTjUiAP0WUxrLqqKzy.json'}

exec(code, env_args)
