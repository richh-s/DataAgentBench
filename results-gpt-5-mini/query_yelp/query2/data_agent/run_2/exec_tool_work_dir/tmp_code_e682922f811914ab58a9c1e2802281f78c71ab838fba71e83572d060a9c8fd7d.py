code = """import json
import re
import pandas as pd

# Load data from storage file paths
business_file = var_call_glKA8W8O9XQpL6skMLeTPrBG
review_file = var_call_Yq9r2lFTFDEhJb5LK7Hi8IAf

with open(business_file, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(review_file, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure expected columns exist
if 'business_id' not in df_b.columns:
    df_b['business_id'] = None
if 'description' not in df_b.columns:
    df_b['description'] = None

# Extract state from description using regex
state_re = re.compile(r"([A-Za-z .'-]+),\s*([A-Z]{2})\b")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_re.search(desc)
    if m:
        return m.group(2)
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Prepare reviews: convert businessref to businessid by replacing prefix
if 'business_ref' in df_r.columns:
    df_r['business_id'] = df_r['business_ref'].astype(str).str.replace('businessref_', 'businessid_', regex=False)
else:
    df_r['business_id'] = None

# Convert rating to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.NA

# Merge reviews with business states
df_merged = df_r.merge(df_b[['business_id', 'state']], on='business_id', how='left')

# Filter only rows with a recognized US state
df_merged = df_merged[df_merged['state'].notna()]

# Group by state to count reviews and compute average rating
grp = df_merged.groupby('state').agg(total_reviews=('rating', 'count'), avg_rating=('rating', 'mean')).reset_index()

if grp.empty:
    result = {"state": None, "total_reviews": 0, "avg_rating": None}
else:
    # Find state with max reviews
    top = grp.sort_values(['total_reviews', 'state'], ascending=[False, True]).iloc[0]
    result = {"state": str(top['state']), "total_reviews": int(top['total_reviews']), "avg_rating": float(round(top['avg_rating'], 3))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_glKA8W8O9XQpL6skMLeTPrBG': 'file_storage/call_glKA8W8O9XQpL6skMLeTPrBG.json', 'var_call_Yq9r2lFTFDEhJb5LK7Hi8IAf': 'file_storage/call_Yq9r2lFTFDEhJb5LK7Hi8IAf.json'}

exec(code, env_args)
