code = """import json
import pandas as pd

# Load the business and review data from storage file paths
with open(var_call_0Ioc9rMhjiImYfuDCvN3Uwm6, 'r') as f:
    businesses = json.load(f)
with open(var_call_6MN17eUATOGx111pe3StyhUD, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
df_r = pd.DataFrame(reviews)

# Normalize attributes parsing
import re

def accepts_credit(attributes):
    if attributes is None:
        return False
    # If it's a dict
    if isinstance(attributes, dict):
        val = attributes.get('BusinessAcceptsCreditCards')
        return val is True or str(val) == 'True'
    # if it's a string representation
    if isinstance(attributes, str):
        if attributes.strip().lower() == 'none':
            return False
        # look for BusinessAcceptsCreditCards key and True value
        m = re.search(r"BusinessAcceptsCreditCards\s*[:=]?,?\s*('?\"?)(True|False)\1", attributes)
        if m:
            return m.group(2) == 'True'
        # also handle formats like 'BusinessAcceptsCreditCards': 'True' or "BusinessAcceptsCreditCards": "True"
        if 'BusinessAcceptsCreditCards' in attributes and 'True' in attributes:
            return True
    return False

# Apply function
# Some rows may not have attributes column; ensure existence
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# Prepare categories: normalize to list
def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        # Some strings may be like "Food, Restaurants"
        parts = [c.strip() for c in cat.split(',')]
        return [p for p in parts if p]
    return []

if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Add business_ref column to match reviews
df_b['business_ref'] = df_b['business_id'].str.replace('businessid_', 'businessref_')

# Filter businesses that accept credit cards
df_cc = df_b[df_b['accepts_cc'] == True].copy()

# Expand categories
df_cc['category_list'] = df_cc['categories'].apply(parse_categories)

# Explode
df_expl = df_cc[['business_id', 'business_ref', 'category_list']].explode('category_list')
# Drop rows with empty category
df_expl = df_expl[df_expl['category_list'].notna() & (df_expl['category_list'] != '')]

# Count unique businesses per category
biz_count = df_expl.groupby('category_list')['business_id'].nunique().reset_index()
biz_count = biz_count.rename(columns={'business_id': 'business_count', 'category_list': 'category'})

# Prepare reviews dataframe
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Merge reviews with exploded categories on business_ref
merged = pd.merge(df_expl, df_r, left_on='business_ref', right_on='business_ref', how='left')

# Compute average rating per category using reviews
avg_rating = merged.groupby('category_list')['rating'].mean().reset_index()
avg_rating = avg_rating.rename(columns={'category_list': 'category', 'rating': 'average_rating'})

# Combine counts and average
summary = pd.merge(biz_count, avg_rating, on='category', how='left')
# If average_rating is NaN (no reviews), set to None
summary['average_rating'] = summary['average_rating'].apply(lambda x: None if pd.isna(x) else float(x))

# Find category with largest business_count
if summary.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top = summary.sort_values(['business_count', 'average_rating'], ascending=[False, False]).iloc[0]
    result = {'category': top['category'], 'business_count': int(top['business_count']), 'average_rating': (round(top['average_rating'], 2) if top['average_rating'] is not None else None)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_TLLD5knH0l6gGexALt0meO7T': 'file_storage/call_TLLD5knH0l6gGexALt0meO7T.json', 'var_call_0Ioc9rMhjiImYfuDCvN3Uwm6': 'file_storage/call_0Ioc9rMhjiImYfuDCvN3Uwm6.json', 'var_call_6MN17eUATOGx111pe3StyhUD': 'file_storage/call_6MN17eUATOGx111pe3StyhUD.json'}

exec(code, env_args)
