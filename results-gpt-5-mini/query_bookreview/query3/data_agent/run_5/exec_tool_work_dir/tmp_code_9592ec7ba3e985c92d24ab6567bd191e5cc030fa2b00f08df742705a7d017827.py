code = """import json
import pandas as pd
import re
import ast

# Load data from storage-provided file paths
with open(var_call_Cw1mmm6Dq10hFgi6XAE0NJkB, 'r', encoding='utf-8') as f:
    reviews = json.load(f)
with open(var_call_w3Z6TbDgMEr1ZtpmNVhxTv9z, 'r', encoding='utf-8') as f:
    books = json.load(f)

# Create DataFrame for reviews
df_reviews = pd.DataFrame(reviews)
# Keep relevant columns and clean
if 'rating' in df_reviews.columns:
    df_reviews = df_reviews[['purchase_id', 'rating', 'review_time']].copy()
else:
    df_reviews = df_reviews.copy()

# Convert rating to float, drop rows with invalid ratings
def to_float(x):
    try:
        return float(x)
    except:
        return None

df_reviews['rating'] = df_reviews['rating'].apply(to_float)
df_reviews = df_reviews.dropna(subset=['rating'])

# Ensure review_time is string and filter from 2020-01-01 just in case
df_reviews['review_time'] = df_reviews['review_time'].astype(str)
df_reviews = df_reviews[df_reviews['review_time'] >= '2020-01-01']

# Group by purchase_id to compute average rating and count
grp = df_reviews.groupby('purchase_id').rating.agg(['mean','count']).reset_index()
grp = grp.rename(columns={'mean':'avg_rating','count':'review_count'})

# Create DataFrame for books
df_books = pd.DataFrame(books)
# Parse categories field which is stored as string representation of list
def parse_categories(cat_str):
    if not isinstance(cat_str, str):
        return []
    try:
        # First try json
        return json.loads(cat_str)
    except:
        try:
            return ast.literal_eval(cat_str)
        except:
            # fallback: find substrings
            return []

if 'categories' in df_books.columns:
    df_books['categories_parsed'] = df_books['categories'].apply(parse_categories)
else:
    df_books['categories_parsed'] = [[] for _ in range(len(df_books))]

# Identify books that have "Children's Books" in categories
def is_childrens(cats):
    if not isinstance(cats, list):
        return False
    return any((c.strip() == "Children's Books") for c in cats)

df_books['is_childrens'] = df_books['categories_parsed'].apply(is_childrens)
children_books = df_books[df_books['is_childrens']].copy()

# Extract numeric id from book_id and build corresponding purchase_id
def extract_suffix_id(s):
    if not isinstance(s, str):
        return None
    m = re.search(r"(\d+)$", s)
    return m.group(1) if m else None

children_books['suffix'] = children_books['book_id'].apply(extract_suffix_id)
children_books['purchase_id'] = children_books['suffix'].apply(lambda x: f'purchaseid_{x}' if x is not None else None)

# Merge with grouped reviews
merged = children_books.merge(grp, on='purchase_id', how='left')

# Filter avg_rating >= 4.5 and have at least 1 review
res = merged[merged['avg_rating'].notna() & (merged['avg_rating'] >= 4.5)].copy()

# Prepare output list
output = []
for _, row in res.iterrows():
    output.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'average_rating': round(float(row.get('avg_rating')), 3) if pd.notna(row.get('avg_rating')) else None,
        'review_count': int(row.get('review_count')) if pd.notna(row.get('review_count')) else 0,
        'categories': row.get('categories_parsed')
    })

# Sort by average_rating desc then review_count desc
output = sorted(output, key=lambda x: (-x['average_rating'], -x['review_count']))

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_RFsZuS1899j6AWpQEpqb4B0h': ['review'], 'var_call_Cw1mmm6Dq10hFgi6XAE0NJkB': 'file_storage/call_Cw1mmm6Dq10hFgi6XAE0NJkB.json', 'var_call_DCG44S3NPf1lGMEqdsMCjpiH': ['books_info'], 'var_call_w3Z6TbDgMEr1ZtpmNVhxTv9z': 'file_storage/call_w3Z6TbDgMEr1ZtpmNVhxTv9z.json'}

exec(code, env_args)
