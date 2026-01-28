code = """import json
import re
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_zbZVBzAf6L1maBUDhJpN84JT, 'r') as f:
    business_docs = json.load(f)
with open(var_call_HtUP2QtCM4W2py1nVbQumg46, 'r') as f:
    review_rows = json.load(f)

# Create DataFrame for businesses
df_biz = pd.DataFrame(business_docs)
# Extract state from description using regex
# Pattern looks for a comma, space, two uppercase letters, then a comma (e.g., ", CA,")
state_pattern = re.compile(r",\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_pattern.search(desc)
    if m:
        return m.group(1)
    return None

df_biz['state'] = df_biz['description'].apply(extract_state)
# Create mapping from business_id to state
biz_state_map = dict(zip(df_biz['business_id'], df_biz['state']))

# Create DataFrame for reviews
df_rev = pd.DataFrame(review_rows)
# Ensure rating is numeric
# Some ratings may be strings; coerce to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
# Map business_ref to business_id by replacing prefix
# businessref_1 -> businessid_1
df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
# Map to state
df_rev['state'] = df_rev['business_id'].map(biz_state_map)
# Drop reviews without a mapped state
df_rev_mapped = df_rev.dropna(subset=['state']).copy()

# Compute review counts per state
state_counts = df_rev_mapped.groupby('state').size().rename('review_count')
if state_counts.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    top_state = state_counts.idxmax()
    top_count = int(state_counts.max())
    # Compute average rating for reviews in that state
    avg_rating = float(df_rev_mapped.loc[df_rev_mapped['state'] == top_state, 'rating'].mean())
    # Round to 3 decimal places for clarity
    avg_rating = round(avg_rating, 3) if avg_rating is not None else None
    result = {"state": top_state, "review_count": top_count, "average_rating": avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zbZVBzAf6L1maBUDhJpN84JT': 'file_storage/call_zbZVBzAf6L1maBUDhJpN84JT.json', 'var_call_HtUP2QtCM4W2py1nVbQumg46': 'file_storage/call_HtUP2QtCM4W2py1nVbQumg46.json'}

exec(code, env_args)
