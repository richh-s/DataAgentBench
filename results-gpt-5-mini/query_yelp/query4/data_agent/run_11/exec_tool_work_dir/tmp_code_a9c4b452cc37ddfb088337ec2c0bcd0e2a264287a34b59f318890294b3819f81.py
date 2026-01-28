code = """import json
import pandas as pd

# Load data from stored JSON files
with open(var_call_9lcqa0C2p1ehoGhnkxLGVTmB, 'r') as f:
    biz = json.load(f)
with open(var_call_fgTMzoFPTAhXSsJn9tUNfzGG, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(biz)
df_rev = pd.DataFrame(reviews)

# Function to determine if business accepts credit cards
def accepts_cc(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        return str(val).lower().find('true') >= 0
    s = str(attr)
    if 'BusinessAcceptsCreditCards' not in s:
        return False
    # simple heuristics: check for 'True' or 'true' after the key
    return ('True' in s) or ('true' in s)

# Apply to df_biz
if 'attributes' not in df_biz.columns:
    df_biz['attributes'] = None

df_biz['accepts_cc'] = df_biz['attributes'].apply(accepts_cc)

# Handle categories
if 'categories' not in df_biz.columns:
    df_biz['categories'] = None

def split_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [str(c).strip() for c in cat if c]
    s = str(cat)
    if s.strip().lower() in ('none', 'nan', ''):
        return []
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

# Filter businesses that accept credit cards
df_cc = df_biz[df_biz['accepts_cc'] == True].copy()

# Expand categories
rows = []
for _, r in df_cc.iterrows():
    cats = split_categories(r.get('categories'))
    if not cats:
        continue
    for c in cats:
        rows.append({'business_id': r.get('business_id'), 'category': c})

if not rows:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_cats = pd.DataFrame(rows)
    cat_counts = df_cats.groupby('category')['business_id'].nunique().reset_index(name='business_count')
    cat_counts = cat_counts.sort_values(['business_count', 'category'], ascending=[False, True]).reset_index(drop=True)
    top = cat_counts.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Get business_ids for top category
    top_biz_ids = df_cats[df_cats['category'] == top_category]['business_id'].unique().tolist()
    top_biz_refs = [bid.replace('businessid_', 'businessref_') for bid in top_biz_ids]

    # Compute average rating from reviews
    if df_rev.empty or 'business_ref' not in df_rev.columns or 'rating' not in df_rev.columns:
        avg_rating = None
    else:
        df_rev['rating_num'] = pd.to_numeric(df_rev['rating'], errors='coerce')
        df_top_reviews = df_rev[df_rev['business_ref'].isin(top_biz_refs)]
        if df_top_reviews.empty:
            avg_rating = None
        else:
            avg_rating = float(df_top_reviews['rating_num'].mean())

    result = {'category': top_category, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LhTd7FhVPoct9dTI7RhOOXAk': ['business', 'checkin'], 'var_call_sOWfkyzFYP4FkbOwQlzprD6m': ['review', 'tip', 'user'], 'var_call_9lcqa0C2p1ehoGhnkxLGVTmB': 'file_storage/call_9lcqa0C2p1ehoGhnkxLGVTmB.json', 'var_call_fgTMzoFPTAhXSsJn9tUNfzGG': 'file_storage/call_fgTMzoFPTAhXSsJn9tUNfzGG.json'}

exec(code, env_args)
