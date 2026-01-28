code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_doarPlbi5gmmAmwXzflue43q, 'r') as f:
    businesses = json.load(f)
with open(var_call_4Qk0cvzCIYKacF9lDPqlq60F, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
# Ensure business_id and description exist
df_b = df_b[['business_id', 'description']].dropna()

# Extract state from description using regex
states = []
pattern = re.compile(r",\s*([A-Z]{2})(?:,|\b)")
for desc in df_b['description']:
    m = pattern.search(desc)
    if m:
        states.append(m.group(1))
    else:
        states.append(None)

df_b['state'] = states
# Drop rows without state
df_b = df_b.dropna(subset=['state']).copy()

# Load reviews into DataFrame
df_r = pd.DataFrame(reviews)
# Convert rating to numeric
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
# Map business_ref to business_id (prefix change)
if 'business_ref' in df_r.columns:
    df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_')

# Join reviews with businesses to get state for each review
df_join = pd.merge(df_r, df_b[['business_id','state']], on='business_id', how='left')
# Drop reviews with no state mapping
df_join = df_join.dropna(subset=['state']).copy()

# Group by state: count reviews and average rating
grp = df_join.groupby('state').agg(total_reviews=('rating','count'), average_rating=('rating','mean')).reset_index()

# Find state with max reviews
if grp.shape[0] == 0:
    result = {'state': None, 'total_reviews': 0, 'average_rating': None}
else:
    top = grp.sort_values('total_reviews', ascending=False).iloc[0]
    result = {'state': top['state'], 'total_reviews': int(top['total_reviews']), 'average_rating': float(top['average_rating'])}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_doarPlbi5gmmAmwXzflue43q': 'file_storage/call_doarPlbi5gmmAmwXzflue43q.json', 'var_call_4Qk0cvzCIYKacF9lDPqlq60F': 'file_storage/call_4Qk0cvzCIYKacF9lDPqlq60F.json'}

exec(code, env_args)
