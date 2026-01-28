code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_WxTjm8yJBKjgiFdZopzR8a8o, 'r') as f:
    businesses = json.load(f)
with open(var_call_tV5Ysp0Q7UR4tdGymlUigNb5, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize business id numeric part
def extract_num_id(bid):
    if not isinstance(bid, str):
        return None
    parts = bid.split('_')
    return parts[-1]

bdf['biz_num'] = bdf['business_id'].apply(extract_num_id)
rdf['biz_num'] = rdf['business_ref'].apply(extract_num_id)

# Convert ratings to numeric
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

# Function to determine if a business accepts credit cards
import re

def accepts_cc(attr):
    if attr is None:
        return False
    # If it's a dict
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is True:
            return True
        if isinstance(val, str) and 'True' in val:
            return True
        return False
    # If it's a string representation
    if isinstance(attr, str):
        if attr.strip().lower() == 'none':
            return False
        # look for the substring BusinessAcceptsCreditCards followed by True
        if 'BusinessAcceptsCreditCards' in attr and 'True' in attr:
            return True
        return False
    return False

bdf['accepts_cc'] = bdf['attributes'].apply(accepts_cc)

# Prepare categories: some records may not have 'categories' key
if 'categories' not in bdf.columns:
    bdf['categories'] = None

# Split categories into list

def split_categories(cat):
    if pd.isna(cat) or cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        # sometimes categories are represented as a single string with commas
        parts = [c.strip() for c in cat.split(',') if c.strip()]
        return parts
    return []

bdf['category_list'] = bdf['categories'].apply(split_categories)

# Filter businesses that accept credit cards
cc_biz = bdf[bdf['accepts_cc'] == True].copy()

# Explode categories
cc_biz_expl = cc_biz.explode('category_list')
# Drop rows with empty category
cc_biz_expl = cc_biz_expl[cc_biz_expl['category_list'].notna() & (cc_biz_expl['category_list'] != '')]

# Count distinct businesses per category
cat_counts = cc_biz_expl.groupby('category_list')['biz_num'].nunique().reset_index()
cat_counts = cat_counts.rename(columns={'category_list': 'category', 'biz_num': 'business_count'})

# If no categories found, return empty
if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # Find top category
    top = cat_counts.sort_values(['business_count', 'category'], ascending=[False, True]).iloc[0]
    top_cat = top['category']
    top_count = int(top['business_count'])

    # Businesses in top category that accept cc
    biz_nums_in_top = cc_biz_expl[cc_biz_expl['category_list'] == top_cat]['biz_num'].unique().tolist()

    # Filter reviews for these businesses
    revs_top = rdf[rdf['biz_num'].isin(biz_nums_in_top)].copy()

    if revs_top.empty:
        avg_rating = None
    else:
        avg_rating = float(revs_top['rating'].mean())

    result = {'category': top_cat, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WxTjm8yJBKjgiFdZopzR8a8o': 'file_storage/call_WxTjm8yJBKjgiFdZopzR8a8o.json', 'var_call_tV5Ysp0Q7UR4tdGymlUigNb5': 'file_storage/call_tV5Ysp0Q7UR4tdGymlUigNb5.json'}

exec(code, env_args)
