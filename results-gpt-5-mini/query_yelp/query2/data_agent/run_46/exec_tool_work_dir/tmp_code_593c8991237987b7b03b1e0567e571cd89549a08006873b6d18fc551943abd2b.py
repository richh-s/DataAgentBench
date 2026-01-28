code = """import json
import pandas as pd
import re

# Load data from stored JSON file paths
with open(var_call_s0cbv6v3y1glmOFailpYdjPR, 'r') as f:
    business = json.load(f)
with open(var_call_mWpcGhhjU7kjURECO1LH19AA, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(business)
df_r = pd.DataFrame(reviews)

# Normalize and convert types
if 'business_ref' in df_r.columns:
    df_r['business_id'] = df_r['business_ref'].str.replace('businessref_', 'businessid_', regex=False)
else:
    df_r['business_id'] = None

df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')

# Merge reviews with business descriptions
df = pd.merge(df_r, df_b[['business_id', 'description']], on='business_id', how='left')

# Function to extract 2-letter state code from description
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    # Common pattern: ", XX,"
    m = re.search(r',\s*([A-Z]{2})[,\.]', desc)
    if m:
        return m.group(1)
    # Pattern with 'in City, ST'
    m = re.search(r'in [^,]+,\s*([A-Z]{2})', desc)
    if m:
        return m.group(1)
    # Fallback: find any two-letter uppercase token
    m = re.findall(r'\b([A-Z]{2})\b', desc)
    if m:
        return m[0]
    return None

# Apply extraction
df['state'] = df['description'].apply(extract_state)

# Group by state to count reviews and compute average rating
grp = df.groupby('state').agg(total_reviews=('rating', 'count'), avg_rating=('rating', 'mean')).reset_index()
grp = grp[grp['state'].notna()]

# Handle case with no data
if grp.empty:
    result = {"state": None, "total_reviews": 0, "avg_rating": None}
else:
    row = grp.loc[grp['total_reviews'].idxmax()]
    state = row['state']
    total = int(row['total_reviews'])
    avg = round(float(row['avg_rating']), 2) if not pd.isna(row['avg_rating']) else None
    result = {"state": state, "total_reviews": total, "avg_rating": avg}

import json as _json
print("__RESULT__:")
print(_json.dumps(result))"""

env_args = {'var_call_dcG1W8rbw1H4d8YxTkZhT9T5': ['business', 'checkin'], 'var_call_hMB47VWfI82805VKRZltr494': ['review', 'tip', 'user'], 'var_call_s0cbv6v3y1glmOFailpYdjPR': 'file_storage/call_s0cbv6v3y1glmOFailpYdjPR.json', 'var_call_mWpcGhhjU7kjURECO1LH19AA': 'file_storage/call_mWpcGhhjU7kjURECO1LH19AA.json'}

exec(code, env_args)
