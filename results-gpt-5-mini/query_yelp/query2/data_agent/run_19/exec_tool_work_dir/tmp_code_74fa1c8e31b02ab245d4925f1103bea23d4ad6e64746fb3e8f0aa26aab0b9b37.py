code = """import json
import pandas as pd
import re

# Load data from storage files
with open(var_call_hmTBT2DHTxceJVlLDlvqmGy5, 'r') as f:
    businesses = json.load(f)
with open(var_call_C26XA720lemvNYIWrVw6IXtD, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Ensure columns exist
if 'description' not in df_b.columns:
    df_b['description'] = None

# Extract state from description using regex (take last 2-letter uppercase match)
def extract_state(desc):
    if not isinstance(desc, str):
        return None
    matches = re.findall(r"\b([A-Z]{2})\b", desc)
    return matches[-1] if matches else None

df_b['state'] = df_b['description'].apply(extract_state)

# Extract suffix id from business_id and business_ref
df_b['id_suffix'] = df_b['business_id'].astype(str).apply(lambda s: s.split('_')[-1] if isinstance(s, str) and '_' in s else None)
if 'business_ref' in df_r.columns:
    df_r['id_suffix'] = df_r['business_ref'].astype(str).apply(lambda s: s.split('_')[-1] if isinstance(s, str) and '_' in s else None)
else:
    df_r['id_suffix'] = None

# Convert ratings to numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with businesses on id_suffix
df = df_r.merge(df_b[['id_suffix', 'state']], on='id_suffix', how='left')

# Filter to rows with a valid state and rating
df = df[df['state'].notna() & df['rating'].notna()]

# Group by state
grp = df.groupby('state').agg(review_count=('rating', 'size'), average_rating=('rating', 'mean')).reset_index()

# If no data, return empty
if grp.empty:
    result = {"state": None, "review_count": 0, "average_rating": None}
else:
    max_row = grp.loc[grp['review_count'].idxmax()]
    result = {
        "state": str(max_row['state']),
        "review_count": int(max_row['review_count']),
        "average_rating": float(round(float(max_row['average_rating']), 3))
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_35fgkqrbnU6wwvPZlWOULiZy': ['business', 'checkin'], 'var_call_4aMIiTGqEUjIrhUXk4fjUb2X': ['review', 'tip', 'user'], 'var_call_hmTBT2DHTxceJVlLDlvqmGy5': 'file_storage/call_hmTBT2DHTxceJVlLDlvqmGy5.json', 'var_call_C26XA720lemvNYIWrVw6IXtD': 'file_storage/call_C26XA720lemvNYIWrVw6IXtD.json'}

exec(code, env_args)
