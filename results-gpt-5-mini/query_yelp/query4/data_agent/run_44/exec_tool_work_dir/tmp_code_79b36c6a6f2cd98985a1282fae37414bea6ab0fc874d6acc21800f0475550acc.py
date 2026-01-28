code = """import json
import pandas as pd
import re

# Load data
with open(var_call_1vCVrSc3c2QdSudm9mXP66rw, 'r') as f:
    businesses = json.load(f)
with open(var_call_nnzZmlMsxerc5X0sauGx54mf, 'r') as f:
    reviews = json.load(f)

# Function to determine if accepts credit cards
def accepts_credit(attrs):
    if attrs is None:
        return False
    if isinstance(attrs, dict):
        v = attrs.get('BusinessAcceptsCreditCards')
        if v is None:
            return False
        return str(v).lower() == 'true'
    if isinstance(attrs, str):
        if attrs == 'None':
            return False
        # look for patterns like BusinessAcceptsCreditCards': 'True' or "BusinessAcceptsCreditCards: True"
        patterns = [r"BusinessAcceptsCreditCards\s*[":=]\s*'?\"?(True|False|None)\"?'",
                    r"['\"]BusinessAcceptsCreditCards['\"]\s*:\s*['\"]?(True|False|None)['\"]?"]
        for pat in patterns:
            m = re.search(pat, attrs)
            if m:
                return m.group(1).lower() == 'true'
        # fallback: check if the substring "BusinessAcceptsCreditCards" and "True" appear
        if 'BusinessAcceptsCreditCards' in attrs and 'True' in attrs:
            return True
        return False
    return False

# Build dataframe
rows = []
for b in businesses:
    bid = b.get('business_id')
    attrs = b.get('attributes')
    cats = b.get('categories', None)
    # normalize categories
    if isinstance(cats, list):
        cat_list = [c.strip() for c in cats if c]
    elif isinstance(cats, str):
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    else:
        cat_list = []
    rows.append({'business_id': bid, 'attributes': attrs, 'accepts_cc': accepts_credit(attrs), 'categories': cat_list})

biz_df = pd.DataFrame(rows)
cc_biz = biz_df[biz_df['accepts_cc'] == True].copy()

# Explode categories
if not cc_biz.empty:
    cc_biz_exploded = cc_biz.explode('categories')
    cc_biz_exploded['categories'] = cc_biz_exploded['categories'].fillna('Unknown')
else:
    cc_biz_exploded = cc_biz.copy()

# Count unique businesses per category
if not cc_biz_exploded.empty:
    cat_counts = cc_biz_exploded.groupby('categories')['business_id'].nunique().reset_index(name='biz_count')
    cat_counts = cat_counts.sort_values('biz_count', ascending=False)
else:
    cat_counts = pd.DataFrame(columns=['categories','biz_count'])

# Load reviews
rev_df = pd.DataFrame(reviews)
if 'rating' in rev_df.columns:
    rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')
else:
    rev_df['rating'] = pd.Series(dtype='float')

# Determine top category
if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    top_count = int(cat_counts['biz_count'].max())
    top_categories = cat_counts[cat_counts['biz_count'] == top_count]['categories'].tolist()
    top_category = sorted(top_categories)[0]
    biz_ids_in_cat = cc_biz_exploded[cc_biz_exploded['categories'] == top_category]['business_id'].unique().tolist()
    biz_refs = [b.replace('businessid_', 'businessref_') for b in biz_ids_in_cat]
    revs_for_cat = rev_df[rev_df['business_ref'].isin(biz_refs)]
    if revs_for_cat.empty:
        avg_rating = None
    else:
        avg_rating = round(float(revs_for_cat['rating'].mean()), 2)
    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg_rating}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1vCVrSc3c2QdSudm9mXP66rw': 'file_storage/call_1vCVrSc3c2QdSudm9mXP66rw.json', 'var_call_nnzZmlMsxerc5X0sauGx54mf': 'file_storage/call_nnzZmlMsxerc5X0sauGx54mf.json', 'var_call_U7mTtNYY1BCQAR4C4pE0cmY5': ['checkin', 'business']}

exec(code, env_args)
