code = """import json
import pandas as pd

# Load full results from storage file paths
with open(var_call_L3aEZLGLFlCjzU90qdErzaiv, 'r') as f:
    businesses = json.load(f)
with open(var_call_ZS8TTBueUsmVsHL2RjoBDATY, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize attributes: ensure dict or None
def parse_attributes(a):
    if a is None:
        return {}
    if isinstance(a, dict):
        return a
    # sometimes string "None"
    if isinstance(a, str):
        if a.strip().lower() == 'none':
            return {}
        try:
            # attempt to eval simple dict-like strings
            parsed = eval(a)
            if isinstance(parsed, dict):
                return parsed
            else:
                return {}
        except Exception:
            return {}
    return {}

bdf['attributes_parsed'] = bdf['attributes'].apply(parse_attributes)

# Determine whether business accepts credit cards
def accepts_cc(attrs):
    if not isinstance(attrs, dict):
        return False
    val = attrs.get('BusinessAcceptsCreditCards')
    if val is None:
        # some datasets might have different casing
        for k in attrs.keys():
            if k.lower() == 'businessacceptscreditcards':
                val = attrs.get(k)
                break
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val)
    if isinstance(val, str):
        v = val.strip().lower()
        # handle patterns like "u'no'" or "'True'"
        if "true" in v:
            return True
        if v in ['1','yes','y','t']:
            return True
        return False
    return False

bdf['accepts_cc'] = bdf['attributes_parsed'].apply(accepts_cc)

# Parse categories: handle None, list, string
def parse_categories(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    if isinstance(c, str):
        if c.strip().lower() in ['none','nan','null','']:
            return []
        # split by comma
        parts = [p.strip() for p in c.split(',')]
        parts = [p for p in parts if p]
        return parts
    return []

if 'categories' not in bdf.columns:
    bdf['categories'] = None
bdf['categories_parsed'] = bdf['categories'].apply(parse_categories)

# Filter businesses that accept credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()

# Explode categories so each row is business-category
cc_biz_exploded = cc_biz.explode('categories_parsed')
cc_biz_exploded = cc_biz_exploded.rename(columns={'categories_parsed':'category'})
cc_biz_exploded = cc_biz_exploded[cc_biz_exploded['category'].notna()]

# Count unique businesses per category
cat_counts = cc_biz_exploded.groupby('category')['business_id'].nunique().reset_index()
cat_counts = cat_counts.rename(columns={'business_id':'num_businesses'})

# Prepare reviews DataFrame: convert rating to numeric and map business_ref to business_id
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
rdf['business_id'] = rdf['business_ref'].str.replace('businessref_','businessid_')

# For businesses that accept cc, join reviews
# We'll compute average rating per category using all reviews of businesses in that category
# First join cc_biz_exploded (business_id, category) with reviews on business_id
merged = pd.merge(cc_biz_exploded[['business_id','category']], rdf[['business_id','rating']], on='business_id', how='left')

# Compute average rating per category (ignore NaN ratings)
cat_ratings = merged.groupby('category')['rating'].agg(['mean','count']).reset_index()
cat_ratings = cat_ratings.rename(columns={'mean':'avg_rating','count':'num_reviews'})

# Combine counts and ratings
summary = pd.merge(cat_counts, cat_ratings, on='category', how='left')

# Replace NaN avg_rating with None
summary['avg_rating'] = summary['avg_rating'].apply(lambda x: None if pd.isna(x) else float(x))

# Find top category by num_businesses
if summary.shape[0] == 0:
    result = {'category': None, 'num_businesses': 0, 'average_rating': None}
else:
    top_row = summary.sort_values(['num_businesses','avg_rating'], ascending=[False, False]).iloc[0]
    result = {
        'category': top_row['category'],
        'num_businesses': int(top_row['num_businesses']),
        'average_rating': None if top_row['avg_rating'] is None else round(float(top_row['avg_rating']), 2)
    }

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9eED9IMmcC3gBPqLot3GmKf2': ['checkin', 'business'], 'var_call_L3aEZLGLFlCjzU90qdErzaiv': 'file_storage/call_L3aEZLGLFlCjzU90qdErzaiv.json', 'var_call_Eg0pI6raclNDSIJBwTjhmyyt': ['review', 'tip', 'user'], 'var_call_ZS8TTBueUsmVsHL2RjoBDATY': 'file_storage/call_ZS8TTBueUsmVsHL2RjoBDATY.json'}

exec(code, env_args)
