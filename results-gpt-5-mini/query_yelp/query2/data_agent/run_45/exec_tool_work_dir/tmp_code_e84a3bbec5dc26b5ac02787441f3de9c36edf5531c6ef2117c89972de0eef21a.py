code = """import json
import pandas as pd
import re

# Load stored results from previous tool calls
# var_call_SGVDFAkvaGFL6IXpUim6tuXj and var_call_wDTEvFjtZIGStRVfgNAjxsW3 are available in the environment

def load_var(v):
    if isinstance(v, str):
        # assume it's a filepath to a JSON file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_SGVDFAkvaGFL6IXpUim6tuXj)
review_records = load_var(var_call_wDTEvFjtZIGStRVfgNAjxsW3)

# Create DataFrames
df_b = pd.DataFrame(business_records)
# Some entries might not have description; ensure column exists
if 'description' not in df_b.columns:
    df_b['description'] = None

# Extract state from description using regex
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try patterns: ", ST," or ", ST" or "in City, ST"
    m = re.search(r',\s*([A-Z]{2})(?:[,\.|\s]|$)', desc)
    if m:
        return m.group(1)
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    return None

df_b['state'] = df_b['description'].apply(extract_state)
# Extract numeric id
df_b['id'] = df_b['business_id'].astype(str).str.replace('businessid_', '', regex=False)

# Reviews
df_r = pd.DataFrame(review_records)
# Convert rating to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = pd.NA
# Extract id
if 'business_ref' in df_r.columns:
    df_r['id'] = df_r['business_ref'].astype(str).str.replace('businessref_', '', regex=False)
else:
    df_r['id'] = None

# Merge reviews with business states
df_merge = df_r.merge(df_b[['id', 'state']], on='id', how='left')
# Drop reviews without state
df_merge = df_merge[df_merge['state'].notna()].copy()

# Group by state: count reviews and average rating (across reviews)
group = df_merge.groupby('state').agg(review_count=('rating', 'count'), avg_rating=('rating', 'mean')).reset_index()
# If no data, prepare empty result
if group.empty:
    result = {"state": None, "review_count": 0, "avg_rating": None}
else:
    # Find state with highest number of reviews
    top = group.sort_values(['review_count', 'avg_rating'], ascending=[False, False]).iloc[0]
    # Round avg_rating to 3 decimals
    avg_rating = None if pd.isna(top['avg_rating']) else round(float(top['avg_rating']), 3)
    result = {"state": top['state'], "review_count": int(top['review_count']), "avg_rating": avg_rating}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SGVDFAkvaGFL6IXpUim6tuXj': 'file_storage/call_SGVDFAkvaGFL6IXpUim6tuXj.json', 'var_call_wDTEvFjtZIGStRVfgNAjxsW3': 'file_storage/call_wDTEvFjtZIGStRVfgNAjxsW3.json'}

exec(code, env_args)
