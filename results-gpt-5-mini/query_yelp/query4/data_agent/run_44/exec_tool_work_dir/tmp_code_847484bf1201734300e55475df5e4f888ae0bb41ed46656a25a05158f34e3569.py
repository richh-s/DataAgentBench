code = """import json
import pandas as pd
import re

# Load data from storage-provided file paths
with open(var_call_1vCVrSc3c2QdSudm9mXP66rw, 'r') as f:
    businesses = json.load(f)
with open(var_call_nnzZmlMsxerc5X0sauGx54mf, 'r') as f:
    reviews = json.load(f)

# Helper to detect if business accepts credit cards
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        return str(v).lower() == 'true'
    if isinstance(attrs, str):
        s = attrs
        if s == 'None':
            return False
        # try to find occurrence of BusinessAcceptsCreditCards and its value
        m = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?(True|False|None)['\"]?", s)
        if not m:
            # try with python dict style with key in quotes
            m = re.search(r"['\"]BusinessAcceptsCreditCards['\"]\s*:\s*['\"]?(True|False|None)['\"]?", s)
        if m:
            val = m.group(1)
            return str(val).lower() == 'true'
        return False
    return False

# Build dataframe for businesses
biz_rows = []
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    cats = b.get('categories') if 'categories' in b else None
    # normalize categories
    if isinstance(cats, list):
        cat_list = [c.strip() for c in cats if c]
    elif isinstance(cats, str):
        # split by comma
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    else:
        cat_list = []
    biz_rows.append({'business_id': bid, 'attributes': attrs, 'accepts_cc': accepts_credit(attrs), 'categories': cat_list})

biz_df = pd.DataFrame(biz_rows)
# Filter to businesses that accept credit cards
cc_biz = biz_df[biz_df['accepts_cc'] == True].copy()

# Explode categories
cc_biz_exploded = cc_biz.explode('categories')
cc_biz_exploded['categories'] = cc_biz_exploded['categories'].fillna('Unknown')

# Count unique businesses per category
cat_counts = cc_biz_exploded.groupby('categories')['business_id'].nunique().reset_index(name='biz_count')
cat_counts = cat_counts.sort_values('biz_count', ascending=False)

# Load reviews into dataframe
rev_df = pd.DataFrame(reviews)
# ensure rating numeric
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

# Map business_id to business_ref
# Create mapping for businesses that accept cc
cc_biz['business_ref'] = cc_biz['business_id'].str.replace('businessid_', 'businessref_')

# Find top category (largest number of businesses)
if cat_counts.shape[0] == 0:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_count = cat_counts['biz_count'].max()
    top_categories = cat_counts[cat_counts['biz_count'] == top_count]['categories'].tolist()
    # If multiple categories tie, pick the first alphabetically
    top_category = sorted(top_categories)[0]
    # Get business_ids in this category
    biz_ids_in_cat = cc_biz_exploded[cc_biz_exploded['categories'] == top_category]['business_id'].unique().tolist()
    # Convert to business_ref
    biz_refs_in_cat = [b.replace('businessid_', 'businessref_') for b in biz_ids_in_cat]
    # Filter reviews for these refs
    revs_for_cat = rev_df[rev_df['business_ref'].isin(biz_refs_in_cat)]
    if len(revs_for_cat) == 0:
        avg_rating = None
    else:
        avg_rating = float(revs_for_cat['rating'].mean())
    result = {'category': top_category, 'business_count': int(top_count), 'average_rating': None if avg_rating is None else round(avg_rating, 2)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_1vCVrSc3c2QdSudm9mXP66rw': 'file_storage/call_1vCVrSc3c2QdSudm9mXP66rw.json', 'var_call_nnzZmlMsxerc5X0sauGx54mf': 'file_storage/call_nnzZmlMsxerc5X0sauGx54mf.json', 'var_call_U7mTtNYY1BCQAR4C4pE0cmY5': ['checkin', 'business']}

exec(code, env_args)
