code = """import json
import pandas as pd

# Load business data
data_path = var_call_uM66o8gfxRMsPZNM2Vbl26Cj
if isinstance(data_path, str):
    with open(data_path, 'r') as f:
        businesses = json.load(f)
else:
    businesses = data_path

# Load reviews data
rev_path = var_call_rx4eFEGYXvzUp1nrbfdgwYXF
if isinstance(rev_path, str):
    with open(rev_path, 'r') as f:
        reviews = json.load(f)
else:
    reviews = rev_path

# Create DataFrame
bdf = pd.DataFrame(businesses)
rdf = pd.DataFrame(reviews)

# Normalize attributes: ensure dict or None
def accepts_cc(attr):
    if attr is None:
        return False
    # sometimes attributes stored as string 'None'
    if isinstance(attr, str):
        if attr.lower() == 'none':
            return False
        try:
            # attempt to parse string-formatted dict
            parsed = eval(attr)
            attr = parsed
        except Exception:
            return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            # sometimes nested or different casing
            for k in attr.keys():
                if k.lower() == 'businessacceptscreditcards':
                    val = attr[k]
                    break
        if val is None:
            return False
        # value may be boolean or string
        if isinstance(val, bool):
            return val
        if isinstance(val, (int, float)):
            return bool(val)
        if isinstance(val, str):
            return val.strip().lower() == 'true'
    return False

bdf['accepts_cc'] = bdf['attributes'].apply(accepts_cc)

# Parse categories into list
def parse_categories(x):
    if x is None:
        return []
    if isinstance(x, list):
        return [str(i).strip() for i in x if i]
    if isinstance(x, str):
        if x.lower() == 'none':
            return []
        # split by comma
        parts = [part.strip() for part in x.split(',')]
        return [p for p in parts if p]
    return []

if 'categories' not in bdf.columns:
    bdf['categories'] = None

bdf['categories_list'] = bdf['categories'].apply(parse_categories)

# Explode categories for counting
exploded = bdf[bdf['accepts_cc']].explode('categories_list')
exploded = exploded[exploded['categories_list'].notnull() & (exploded['categories_list'] != '')]

# Count businesses per category (unique business_id counts)
counts = exploded.groupby('categories_list')['business_id'].nunique().reset_index()
counts = counts.rename(columns={'categories_list':'category','business_id':'business_count'})
counts_sorted = counts.sort_values(['business_count','category'], ascending=[False, True])

if counts_sorted.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top = counts_sorted.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Get businesses in this category that accept cc
    top_businesses = exploded[exploded['categories_list'] == top_category]['business_id'].unique().tolist()

    # Map business_id to business_ref
    def bizid_to_ref(bid):
        if not isinstance(bid, str):
            return None
        parts = bid.split('_',1)
        if len(parts) == 2:
            return 'businessref_' + parts[1]
        return None

    top_refs = set(bizid_to_ref(b) for b in top_businesses)
    # Filter reviews for these refs
    rdf_filtered = rdf[rdf['business_ref'].isin(top_refs)].copy()
    # Convert rating to numeric
    if not rdf_filtered.empty:
        rdf_filtered['rating'] = pd.to_numeric(rdf_filtered['rating'], errors='coerce')
        avg_rating = rdf_filtered['rating'].mean()
        # round to 2 decimals
        avg_rating = round(float(avg_rating), 2)
    else:
        avg_rating = None

    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg_rating}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qKe6K9xSeTMnrKra3a4TBAVv': ['checkin', 'business'], 'var_call_x5ANzylX9WGMppdPR142hyW8': ['review', 'tip', 'user'], 'var_call_uM66o8gfxRMsPZNM2Vbl26Cj': 'file_storage/call_uM66o8gfxRMsPZNM2Vbl26Cj.json', 'var_call_rx4eFEGYXvzUp1nrbfdgwYXF': 'file_storage/call_rx4eFEGYXvzUp1nrbfdgwYXF.json'}

exec(code, env_args)
