code = """import json
import re
import pandas as pd

# Load the query results from storage files
with open(var_call_44ZjECz4jsmP2YagpmhQJh6f, 'r') as f:
    businesses = json.load(f)
with open(var_call_JBiogo0sXTh4HbhR1iAOCGnQ, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Helper to determine if business accepts credit cards
import math

def accepts_credit(attrs):
    if attrs is None:
        return False
    # If it's a dict
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return str(val).lower().find('true') != -1
    # If string
    if isinstance(attrs, str):
        s = attrs.strip()
        if s.lower() == 'none':
            return False
        # Try to find a key/value pattern
        m = re.search(r"BusinessAcceptsCreditCards[^:\n]*[:=]\s*'?\"?(True|False)'?\"?", s, flags=re.IGNORECASE)
        if m:
            return m.group(1).lower() == 'true'
        # Also check for patterns like 'BusinessAcceptsCreditCards': 'True'
        m = re.search(r"BusinessAcceptsCreditCards\s*\'\s*[:]\s*\'?(True|False)\'?", s, flags=re.IGNORECASE)
        if m:
            return m.group(1).lower() == 'true'
        # Last resort, see if the word True appears near the key
        if 'BusinessAcceptsCreditCards' in s and 'true' in s.lower():
            return True
        return False
    return False

# Normalize categories: may be missing; if present as string, split by comma

def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        s = cat.strip()
        if s.lower() == 'none' or s == '':
            return []
        # Sometimes categories are quoted lists or a single string with commas
        # Remove surrounding brackets or quotes
        s2 = s
        # If string contains commas, split
        parts = [p.strip() for p in s2.split(',') if p.strip()]
        return parts
    return []

# Build mapping for businesses that accept credit cards
bdf['accepts_credit'] = bdf['attributes'].apply(accepts_credit)
# Ensure categories column exists
if 'categories' not in bdf.columns:
    bdf['categories'] = None

bdf['categories_list'] = bdf['categories'].apply(parse_categories)

# Create business_ref equivalent
def to_ref(bid):
    if not isinstance(bid, str):
        return None
    return bid.replace('businessid_', 'businessref_')

bdf['business_ref'] = bdf['business_id'].apply(to_ref)

# Filter businesses that accept credit cards
credit_biz = bdf[bdf['accepts_credit'] == True].copy()

# Build mapping business_ref -> categories_list
biz_cat = credit_biz.set_index('business_ref')['categories_list'].to_dict()

# Prepare reviews DataFrame
rdf = rdf[rdf['business_ref'].notnull()].copy()
# Convert rating to numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Filter reviews to only those for businesses that accept credit cards
rdf_credit = rdf[rdf['business_ref'].isin(biz_cat.keys())].copy()

# Expand reviews by categories: map business_ref to categories and explode
rdf_credit['categories'] = rdf_credit['business_ref'].map(biz_cat)
# Drop reviews whose business has no categories
rdf_credit = rdf_credit[rdf_credit['categories'].map(lambda x: bool(x))].copy()

rdf_exploded = rdf_credit.explode('categories')
rdf_exploded['categories'] = rdf_exploded['categories'].str.strip()

# Compute number of unique businesses per category (among credit-accepting businesses)
# For that, use biz_cat mapping to count unique business_refs per category
from collections import defaultdict
cat_to_bizset = defaultdict(set)
for br, cats in biz_cat.items():
    for c in cats:
        c2 = c.strip()
        if c2:
            cat_to_bizset[c2].add(br)

cat_counts = {c: len(s) for c, s in cat_to_bizset.items()}

# Compute average rating per category using reviews (weighted by number of reviews)
# Use rdf_exploded which contains review-level ratings mapped to categories
cat_group = rdf_exploded.groupby('categories')['rating'].agg(['mean','count']).reset_index()
cat_group['mean'] = cat_group['mean'].round(3)

# Combine counts and means
results = []
for c, cnt in cat_counts.items():
    mean_row = cat_group[cat_group['categories'] == c]
    mean = None
    review_count = 0
    if not mean_row.empty:
        mean = float(mean_row['mean'].iloc[0])
        review_count = int(mean_row['count'].iloc[0])
    results.append({'category': c, 'business_count': cnt, 'avg_rating': mean, 'num_reviews': review_count})

# If no results, return a message
if not results:
    out = {'category': None, 'business_count': 0, 'avg_rating': None}
else:
    # Find category with largest business_count; if tie, choose with highest business_count then highest avg_rating
    res_df = pd.DataFrame(results)
    max_count = res_df['business_count'].max()
    candidates = res_df[res_df['business_count'] == max_count].copy()
    # choose the one with highest avg_rating among candidates (NaNs handled)
    candidates['avg_rating_fill'] = candidates['avg_rating'].fillna(-1)
    best = candidates.sort_values(['avg_rating_fill','category'], ascending=[False, True]).iloc[0]
    out = {'category': best['category'], 'business_count': int(best['business_count']), 'avg_rating': None if pd.isna(best['avg_rating']) else float(round(best['avg_rating'],3))}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_44ZjECz4jsmP2YagpmhQJh6f': 'file_storage/call_44ZjECz4jsmP2YagpmhQJh6f.json', 'var_call_JBiogo0sXTh4HbhR1iAOCGnQ': 'file_storage/call_JBiogo0sXTh4HbhR1iAOCGnQ.json'}

exec(code, env_args)
