code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_FekEckYHEJU4LcfALlmJ26B8, 'r') as f:
    businesses = json.load(f)
with open(var_call_y3A2nxDih0pCWz7NwAV9bfGk, 'r') as f:
    reviews = json.load(f)

# Convert to DataFrame
df_b = pd.DataFrame(businesses)
# Ensure attributes column exists
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None

# Extract accept credit card flag and categories
def accepts_cc(attr):
    if not isinstance(attr, dict):
        return False
    v = attr.get('BusinessAcceptsCreditCards')
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    return s == 'true'

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# Some docs may have categories field; ensure presence
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Filter businesses that accept credit cards
df_cc = df_b[df_b['accepts_cc'] == True].copy()

# Expand categories
def split_cats(x):
    if x is None:
        return []
    if not isinstance(x, str):
        return []
    parts = [p.strip() for p in x.split(',') if p.strip() != '']
    return parts

# Create exploded df of business-category pairs
rows = []
for _, r in df_cc.iterrows():
    bids = r.get('business_id')
    cats = split_cats(r.get('categories'))
    for c in cats:
        rows.append({'business_id': bids, 'category': c})

if len(rows) == 0:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_pairs = pd.DataFrame(rows)
    # Count unique businesses per category
    df_unique = df_pairs.drop_duplicates(['business_id','category'])
    counts = df_unique.groupby('category').business_id.nunique().reset_index(name='business_count')
    counts = counts.sort_values(['business_count','category'], ascending=[False,True])
    top = counts.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Prepare reviews DF
    df_r = pd.DataFrame(reviews)
    # Convert rating to numeric
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = None

    # Map review.business_ref to business_id by replacing prefix
    def ref_to_bid(x):
        if not isinstance(x, str):
            return None
        if x.startswith('businessref_'):
            return 'businessid_' + x.split('businessref_')[-1]
        return x

    df_r['business_id'] = df_r['business_ref'].apply(ref_to_bid)

    # Get business_ids in top category
    biz_in_top = df_unique[df_unique['category'] == top_category]['business_id'].unique().tolist()

    # Filter reviews for these business_ids
    df_top_reviews = df_r[df_r['business_id'].isin(biz_in_top)].copy()
    # Calculate average rating across all reviews for these businesses
    if len(df_top_reviews) == 0:
        avg_rating = None
    else:
        avg_rating = float(df_top_reviews['rating'].mean())

    result = {'category': top_category, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating,4)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rOGdUkWyGCSFzHjSQs9yUcKm': ['business', 'checkin'], 'var_call_7s61UCAIDop1liwo1vPB7xQe': ['review', 'tip', 'user'], 'var_call_FekEckYHEJU4LcfALlmJ26B8': 'file_storage/call_FekEckYHEJU4LcfALlmJ26B8.json', 'var_call_y3A2nxDih0pCWz7NwAV9bfGk': 'file_storage/call_y3A2nxDih0pCWz7NwAV9bfGk.json'}

exec(code, env_args)
