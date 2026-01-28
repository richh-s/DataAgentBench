code = """import json
import pandas as pd
import re

def load_var(v):
    # v is provided by storage; it may be a path string or a list
    if isinstance(v, str):
        # assume it's a filepath
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_OPoWjLOuz2e3eHihbcSxLk3A)
review_records = load_var(var_call_yOKR7q8hgtOHNxOVPQXaQ0S8)

# Create DataFrames
biz_df = pd.DataFrame(business_records)
rev_df = pd.DataFrame(review_records)

# Ensure relevant columns exist
if 'business_id' not in biz_df.columns:
    biz_df['business_id'] = None
if 'description' not in biz_df.columns:
    biz_df['description'] = None

# Extract state from description using regex for 2-letter state
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Look for patterns like ", XX" where XX are letters
    m = re.search(r",\s*([A-Z]{2})(?:\b|,)", desc)
    if m:
        return m.group(1)
    # also try patterns like ' in City, ST' or ending with ' City, ST.'
    m2 = re.search(r"\b([A-Z]{2})\b", desc)
    if m2:
        return m2.group(1)
    return None

biz_df['state'] = biz_df['description'].apply(extract_state)

# Map businessid_# -> businessref_#
def to_business_ref(bid):
    if not isinstance(bid, str):
        return None
    # replace prefix
    return bid.replace('businessid_', 'businessref_')

biz_df['business_ref'] = biz_df['business_id'].apply(to_business_ref)

# Prepare reviews
if 'business_ref' not in rev_df.columns:
    rev_df['business_ref'] = None
if 'rating' not in rev_df.columns:
    rev_df['rating'] = None

# Convert rating to numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Join reviews with business states
merged = rev_df.merge(biz_df[['business_ref','state']], on='business_ref', how='left')

# Drop reviews without state
merged = merged[merged['state'].notna()].copy()

# Group by state
grp = merged.groupby('state').agg(total_reviews=('rating','size'), average_rating=('rating','mean')).reset_index()

if grp.empty:
    result = {'state': None, 'total_reviews': 0, 'average_rating': None}
else:
    # find state with max reviews
    top = grp.sort_values('total_reviews', ascending=False).iloc[0]
    result = {
        'state': str(top['state']),
        'total_reviews': int(top['total_reviews']),
        'average_rating': round(float(top['average_rating']), 3)
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_OPoWjLOuz2e3eHihbcSxLk3A': 'file_storage/call_OPoWjLOuz2e3eHihbcSxLk3A.json', 'var_call_yOKR7q8hgtOHNxOVPQXaQ0S8': 'file_storage/call_yOKR7q8hgtOHNxOVPQXaQ0S8.json'}

exec(code, env_args)
