code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_2VgzWa3JXAusBYgey1CUq8bj, 'r') as f:
    biz = json.load(f)
with open(var_call_ZRQPeIbwlwDm9DOxHjzcFWq3, 'r') as f:
    reviews = json.load(f)

# Create dataframes
df_biz = pd.DataFrame(biz)
df_rev = pd.DataFrame(reviews)

# Helper to determine if a business accepts credit cards
def accepts_credit(attrs):
    if not isinstance(attrs, dict):
        return False
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        return False
    s = str(val).lower()
    return 'true' in s

# Apply filter
if 'attributes' not in df_biz.columns:
    df_biz['attributes'] = None

df_biz_accept = df_biz[df_biz['attributes'].apply(accepts_credit)].copy()

# Extract categories into list
def split_categories(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    s = str(c)
    # Some entries may be 'None' or 'u\'...' strings; treat literally
    if s.strip().lower() in ('none', "none"):
        return []
    parts = [p.strip() for p in s.split(',')]
    return [p for p in parts if p]

if 'categories' not in df_biz_accept.columns:
    df_biz_accept['categories'] = None

df_biz_accept['category_list'] = df_biz_accept['categories'].apply(split_categories)

# Map business_id to business_ref format
if 'business_id' not in df_biz_accept.columns:
    df_biz_accept['business_id'] = None

df_biz_accept['business_ref'] = df_biz_accept['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# Explode categories
df_expl = df_biz_accept.explode('category_list')
# Drop rows with no category
df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list'] != '')].copy()

# Compute unique business counts per category
cat_counts = df_expl.groupby('category_list')['business_id'].nunique()
if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_category = cat_counts.idxmax()
    top_count = int(cat_counts.max())
    # Get business_refs in that category
    biz_refs = set(df_expl[df_expl['category_list'] == top_category]['business_ref'].unique())

    # Prepare reviews df
    if 'business_ref' not in df_rev.columns or 'rating' not in df_rev.columns:
        avg_rating = None
    else:
        df_rev_filtered = df_rev[df_rev['business_ref'].isin(biz_refs)].copy()
        if df_rev_filtered.empty:
            avg_rating = None
        else:
            df_rev_filtered['rating'] = pd.to_numeric(df_rev_filtered['rating'], errors='coerce')
            avg = df_rev_filtered['rating'].mean()
            if pd.isna(avg):
                avg_rating = None
            else:
                avg_rating = round(float(avg), 2)

    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2VgzWa3JXAusBYgey1CUq8bj': 'file_storage/call_2VgzWa3JXAusBYgey1CUq8bj.json', 'var_call_ZRQPeIbwlwDm9DOxHjzcFWq3': 'file_storage/call_ZRQPeIbwlwDm9DOxHjzcFWq3.json'}

exec(code, env_args)
