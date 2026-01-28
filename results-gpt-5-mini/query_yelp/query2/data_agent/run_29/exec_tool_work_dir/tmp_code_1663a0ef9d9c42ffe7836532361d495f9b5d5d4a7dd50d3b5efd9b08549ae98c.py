code = """import json
import pandas as pd
import re

# Load data from previous tool results (file paths)
with open(var_call_054qybDdWwcEoKrO75A6satZ, 'r') as f:
    business = json.load(f)
with open(var_call_fs51dphDOuGPnfTacl7T4gFe, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
dfb = pd.DataFrame(business)
dfr = pd.DataFrame(reviews)

# Extract numeric id
dfb['id'] = dfb['business_id'].str.extract(r'_(\d+)$')
dfr['id'] = dfr['business_ref'].str.extract(r'_(\d+)$')

# Convert to int where possible
dfb = dfb[dfb['id'].notna()].copy()
dfr = dfr[dfr['id'].notna()].copy()
dfb['id'] = dfb['id'].astype(int)
dfr['id'] = dfr['id'].astype(int)

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for patterns like ", PA," or ", PA" or " in City, PA,"
    m = re.search(r',\s*([A-Z]{2})(?:,|\s|$)', desc)
    if m:
        return m.group(1)
    return None

dfb['state'] = dfb['description'].apply(extract_state)

# Merge reviews with business states
merged = dfr.merge(dfb[['id', 'state']], on='id', how='left')

# Convert rating to numeric
merged['rating'] = pd.to_numeric(merged['rating'], errors='coerce')

# Filter to rows with a known state
merged = merged[merged['state'].notna()].copy()

# Group by state to get review counts and average rating
grp = merged.groupby('state').agg(review_count=('rating', 'size'), average_rating=('rating', 'mean')).reset_index()

# If no data, return empty
if grp.shape[0] == 0:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    top = grp.sort_values(['review_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {"state": top['state'], "review_count": int(top['review_count']), "average_rating": round(float(top['average_rating']), 2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_gnEovHnvUIOJgtmMoDY7Pqpm': ['business', 'checkin'], 'var_call_7I51i9NVjqbxmb6YrwN7ovee': ['review', 'tip', 'user'], 'var_call_054qybDdWwcEoKrO75A6satZ': 'file_storage/call_054qybDdWwcEoKrO75A6satZ.json', 'var_call_fs51dphDOuGPnfTacl7T4gFe': 'file_storage/call_fs51dphDOuGPnfTacl7T4gFe.json'}

exec(code, env_args)
