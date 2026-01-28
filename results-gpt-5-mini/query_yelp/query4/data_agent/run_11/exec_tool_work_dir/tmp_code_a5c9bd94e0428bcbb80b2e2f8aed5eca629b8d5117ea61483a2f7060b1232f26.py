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

# Normalize attributes: some are None or strings
def accepts_cc(attr):
    if attr is None:
        return False
    # If it's a dict
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
    else:
        # Could be string like "None" or "{...}" or other
        # Try to handle the case where attributes is a string representation containing the key
        try:
            # if it's string, attempt to eval safe-ish by checking substring
            s = str(attr)
            if 'BusinessAcceptsCreditCards' in s:
                # find the part after key
                # This is heuristic: look for BusinessAcceptsCreditCards': 'True' or BusinessAcceptsCreditCards": "True"
                import re
                m = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?(True|False|true|false)['\"]?", s)
                if m:
                    val = m.group(1)
                else:
                    # maybe like "BusinessAcceptsCreditCards': True"
                    m2 = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*(True|False|true|false)", s)
                    if m2:
                        val = m2.group(1)
                    else:
                        val = None
            else:
                val = None
        except Exception:
            val = None
    if val is None:
        return False
    return str(val).lower().find('true') >= 0

# Apply to df_biz
# Some docs may have 'attributes' missing
if 'attributes' not in df_biz.columns:
    df_biz['attributes'] = None

df_biz['accepts_cc'] = df_biz['attributes'].apply(accepts_cc)

# Extract categories: some entries might have 'categories' field missing
if 'categories' not in df_biz.columns:
    df_biz['categories'] = None

# Normalize categories into list
def split_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [str(c).strip() for c in cat if c]
    s = str(cat)
    if s.strip() == 'None' or s.strip() == "nan":
        return []
    # Split by comma
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

from itertools import chain

# Filter businesses that accept credit cards
df_cc = df_biz[df_biz['accepts_cc'] == True].copy()

# Expand categories
rows = []
for _, r in df_cc.iterrows():
    cats = split_categories(r.get('categories'))
    # If no categories, we can skip
    if not cats:
        continue
    for c in cats:
        rows.append({'business_id': r.get('business_id'), 'category': c})

if not rows:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    df_cats = pd.DataFrame(rows)
    # Count unique businesses per category
    cat_counts = df_cats.groupby('category')['business_id'].nunique().reset_index()
    cat_counts = cat_counts.sort_values(['business_id', 'category'], ascending=[False, True])
    top = cat_counts.iloc[0]
    top_category = top['category']
    top_count = int(top['business_id'])

    # Map business_id to business_ref
    df_cc_ids = df_cc[['business_id']].dropna().drop_duplicates()
    df_cc_ids['business_ref'] = df_cc_ids['business_id'].astype(str).str.replace('businessid_', 'businessref_')

    # Determine business_refs in top category
    top_biz_ids = df_cats[df_cats['category'] == top_category]['business_id'].unique().tolist()
    top_biz_refs = [bid.replace('businessid_', 'businessref_') for bid in top_biz_ids]

    # Filter reviews for these business_refs
    if df_rev.empty:
        avg_rating = None
    else:
        if 'business_ref' not in df_rev.columns or 'rating' not in df_rev.columns:
            avg_rating = None
        else:
            # Convert rating to numeric where possible
            df_rev['rating_num'] = pd.to_numeric(df_rev['rating'], errors='coerce')
            df_top_reviews = df_rev[df_rev['business_ref'].isin(top_biz_refs)]
            if df_top_reviews.empty:
                avg_rating = None
            else:
                avg_rating = float(df_top_reviews['rating_num'].mean())

    result = {'category': top_category, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LhTd7FhVPoct9dTI7RhOOXAk': ['business', 'checkin'], 'var_call_sOWfkyzFYP4FkbOwQlzprD6m': ['review', 'tip', 'user'], 'var_call_9lcqa0C2p1ehoGhnkxLGVTmB': 'file_storage/call_9lcqa0C2p1ehoGhnkxLGVTmB.json', 'var_call_fgTMzoFPTAhXSsJn9tUNfzGG': 'file_storage/call_fgTMzoFPTAhXSsJn9tUNfzGG.json'}

exec(code, env_args)
