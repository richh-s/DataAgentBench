code = """import json
import pandas as pd
import re

# Load data files from previous tool calls
with open(var_call_5u72CFr6RYHT6MZ5xk6hTNx, 'r') as f:
    businesses = json.load(f)
with open(var_call_pPOFbEeTYqEA9ypm58fbm9eV, 'r') as f:
    reviews = json.load(f)

# DataFrames
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Helper to determine if business accepts credit cards
def accepts_credit(attrs):
    if attrs is None:
        return False
    # If it's a dict
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if val is None:
            return False
        s = str(val)
        return s.lower() == 'true'
    # Otherwise treat as string
    s = str(attrs)
    # Quick check for keywords
    if 'BusinessAcceptsCreditCards' not in s:
        return False
    # regex to capture True/False/None
    m = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?([Tt]rue|[Ff]alse|None)['\"]?", s)
    if m:
        val = m.group(1)
        return val.lower() == 'true'
    # fallback: check for substring "BusinessAcceptsCreditCards': 'True'"
    return 'BusinessAcceptsCreditCards' in s and 'True' in s

# Determine accepting credit card businesses
bdf['_accepts_cc'] = bdf['attributes'].apply(accepts_credit)
# Ensure business_id exists
bdf = bdf.dropna(subset=['business_id'])

# Parse categories into list
def parse_categories(c):
    if pd.isna(c):
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    s = str(c)
    if s.strip() == '' or s.lower() == 'none':
        return []
    # Categories may be a comma-separated string
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

if 'categories' not in bdf.columns:
    # If categories field missing, add empty
    bdf['categories'] = None

bdf['_categories_list'] = bdf['categories'].apply(parse_categories)

# Expand categories for businesses that accept credit cards
acc_df = bdf[bdf['_accepts_cc']].copy()
acc_expanded = acc_df[['business_id','name','_categories_list']].explode('_categories_list')
acc_expanded = acc_expanded.rename(columns={'_categories_list':'category'})
acc_expanded = acc_expanded[~acc_expanded['category'].isna()]

# Count businesses per category (unique business_id per category)
cat_counts = acc_expanded.groupby('category')['business_id'].nunique().reset_index(name='business_count')
if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # Find top category
    top = cat_counts.sort_values(['business_count','category'], ascending=[False, True]).iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Build mapping from review.business_ref to business_id by replacing prefix
    def ref_to_bid(ref):
        if ref is None:
            return None
        return str(ref).replace('businessref_','businessid_')

    rdf['business_id'] = rdf['business_ref'].apply(ref_to_bid)
    rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')

    # Get set of business_ids in top category
    top_bids = set(acc_expanded[acc_expanded['category']==top_category]['business_id'].unique())
    # Filter reviews for those business ids
    relevant_reviews = rdf[rdf['business_id'].isin(top_bids) & rdf['rating'].notna()]

    if relevant_reviews.empty:
        avg_rating = None
    else:
        avg_rating = round(float(relevant_reviews['rating'].mean()), 2)

    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_33tJdYSKyPvqCFR6GBOv64VT': ['checkin', 'business'], 'var_call_0RUxKzrFEwaCMBIFUgyyM9Wi': ['review', 'tip', 'user'], 'var_call_5u72CFr6RYHT6MZ5xk6hTNxq': 'file_storage/call_5u72CFr6RYHT6MZ5xk6hTNxq.json', 'var_call_pPOFbEeTYqEA9ypm58fbm9eV': 'file_storage/call_pPOFbEeTYqEA9ypm58fbm9eV.json'}

exec(code, env_args)
