code = """import json
import pandas as pd

# Load the query results from storage variables (file paths)
businesses_path = var_call_5kJVrgXIvN0Edazsc7HFYBgI
reviews_path = var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g

with open(businesses_path, 'r') as f:
    businesses = json.load(f)
with open(reviews_path, 'r') as f:
    reviews = json.load(f)

# Create DataFrame for businesses
df_b = pd.DataFrame(businesses)
# Ensure categories column exists
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Normalize categories: split by comma into list, handle None
def split_categories(x):
    if not x or x is None:
        return []
    # sometimes categories may be list already; handle strings
    if isinstance(x, list):
        # join list items if they are strings
        cats = []
        for it in x:
            if isinstance(it, str):
                parts = [p.strip() for p in it.split(',') if p.strip()]
                cats.extend(parts)
        return cats
    if isinstance(x, str):
        parts = [p.strip() for p in x.split(',') if p.strip()]
        return parts
    return []

# Expand categories
df_b['category_list'] = df_b['categories'].apply(split_categories)
# Explode
df_expl = df_b.explode('category_list')
# Drop rows with no category
df_expl = df_expl[df_expl['category_list'].notna()]
# Rename for clarity
df_expl = df_expl.rename(columns={'category_list': 'category'})

# Count unique businesses per category
cat_counts = df_expl.groupby('category')['business_id'].nunique().reset_index()
cat_counts = cat_counts.rename(columns={'business_id': 'business_count'})
# If there are no categories, handle
if cat_counts.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    # find top category by count (ties: pick first by descending count then alphabetically)
    cat_counts = cat_counts.sort_values(by=['business_count', 'category'], ascending=[False, True])
    top = cat_counts.iloc[0]
    top_category = top['category']
    top_count = int(top['business_count'])

    # Prepare set of business_ids in this category
    biz_ids_in_cat = set(df_expl[df_expl['category'] == top_category]['business_id'].unique())

    # Load reviews into DataFrame
    df_r = pd.DataFrame(reviews)
    # Convert rating to numeric
    if 'rating' in df_r.columns:
        df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
    else:
        df_r['rating'] = pd.Series(dtype='float')

    # Map business_ref to business_id by replacing prefix
    def ref_to_id(ref):
        if not isinstance(ref, str):
            return None
        return ref.replace('businessref_', 'businessid_')

    df_r['business_id'] = df_r['business_ref'].apply(ref_to_id)

    # Filter reviews for businesses in category
    df_r_cat = df_r[df_r['business_id'].isin(biz_ids_in_cat)]

    if df_r_cat.empty:
        avg_rating = None
    else:
        avg_rating = float(df_r_cat['rating'].mean())

    result = {"category": top_category, "business_count": top_count, "average_rating": (None if avg_rating is None else round(avg_rating, 2))}

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NeumhbNtYh7RIqIMjxGLdY3e': ['checkin', 'business'], 'var_call_yJeK0J3aYKtbIkDeETPJZWaP': ['review', 'tip', 'user'], 'var_call_5kJVrgXIvN0Edazsc7HFYBgI': 'file_storage/call_5kJVrgXIvN0Edazsc7HFYBgI.json', 'var_call_QYZaFbgIPmrqZ0Z5w0n7PI7g': 'file_storage/call_QYZaFbgIPmrqZ0Z5w0n7PI7g.json'}

exec(code, env_args)
