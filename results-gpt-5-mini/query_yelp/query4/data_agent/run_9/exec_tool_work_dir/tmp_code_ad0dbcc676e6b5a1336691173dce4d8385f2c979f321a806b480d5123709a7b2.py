code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_ZBHW94XWp3U3AoDfUe6ZQ30P, 'r') as f:
    businesses = json.load(f)
with open(var_call_sRAONQyMLlvwgo57IQUKQv8l, 'r') as f:
    reviews = json.load(f)

bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Helper to detect acceptance of credit cards
def accepts_credit(attr):
    if attr is None:
        return False
    s = str(attr)
    # Look for patterns like BusinessAcceptsCreditCards': 'True' or "BusinessAcceptsCreditCards": "True"
    if re.search(r"BusinessAcceptsCreditCards\W*True", s, re.IGNORECASE):
        return True
    return False

# Normalize categories into list
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        t = cat.strip()
        if t == '' or t.lower() == 'none':
            return []
        # split by comma
        parts = [p.strip() for p in t.split(',')]
        return [p for p in parts if p]
    # fallback
    s = str(cat)
    if s.lower() == 'none':
        return []
    parts = [p.strip() for p in s.split(',')]
    return [p for p in parts if p]

# Ensure columns exist
if 'business_id' not in bdf.columns:
    bdf['business_id'] = None

if 'attributes' not in bdf.columns:
    bdf['attributes'] = None

bdf['accepts_credit'] = bdf['attributes'].apply(accepts_credit)

if 'categories' not in bdf.columns:
    bdf['categories'] = None
bdf['categories_list'] = bdf['categories'].apply(parse_categories)

# create business_ref to match reviews
bdf['business_ref'] = bdf['business_id'].astype(str).str.replace('businessid_', 'businessref_')

# explode categories
bexp = bdf[['business_ref', 'business_id', 'name', 'accepts_credit', 'categories_list']].explode('categories_list')
bexp = bexp.rename(columns={'categories_list': 'category'})

# Filter businesses that accept credit
b_accept = bexp[bexp['accepts_credit'] == True]

# Count unique businesses per category
counts = b_accept.groupby('category')['business_ref'].nunique().reset_index().rename(columns={'business_ref':'num_businesses'})

# Prepare reviews df: convert rating to numeric
if 'rating' in rdf.columns:
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
else:
    rdf['rating'] = pd.NA

# Keep reviews only for businesses that accept credit
accept_refs = set(b_accept['business_ref'].dropna().unique())
rdf_accept = rdf[rdf['business_ref'].isin(accept_refs)].copy()

# Merge reviews with category mapping
merged = pd.merge(rdf_accept, b_accept[['business_ref','category']].dropna(), on='business_ref', how='left')

# Compute average rating per category
avg_ratings = merged.groupby('category')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Combine counts and average ratings
summary = pd.merge(counts, avg_ratings, on='category', how='left')

# Drop missing category
summary = summary[summary['category'].notna()]

# Select top category by num_businesses
if summary.empty:
    result = {'category': None, 'num_businesses': 0, 'avg_rating': None}
else:
    summary_sorted = summary.sort_values(['num_businesses','avg_rating'], ascending=[False, False])
    top = summary_sorted.iloc[0]
    # format avg_rating to 4 decimal places
    avg = None if pd.isna(top['avg_rating']) else round(float(top['avg_rating']), 4)
    result = {'category': top['category'], 'num_businesses': int(top['num_businesses']), 'avg_rating': avg}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_57VwjpZjKapp8oKO6AmPqfMm': ['checkin', 'business'], 'var_call_CMobM1WcPKVp7Qb5DZI2SJHs': ['review', 'tip', 'user'], 'var_call_ZBHW94XWp3U3AoDfUe6ZQ30P': 'file_storage/call_ZBHW94XWp3U3AoDfUe6ZQ30P.json', 'var_call_sRAONQyMLlvwgo57IQUKQv8l': 'file_storage/call_sRAONQyMLlvwgo57IQUKQv8l.json'}

exec(code, env_args)
