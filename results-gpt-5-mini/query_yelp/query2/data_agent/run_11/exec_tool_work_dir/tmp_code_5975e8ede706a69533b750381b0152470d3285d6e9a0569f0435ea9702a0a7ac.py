code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_xYY0K9QHgp5wDd5l9aDeFel4, 'r') as f:
    business_data = json.load(f)
with open(var_call_cP82EwxX4FzJyZHJlBon5SFD, 'r') as f:
    review_data = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(business_data)
df_r = pd.DataFrame(review_data)

# Helper to extract numeric id from businessid_XX or businessref_XX
def extract_num(s):
    if pd.isna(s):
        return None
    m = re.search(r"_(\d+)$", str(s))
    return m.group(1) if m else None

# Extract numeric ids
if 'business_id' in df_b.columns:
    df_b['id_num'] = df_b['business_id'].apply(extract_num)
else:
    df_b['id_num'] = df_b.get('_id', None).apply(extract_num)

if 'business_ref' in df_r.columns:
    df_r['id_num'] = df_r['business_ref'].apply(extract_num)
else:
    df_r['id_num'] = None

# Extract state from description

def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Try common pattern: comma space STATE followed by comma
    m = re.search(r",\s*([A-Z]{2})[,\s]", desc)
    if m:
        return m.group(1)
    # Try 'in City, ST' pattern
    m = re.search(r"in [^,]+,\s*([A-Z]{2})", desc)
    if m:
        return m.group(1)
    # Find any two-letter uppercase token surrounded by commas
    tokens = re.findall(r"\b([A-Z]{2})\b", desc)
    if tokens:
        # choose last token (often state)
        return tokens[-1]
    return None

df_b['state'] = df_b['description'].apply(extract_state)

# Clean review ratings to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with business states on id_num
merged = pd.merge(df_r, df_b[['id_num', 'state']], on='id_num', how='left')

# Drop rows without state
merged = merged[merged['state'].notna()]

# Group by state: count reviews and average rating
grouped = merged.groupby('state').agg(review_count=('rating','count'), average_rating=('rating','mean')).reset_index()

# If grouped is empty, prepare a fallback
if grouped.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    # Find state with max reviews
    top = grouped.sort_values(['review_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {
        "state": str(top['state']),
        "review_count": int(top['review_count']),
        "average_rating": round(float(top['average_rating']), 3) if pd.notna(top['average_rating']) else None
    }

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_cyIUIlA2ZG3dFYJyamEuCSd7': ['checkin', 'business'], 'var_call_Nmft9xrAEEBclLMHOjdDNJQx': ['review', 'tip', 'user'], 'var_call_xYY0K9QHgp5wDd5l9aDeFel4': 'file_storage/call_xYY0K9QHgp5wDd5l9aDeFel4.json', 'var_call_cP82EwxX4FzJyZHJlBon5SFD': 'file_storage/call_cP82EwxX4FzJyZHJlBon5SFD.json'}

exec(code, env_args)
