code = """import json
import pandas as pd

# Load data from storage file paths
with open(var_call_6nqTs8j0jeEpDA6Cqp0UwlOf, 'r', encoding='utf-8') as f:
    biz_list = json.load(f)
with open(var_call_9mtxxbPNCG8ojm4K6oHPPUUw, 'r', encoding='utf-8') as f:
    reviews_list = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(biz_list)
df_rev = pd.DataFrame(reviews_list)

# Normalize columns
if 'business_id' not in df_biz.columns:
    df_biz['business_id'] = df_biz['_id']

# Function to detect credit card acceptance
def accepts_credit(attrs):
    if attrs is None:
        return False
    # Sometimes attrs is the string 'None'
    if isinstance(attrs, str):
        if attrs.strip().lower() == 'none':
            return False
        # If it's a string representation of a dict, check for key and True
        if 'BusinessAcceptsCreditCards' in attrs:
            # crude check for True
            if 'True' in attrs or "'True'" in attrs or 'true' in attrs.lower():
                return True
            else:
                return False
        return False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is None:
            return False
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.strip().lower() == 'true'
        return False
    return False

# Apply
df_biz['accepts_credit'] = df_biz.get('attributes').apply(accepts_credit)

# Parse categories: may be missing, None, list, or comma-separated string
def parse_categories(c):
    if c is None:
        return []
    if isinstance(c, list):
        return [str(x).strip() for x in c if x is not None]
    if isinstance(c, str):
        s = c.strip()
        if s == 'None' or s == '':
            return []
        # Split on comma
        parts = [p.strip() for p in s.split(',') if p.strip()]
        return parts
    return []

if 'categories' in df_biz.columns:
    df_biz['categories_parsed'] = df_biz['categories'].apply(parse_categories)
else:
    df_biz['categories_parsed'] = [[] for _ in range(len(df_biz))]

# Filter businesses that accept credit cards
df_accept = df_biz[df_biz['accepts_credit']].copy()

# Map business_id to business_ref
def to_businessref(bid):
    if not isinstance(bid, str):
        return bid
    if bid.startswith('businessid_'):
        return 'businessref_' + bid.split('businessid_')[-1]
    return bid

df_accept['business_ref'] = df_accept['business_id'].apply(to_businessref)

# Explode categories
df_expl = df_accept[['business_ref', 'categories_parsed']].explode('categories_parsed')
df_expl = df_expl.rename(columns={'categories_parsed': 'category'})
# Drop empty categories
df_expl = df_expl[df_expl['category'].notna() & (df_expl['category'] != '')]

# If no categories found, handle
if df_expl.empty:
    result = {'top_category': None, 'business_count': 0, 'average_rating': None}
else:
    # Count distinct businesses per category
    grp = df_expl.groupby('category')['business_ref'].nunique().reset_index()
    grp = grp.rename(columns={'business_ref': 'business_count'})
    grp = grp.sort_values(['business_count', 'category'], ascending=[False, True])
    top_row = grp.iloc[0]
    top_category = top_row['category']
    business_count = int(top_row['business_count'])

    # Filter business_refs for top category
    top_business_refs = df_expl[df_expl['category'] == top_category]['business_ref'].unique().tolist()

    # Prepare reviews df
    if not df_rev.empty:
        df_rev = df_rev[df_rev['business_ref'].notna()].copy()
        df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
        # Filter reviews for businesses in top category
        df_top_reviews = df_rev[df_rev['business_ref'].isin(top_business_refs)]
        if df_top_reviews.empty:
            avg_rating = None
        else:
            avg_rating = float(df_top_reviews['rating'].mean())
    else:
        avg_rating = None

    result = {'top_category': top_category, 'business_count': business_count, 'average_rating': None if avg_rating is None else round(avg_rating, 4)}

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_k7Hlv7AKTUJmYH5ofnVZthTS': ['checkin', 'business'], 'var_call_cn8vrQmfadYO7EE2IGbovTo1': ['review', 'tip', 'user'], 'var_call_6nqTs8j0jeEpDA6Cqp0UwlOf': 'file_storage/call_6nqTs8j0jeEpDA6Cqp0UwlOf.json', 'var_call_9mtxxbPNCG8ojm4K6oHPPUUw': 'file_storage/call_9mtxxbPNCG8ojm4K6oHPPUUw.json'}

exec(code, env_args)
