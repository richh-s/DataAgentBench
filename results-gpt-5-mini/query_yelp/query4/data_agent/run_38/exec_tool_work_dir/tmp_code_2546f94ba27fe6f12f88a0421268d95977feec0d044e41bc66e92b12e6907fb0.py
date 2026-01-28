code = """import json
import pandas as pd

# Load the large JSON results from previous queries stored as file paths
with open(var_call_O9KyZjGrIpkwN2nC1wIjqtqU, 'r') as f:
    businesses = json.load(f)
with open(var_call_VFqrAgjYogQR7lq5ElNsE2Jt, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
# Ensure expected columns
for c in ['business_id', 'attributes', 'categories', 'name']:
    if c not in df_b.columns:
        df_b[c] = None

# Normalize attributes: some are string "None" or None
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, str):
        if attr.lower() == 'none':
            return False
        # try to parse rudimentary dict-looking strings
        if "BusinessAcceptsCreditCards" in attr:
            # find occurrence
            # crude: look for BusinessAcceptsCreditCards': 'True' or "True"
            if 'BusinessAcceptsCreditCards' in attr:
                return 'true' in attr.lower()
        return False
    if isinstance(attr, dict):
        v = attr.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return str(v).lower().find('true')!=-1
    return False

# Determine which businesses accept credit cards
df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# Parse categories: some entries may have categories as string with commas
def parse_cats(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    if isinstance(c, str):
        if c.lower() == 'none' or c.strip()=='' or c.lower()=='null':
            return []
        # split by comma
        parts = [p.strip() for p in c.split(',')]
        return [p for p in parts if p]
    return []

# Apply
if 'categories' not in df_b.columns:
    df_b['categories'] = None

df_b['categories_list'] = df_b['categories'].apply(parse_cats)

# Filter businesses that accept credit cards
df_cc = df_b[df_b['accepts_cc']].copy()

# Map business_id to business_ref
# business_id like 'businessid_1' -> businessref_1
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_',1)
    if len(parts)==2:
        return 'businessref_' + parts[1]
    return None

df_cc['business_ref'] = df_cc['business_id'].apply(to_ref)

# Reviews dataframe
df_r = pd.DataFrame(reviews)
# Ensure rating numeric
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with businesses that accept cc
# Many businesses may have no categories; drop those with no categories
# Explode categories
df_cc_expl = df_cc[['business_id','business_ref','categories_list']].explode('categories_list')
# Drop rows with empty category
df_cc_expl = df_cc_expl[df_cc_expl['categories_list'].notna() & (df_cc_expl['categories_list']!='')]

# Merge reviews
merged = pd.merge(df_cc_expl, df_r, left_on='business_ref', right_on='business_ref', how='left')

# For business counts per category, count unique business_id per category
biz_counts = df_cc_expl.groupby('categories_list')['business_id'].nunique().rename('business_count')

# For average rating per category, take all ratings of businesses in that category
# merged has rows per (business,category,review)
# Exclude NaN ratings when averaging
avg_ratings = merged.groupby('categories_list')['rating'].mean().rename('avg_rating')

# Combine
summary = pd.concat([biz_counts, avg_ratings], axis=1).reset_index().rename(columns={'categories_list':'category'})
# Some categories may have NaN avg_rating if no reviews; keep them
# Find category with largest business_count
if summary.shape[0]==0:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    max_count = summary['business_count'].max()
    top = summary[summary['business_count']==max_count].copy()
    # If multiple, pick the one with highest avg_rating among them (ignoring NaN)
    top['avg_rating_filled'] = top['avg_rating'].fillna(-1)
    top = top.sort_values(['avg_rating_filled','category'], ascending=[False,True]).iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': None if pd.isna(top['avg_rating']) else float(round(top['avg_rating'],3))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_hXzUi1HOyrj3924Zuuu4nlzl': ['business', 'checkin'], 'var_call_Vx7f3xeQCmMRh0NWNG3HKaZW': ['review', 'tip', 'user'], 'var_call_O9KyZjGrIpkwN2nC1wIjqtqU': 'file_storage/call_O9KyZjGrIpkwN2nC1wIjqtqU.json', 'var_call_VFqrAgjYogQR7lq5ElNsE2Jt': 'file_storage/call_VFqrAgjYogQR7lq5ElNsE2Jt.json'}

exec(code, env_args)
