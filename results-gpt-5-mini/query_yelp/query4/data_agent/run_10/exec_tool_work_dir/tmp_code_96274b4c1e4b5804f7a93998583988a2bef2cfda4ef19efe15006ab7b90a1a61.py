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

# Normalize attributes: convert string "None" to None, ensure dicts remain dict
def parse_attributes(attr):
    if attr is None:
        return None
    if isinstance(attr, dict):
        return attr
    # attr might be a string like "None" or "{...}" or "u'...'", try to parse simple cases
    if isinstance(attr, str):
        s = attr.strip()
        if s == 'None' or s == '"None"' or s == "'None'":
            return None
        # try to eval dict-like strings safely by replacing u' with '
        if s.startswith('{'):
            try:
                # Replace Python-style unicode prefixes and single quotes to double for JSON
                s2 = s.replace("u'", "'").replace("\"", "\\\"")
                # Convert single quotes to double quotes for JSON
                s3 = s2.replace("'", '"')
                return json.loads(s3)
            except Exception:
                return None
        return None
    return None

# Apply
df_biz['attributes_parsed'] = df_biz['attributes'].apply(parse_attributes)

# Determine if business accepts credit cards
def accepts_cc(attr):
    if not isinstance(attr, dict):
        return False
    val = attr.get('BusinessAcceptsCreditCards')
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        v = val.strip().lower()
        if v in ('true', 'true\'' , '"true"'):
            return True
        if v in ('false', 'none'):
            return False
    return False

df_biz['accepts_cc'] = df_biz['attributes_parsed'].apply(accepts_cc)

# Normalize categories: if missing, try to handle; assume categories field may be present
if 'categories' not in df_biz.columns:
    df_biz['categories'] = None

# Some categories might be lists or comma-separated strings
def parse_categories(cat):
    if pd.isna(cat) or cat is None:
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        s = cat.strip()
        if s == 'None' or s == "None":
            return []
        # split by comma
        parts = [p.strip() for p in s.split(',') if p.strip()]
        return parts
    return []

# Apply parsing
df_biz['categories_parsed'] = df_biz['categories'].apply(parse_categories)

# Filter businesses that accept credit cards
df_cc = df_biz[df_biz['accepts_cc']].copy()

# Explode categories
df_cc = df_cc.explode('categories_parsed')
# Drop rows with empty category
df_cc = df_cc[df_cc['categories_parsed'].notna() & (df_cc['categories_parsed'] != "")]

# Count unique businesses per category
cat_counts = df_cc.groupby('categories_parsed')['business_id'].nunique().reset_index()
cat_counts = cat_counts.rename(columns={'categories_parsed':'category','business_id':'business_count'})

if cat_counts.empty:
    result = {'category': None, 'business_count': 0, 'average_rating': None}
else:
    # find category with max count
    max_count = cat_counts['business_count'].max()
    top_cats = cat_counts[cat_counts['business_count']==max_count].sort_values('category')
    top_cat = top_cats.iloc[0]['category']
    top_count = int(top_cats.iloc[0]['business_count'])

    # Prepare reviews: convert rating to numeric and map businessref to businessid
    df_rev = df_rev.dropna(subset=['business_ref'])
    df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
    df_rev = df_rev.dropna(subset=['rating'])
    df_rev['business_id'] = df_rev['business_ref'].str.replace('businessref_','businessid_')

    # Get list of business_ids in top category
    biz_ids_in_cat = df_cc[df_cc['categories_parsed']==top_cat]['business_id'].unique().tolist()

    # Filter reviews for these businesses
    df_rev_cat = df_rev[df_rev['business_id'].isin(biz_ids_in_cat)].copy()

    if df_rev_cat.empty:
        avg_rating = None
    else:
        avg_rating = float(df_rev_cat['rating'].mean())

    result = {'category': top_cat, 'business_count': top_count, 'average_rating': None if avg_rating is None else round(avg_rating, 3)}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6FU7kBcN06qZSAs1ZtN8NF87': ['business', 'checkin'], 'var_call_omKwTvAxZYsyy8pP1giAqkKq': ['review', 'tip', 'user'], 'var_call_BNfPlXFrji3oZk83tN7Nfhlh': 'file_storage/call_BNfPlXFrji3oZk83tN7Nfhlh.json', 'var_call_JQL7Y5PXp0wYe9As4GOYFNil': 'file_storage/call_JQL7Y5PXp0wYe9As4GOYFNil.json'}

exec(code, env_args)
