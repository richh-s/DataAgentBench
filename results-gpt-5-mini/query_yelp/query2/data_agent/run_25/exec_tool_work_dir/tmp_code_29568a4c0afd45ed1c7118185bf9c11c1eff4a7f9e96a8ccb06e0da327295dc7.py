code = """import json
import pandas as pd
import re

# Load results from previous query_db calls
business_file = var_call_jZ88YqdkjuL2GfDb5lX2Xu5e
review_file = var_call_FjbXiORSo192Zq1gEMyPxot6

with open(business_file, 'r') as f:
    businesses = json.load(f)
with open(review_file, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
# ensure business_id and description exist
if 'business_id' not in df_b.columns:
    df_b['business_id'] = None
if 'description' not in df_b.columns:
    df_b['description'] = None

# Extract state abbreviation from description using regex
# look for pattern like ', XX' where XX are 2 uppercase letters

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = re.search(r',\s*([A-Z]{2})(?:[,\s]|$)', desc)
    if m:
        return m.group(1)
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Normalize business_id
# business collection uses businessid_#

# Load reviews
df_r = pd.DataFrame(reviews)
if 'business_ref' not in df_r.columns:
    df_r['business_ref'] = None
if 'rating' not in df_r.columns:
    df_r['rating'] = None

# Map review business_ref to business_id by replacing prefix
# Example: businessref_1 -> businessid_1

def ref_to_id(ref):
    if not isinstance(ref, str):
        return None
    return ref.replace('businessref_', 'businessid_')

df_r['business_id'] = df_r['business_ref'].apply(ref_to_id)
# Convert rating to numeric
df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Merge reviews with business data to get state per review
merged = pd.merge(df_r, df_b[['business_id','state']], on='business_id', how='left')

# Drop reviews without state
merged = merged[merged['state'].notna()]

# Group by state: count reviews and compute average rating
grp = merged.groupby('state').agg(total_reviews=('rating','count'), average_rating=('rating','mean')).reset_index()

if grp.empty:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    # find state with max reviews
    top = grp.sort_values('total_reviews', ascending=False).iloc[0]
    result = {"state": str(top['state']), "total_reviews": int(top['total_reviews']), "average_rating": round(float(top['average_rating']), 2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_fYXPEkenoVBFjFYMpMmvNNyN': ['checkin', 'business'], 'var_call_A8pUdTlaDjIv63sJH8ie64U2': ['review', 'tip', 'user'], 'var_call_jZ88YqdkjuL2GfDb5lX2Xu5e': 'file_storage/call_jZ88YqdkjuL2GfDb5lX2Xu5e.json', 'var_call_FjbXiORSo192Zq1gEMyPxot6': 'file_storage/call_FjbXiORSo192Zq1gEMyPxot6.json'}

exec(code, env_args)
