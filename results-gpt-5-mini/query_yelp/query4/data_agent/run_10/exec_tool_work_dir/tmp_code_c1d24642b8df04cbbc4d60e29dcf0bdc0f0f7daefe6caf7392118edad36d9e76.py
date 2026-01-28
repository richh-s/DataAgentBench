code = """import json
import pandas as pd

# Load data from previous tool results
with open(var_call_BNfPlXFrji3oZk83tN7Nfhlh, 'r') as f:
    businesses = json.load(f)
with open(var_call_JQL7Y5PXp0wYe9As4GOYFNil, 'r') as f:
    reviews = json.load(f)

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Simple function to detect if accepts credit cards
def accepts_cc_simple(attr):
    if attr is None:
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.strip().lower() == 'true'
        return False
    if isinstance(attr, str):
        s = attr.lower()
        # check patterns
        if 'businessacceptscreditcards' in s and 'true' in s:
            return True
        return False
    return False

# Apply
if 'attributes' not in df_biz.columns:
    df_biz['attributes'] = None

df_biz['accepts_cc'] = df_biz['attributes'].apply(accepts_cc_simple)

# Parse categories
if 'categories' not in df_biz.columns:
    df_biz['categories'] = None

def parse_categories(cat):
    if cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        s = cat.strip()
        if s == '' or s.lower() == 'none':
            return []
        return [p.strip() for p in s.split(',') if p.strip()]
    return []

df_biz['categories_parsed'] = df_biz['categories'].apply(parse_categories)

# Filter businesses that accept credit cards
df_cc = df_biz[df_biz['accepts_cc']].copy()

# Explode categories
if not df_cc.empty:
    df_cc = df_cc.explode('categories_parsed')
    df_cc = df_cc[df_cc['categories_parsed'].notna() & (df_cc['categories_parsed'] != '')]

# Count unique businesses per category
if df_cc.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    cat_counts = df_cc.groupby('categories_parsed')['business_id'].nunique().reset_index()
    cat_counts = cat_counts.rename(columns={'categories_parsed':'category','business_id':'business_count'})
    max_count = int(cat_counts['business_count'].max())
    top_cats = cat_counts[cat_counts['business_count']==max_count].sort_values('category')
    top_cat = top_cats.iloc[0]['category']
    top_count = int(top_cats.iloc[0]['business_count'])

    # Prepare reviews
    if df_rev.empty:
        avg_rating = None
    else:
        df_rev = df_rev.dropna(subset=['business_ref'])
        df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
        df_rev = df_rev.dropna(subset=['rating'])
        df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_','businessid_')

        # businesses in top category
        biz_ids_in_cat = df_cc[df_cc['categories_parsed']==top_cat]['business_id'].unique().tolist()
        df_rev_cat = df_rev[df_rev['business_id'].isin(biz_ids_in_cat)].copy()
        if df_rev_cat.empty:
            avg_rating = None
        else:
            avg_rating = float(df_rev_cat['rating'].mean())

    result = {'category': top_cat, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6FU7kBcN06qZSAs1ZtN8NF87': ['business', 'checkin'], 'var_call_omKwTvAxZYsyy8pP1giAqkKq': ['review', 'tip', 'user'], 'var_call_BNfPlXFrji3oZk83tN7Nfhlh': 'file_storage/call_BNfPlXFrji3oZk83tN7Nfhlh.json', 'var_call_JQL7Y5PXp0wYe9As4GOYFNil': 'file_storage/call_JQL7Y5PXp0wYe9As4GOYFNil.json'}

exec(code, env_args)
