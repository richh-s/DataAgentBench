code = """import json
import pandas as pd
import re

# Load data from provided storage file paths
with open(var_call_C94LEEQZASwQ8sztFiyeKnJp, 'r') as f:
    businesses = json.load(f)
with open(var_call_46dB9uTSCWe2m7Pi8sTT3qAF, 'r') as f:
    reviews = json.load(f)

df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize and extract short id by removing known prefixes
if 'business_id' in df_b.columns:
    df_b['short_id'] = df_b['business_id'].astype(str).str.replace('businessid_', '', regex=False)
else:
    df_b['short_id'] = None

if 'business_ref' in df_r.columns:
    df_r['short_id'] = df_r['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
else:
    df_r['short_id'] = None

# Function to extract state abbreviation from description
state_re = re.compile(r",\s*([A-Z]{2})(?:[.,]|\b)")
alt_re = re.compile(r"\b([A-Z]{2}) location")

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    m = state_re.search(desc)
    if m:
        return m.group(1)
    m2 = alt_re.search(desc)
    if m2:
        return m2.group(1)
    m3 = re.search(r"([A-Za-z .'\-]+),\s*([A-Z]{2})", desc)
    if m3:
        return m3.group(2)
    return None

# Extract state
if 'description' in df_b.columns:
    df_b['state'] = df_b['description'].apply(extract_state)
else:
    df_b['state'] = None

# Ensure rating numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Merge reviews with business states
merged = pd.merge(df_r, df_b[['short_id', 'state']], on='short_id', how='left')

# Filter to rows with a state
merged = merged[merged['state'].notna()]

# Group by state to get total number of reviews and average rating
grp = merged.groupby('state').agg(total_reviews=('rating', 'count'), avg_rating=('rating', 'mean'))

if grp.shape[0] == 0:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    top_state = grp['total_reviews'].idxmax()
    total_reviews = int(grp.loc[top_state, 'total_reviews'])
    avg_rating = float(grp.loc[top_state, 'avg_rating'])
    avg_rating = round(avg_rating, 3)
    result = {"state": top_state, "total_reviews": total_reviews, "average_rating": avg_rating}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_C94LEEQZASwQ8sztFiyeKnJp': 'file_storage/call_C94LEEQZASwQ8sztFiyeKnJp.json', 'var_call_46dB9uTSCWe2m7Pi8sTT3qAF': 'file_storage/call_46dB9uTSCWe2m7Pi8sTT3qAF.json'}

exec(code, env_args)
