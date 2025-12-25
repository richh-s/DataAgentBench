code = """import json, pandas as pd
from collections import defaultdict

# Load business records with credit card acceptance
business_cc = pd.DataFrame(var_call_palNDytL6J5Vi3TGr1crOeiS)

# Derive mapping from business_id to categories (if categories existed; fall back to None)
if 'categories' in business_cc.columns:
    business_cc['categories'] = business_cc['categories'].fillna('Unknown')
else:
    business_cc['categories'] = 'Unknown'

# Map business_id -> a single category label (using full string as category)
# Also adapt IDs to match review table (businessid_X -> businessref_X)

business_cc['business_ref'] = business_cc['business_id'].str.replace('businessid_', 'businessref_', regex=False)

# Load full review data from file
with open(var_call_F5ZVPlHcTEoSXEQoTy8bauWi, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)
reviews_df['rating'] = reviews_df['rating'].astype(float)

# Filter reviews to only those businesses that accept credit cards
merged = reviews_df.merge(business_cc[['business_ref', 'categories']], on='business_ref', how='inner')

# Group by category: count distinct businesses and compute average rating
agg = merged.groupby('categories').agg(
    num_businesses=('business_ref', pd.Series.nunique),
    avg_rating=('rating', 'mean')
).reset_index()

# Find category with largest number of businesses
max_row = agg.sort_values(['num_businesses', 'avg_rating'], ascending=[False, False]).iloc[0]

result = {
    'business_category': max_row['categories'],
    'num_businesses_accepting_credit_cards': int(max_row['num_businesses']),
    'average_rating': round(float(max_row['avg_rating']), 3)
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_palNDytL6J5Vi3TGr1crOeiS': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_92'}], 'var_call_F5ZVPlHcTEoSXEQoTy8bauWi': 'file_storage/call_F5ZVPlHcTEoSXEQoTy8bauWi.json'}

exec(code, env_args)
