code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
business_path = var_call_VQjIogEs0tu2nkwSJkdJ3cZk
reviews_path = var_call_WWE9o3NplTKO1SGBp5vsUbdG

df_bus = pd.read_json(business_path)
df_rev = pd.read_json(reviews_path)

# Ensure columns exist
if 'description' not in df_bus.columns:
    df_bus['description'] = None

# Function to extract state abbreviation
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Work on uppercase to standardize
    d = desc
    # Try pattern: ' in City, ST,' or 'Located at ... in City, ST,'
    m = re.search(r'in [^,]+,\s*([A-Z]{2})(?:\b|,)', d)
    if m:
        return m.group(1)
    # Fallback: find last occurrence of ', XX' where XX is 2 letters
    m2 = re.search(r',\s*([A-Z]{2})(?:\b|,)', d)
    if m2:
        return m2.group(1)
    # Try lowercase patterns
    m3 = re.search(r'in [^,]+,\s*([a-z]{2})(?:\b|,)', d)
    if m3:
        return m3.group(1).upper()
    m4 = re.search(r',\s*([a-z]{2})(?:\b|,)', d)
    if m4:
        return m4.group(1).upper()
    return None

# Apply extraction
# Some descriptions may contain mixed case; convert to upper for matching where appropriate
# But keep original to preserve punctuation
df_bus['state'] = df_bus['description'].astype(str).apply(lambda x: extract_state(x.upper() if isinstance(x,str) else x))

# Prepare reviews: convert rating to numeric and map business_ref to business_id
if 'rating' in df_rev.columns:
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
else:
    df_rev['rating'] = None

# Map businessref to businessid
if 'business_ref' in df_rev.columns:
    df_rev['business_id'] = df_rev['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
else:
    df_rev['business_id'] = None

# Merge reviews with business states
df_merged = pd.merge(df_rev, df_bus[['business_id', 'state']], on='business_id', how='left')

# Filter to entries with known state and valid rating
df_valid = df_merged[df_merged['state'].notna() & df_merged['rating'].notna()].copy()

# Compute counts and average rating per state
grp = df_valid.groupby('state').agg(review_count=('rating', 'count'), average_rating=('rating', 'mean')).reset_index()

if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # Find state with max reviews
    top = grp.loc[grp['review_count'].idxmax()]
    result = {
        "state": str(top['state']),
        "review_count": int(top['review_count']),
        "average_rating": float(round(top['average_rating'], 4))
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VQjIogEs0tu2nkwSJkdJ3cZk': 'file_storage/call_VQjIogEs0tu2nkwSJkdJ3cZk.json', 'var_call_WWE9o3NplTKO1SGBp5vsUbdG': 'file_storage/call_WWE9o3NplTKO1SGBp5vsUbdG.json'}

exec(code, env_args)
