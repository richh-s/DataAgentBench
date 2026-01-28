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

# normalize business_id and attributes

def accepts_credit(attr):
    if attr is None:
        return False
    s = str(attr)
    # Look for BusinessAcceptsCreditCards: True pattern
    m = re.search(r"BusinessAcceptsCreditCards\s*[:=]?\s*['\"]?True['\"]?", s, re.IGNORECASE)
    return bool(m)

# normalize categories into list

def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        # sometimes stored as "None" or empty
        if cat.strip().lower() == 'none' or cat.strip() == '':
            return []
        # split by comma
        parts = [p.strip() for p in cat.split(',')]
        return [p for p in parts if p]
    # fallback
    s = str(cat)
    if s.lower() == 'none':
        return []
    parts = [p.strip() for p in s.split(',')]
    return [p for p in parts if p]

# Ensure columns exist
if 'business_id' not in bdf.columns:
    bdf['business_id'] = bdf.get('business_id', None)

bdf['accepts_credit'] = bdf.get('attributes').apply(accepts_credit)

# parse categories
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
# We count distinct business_ref per category
counts = b_accept.groupby('category')['business_ref'].nunique().reset_index().rename(columns={'business_ref':'num_businesses'})

# Prepare reviews df: convert rating to numeric
if 'rating' in rdf.columns:
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
else:
    rdf['rating'] = pd.NA

# Join reviews to business categories for accepting businesses
# Keep only reviews for businesses that accept credit
accept_refs = set(b_accept['business_ref'].dropna().unique())
rdf_accept = rdf[rdf['business_ref'].isin(accept_refs)]

# Merge reviews with category mapping (b_accept may have multiple rows per business if multiple categories)
merged = pd.merge(rdf_accept, b_accept[['business_ref','category']].dropna(), on='business_ref', how='left')

# Compute average rating per category (mean of review ratings)
avg_ratings = merged.groupby('category')['rating'].mean().reset_index().rename(columns={'rating':'avg_rating'})

# Combine counts and average ratings
summary = pd.merge(counts, avg_ratings, on='category', how='left')

# If category is NaN (businesses with no category), drop
summary = summary[summary['category'].notna()]

# Select the category with largest num_businesses
if summary.shape[0] == 0:
    result = {'category': None, 'num_businesses': 0, 'avg_rating': None}
else:
    # sort by num_businesses desc, then by avg_rating desc
    summary_sorted = summary.sort_values(['num_businesses','avg_rating'], ascending=[False, False])
    top = summary_sorted.iloc[0]
    result = {'category': top['category'], 'num_businesses': int(top['num_businesses']), 'avg_rating': float(round(top['avg_rating'],4)) if not pd.isna(top['avg_rating']) else None}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_57VwjpZjKapp8oKO6AmPqfMm': ['checkin', 'business'], 'var_call_CMobM1WcPKVp7Qb5DZI2SJHs': ['review', 'tip', 'user'], 'var_call_ZBHW94XWp3U3AoDfUe6ZQ30P': 'file_storage/call_ZBHW94XWp3U3AoDfUe6ZQ30P.json', 'var_call_sRAONQyMLlvwgo57IQUKQv8l': 'file_storage/call_sRAONQyMLlvwgo57IQUKQv8l.json'}

exec(code, env_args)
