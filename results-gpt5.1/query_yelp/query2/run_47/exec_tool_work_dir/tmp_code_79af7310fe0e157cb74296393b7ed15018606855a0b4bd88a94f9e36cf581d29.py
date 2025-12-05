code = """import json, pandas as pd, re

# Load full results from files
with open(var_call_1Xzw2YX1Zbw62fFcAdAcNbM7, 'r') as f:
    business_records = json.load(f)
with open(var_call_Gb4FxZP3RmtJN0YBKfPkSNpK, 'r') as f:
    review_records = json.load(f)

# Create DataFrames
df_bus = pd.DataFrame(business_records)
df_rev = pd.DataFrame(review_records)

# Extract state abbreviation from description (assumes pattern 'City, ST')
state_pattern = re.compile(r',\s*([A-Z]{2})\b')

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    return m.group(1) if m else None

df_bus['state'] = df_bus['description'].apply(extract_state)

# Map business_ref to business_id: businessref_XX -> businessid_XX
# First get mapping businessid_XX -> state
df_bus['suffix'] = df_bus['business_id'].str.replace('businessid_', '', regex=False)

# For reviews, derive matching business_id and join to states
df_rev['suffix'] = df_rev['business_ref'].str.replace('businessref_', '', regex=False)

# Join on suffix
state_map = df_bus[['suffix', 'state']]
df = pd.merge(df_rev, state_map, on='suffix', how='left')

# Ensure rating numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Group by state: count reviews and average rating
state_stats = df.dropna(subset=['state', 'rating']).groupby('state').agg(
    review_count=('rating', 'size'),
    avg_rating=('rating', 'mean')
).reset_index()

# Find state with max reviews
if state_stats.empty:
    result = {"state": None, "review_count": 0, "avg_rating": None}
else:
    top = state_stats.sort_values('review_count', ascending=False).iloc[0]
    result = {
        'state': top['state'],
        'review_count': int(top['review_count']),
        'avg_rating': round(float(top['avg_rating']), 3)
    }

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1Xzw2YX1Zbw62fFcAdAcNbM7': 'file_storage/call_1Xzw2YX1Zbw62fFcAdAcNbM7.json', 'var_call_Gb4FxZP3RmtJN0YBKfPkSNpK': 'file_storage/call_Gb4FxZP3RmtJN0YBKfPkSNpK.json'}

exec(code, env_args)
