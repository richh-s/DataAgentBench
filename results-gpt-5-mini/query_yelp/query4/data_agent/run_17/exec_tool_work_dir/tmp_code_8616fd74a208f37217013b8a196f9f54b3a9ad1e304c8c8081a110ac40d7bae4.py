code = """import json
import pandas as pd
import re

# Load data from storage file paths
with open(var_call_KL7fiKyfNIubTLwwzh6YGblR, 'r', encoding='utf-8') as f:
    businesses = json.load(f)
with open(var_call_oedosZ32xU5OrmgRvz9Fd1bh, 'r', encoding='utf-8') as f:
    reviews = json.load(f)

# Create DataFrames
df_b = pd.DataFrame(businesses)
# ensure columns
if 'business_id' not in df_b.columns:
    df_b['business_id'] = None
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Function to detect BusinessAcceptsCreditCards
def accepts_credit(attr):
    if attr is None:
        return False
    # If it's a dict
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.strip().lower() == 'true'
        return False
    # If it's a string representation
    if isinstance(attr, str):
        s = attr
        if 'BusinessAcceptsCreditCards' not in s:
            return False
        # Try to find True/False after the key
        m = re.search(r"BusinessAcceptsCreditCards\s*[:=]\s*['\"]?(True|False|true|false)['\"]?", s)
        if m:
            return m.group(1).lower() == 'true'
        # fallback: if 'BusinessAcceptsCreditCards' and 'True' both in string
        return ('BusinessAcceptsCreditCards' in s) and ('True' in s)
    return False

# Apply
df_b['accepts_cc'] = df_b['attributes'].apply(accepts_credit)

# Parse categories into list
def parse_cats(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x]
    if isinstance(c, str):
        # some entries might be like "Food, Restaurants"
        parts = [p.strip() for p in c.split(',')]
        return [p for p in parts if p]
    return []

df_b['category_list'] = df_b['categories'].apply(parse_cats)

# Filter businesses that accept credit cards
df_cc = df_b[df_b['accepts_cc'] == True].copy()

# Expand categories
rows = []
for _, r in df_cc.iterrows():
    bids = r.get('business_id')
    cats = r.get('category_list') or []
    if not cats:
        # treat no category as 'Unknown'
        rows.append({'business_id': bids, 'category': None})
    else:
        for c in cats:
            rows.append({'business_id': bids, 'category': c})

df_cat = pd.DataFrame(rows)
if df_cat.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # Count unique businesses per category
    grp = df_cat.groupby('category').agg(business_count=('business_id', pd.Series.nunique)).reset_index()
    # find top category (if ties, choose first by descending count)
    grp = grp.sort_values(['business_count','category'], ascending=[False, True])
    top = grp.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Load reviews into DataFrame
    df_r = pd.DataFrame(reviews)
    # ensure columns
    if 'business_ref' not in df_r.columns:
        df_r['business_ref'] = None
    if 'rating' not in df_r.columns:
        df_r['rating'] = None

    # map business_ref to business_id
    def map_ref(br):
        if br is None:
            return None
        return br.replace('businessref_', 'businessid_')

    df_r['business_id'] = df_r['business_ref'].apply(map_ref)
    # convert rating to numeric
    df_r['rating_num'] = pd.to_numeric(df_r['rating'], errors='coerce')

    # find business ids that are in top category
    biz_in_top = set(df_cat[df_cat['category'] == top_category]['business_id'].unique())

    # filter reviews for those businesses
    relevant_reviews = df_r[df_r['business_id'].isin(biz_in_top) & df_r['rating_num'].notna()]
    if relevant_reviews.empty:
        avg_rating = None
    else:
        avg_rating = float(relevant_reviews['rating_num'].mean())
        # round to 2 decimals
        avg_rating = round(avg_rating, 2)

    result = {'category': top_category, 'business_count': top_count, 'average_rating': avg_rating}

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JnLluO3On3Gk0xm04Vc0e2av': ['business', 'checkin'], 'var_call_tz5knKhzNxFLrxjC90GMIKSe': ['review', 'tip', 'user'], 'var_call_KL7fiKyfNIubTLwwzh6YGblR': 'file_storage/call_KL7fiKyfNIubTLwwzh6YGblR.json', 'var_call_oedosZ32xU5OrmgRvz9Fd1bh': 'file_storage/call_oedosZ32xU5OrmgRvz9Fd1bh.json'}

exec(code, env_args)
