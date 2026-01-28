code = """import json
import pandas as pd
import ast

# Load data from storage file paths
with open(var_call_BXsPjup4GRltX1vEipJgVIHp, 'r') as f:
    reviews = json.load(f)
with open(var_call_cOtGz7ANw5PnpO8c9HmFf0iH, 'r') as f:
    books = json.load(f)

# DataFrames
df_reviews = pd.DataFrame(reviews)
# Ensure types
df_reviews['rating'] = df_reviews['rating'].astype(float)
# Parse datetimes and filter from 2020-01-01
df_reviews['review_time'] = pd.to_datetime(df_reviews['review_time'], errors='coerce')
df_reviews = df_reviews[df_reviews['review_time'] >= pd.Timestamp('2020-01-01')]

# Map purchase_id to book_id (purchaseid_8 -> bookid_8)
if 'purchase_id' in df_reviews.columns:
    df_reviews['book_id'] = df_reviews['purchase_id'].astype(str).str.replace('purchaseid_', 'bookid_')
else:
    df_reviews['book_id'] = df_reviews.get('book_id', pd.Series(dtype=str))

# Aggregate average rating and count per book_id
agg = df_reviews.groupby('book_id').agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()
agg['avg_rating'] = agg['avg_rating'].round(3)

# Books dataframe
df_books = pd.DataFrame(books)
# Function to detect Children's Books in categories
def has_children_cat(cat_str):
    try:
        parsed = ast.literal_eval(cat_str)
        return "Children's Books" in parsed
    except Exception:
        # fallback to substring
        return "Children's Books" in str(cat_str)

if 'categories' in df_books.columns:
    df_books['is_children'] = df_books['categories'].apply(has_children_cat)
else:
    df_books['is_children'] = False

children_books = df_books[df_books['is_children']]

# Merge aggregated ratings with children books
merged = pd.merge(children_books, agg, on='book_id', how='inner')
# Filter average rating >= 4.5
result = merged[merged['avg_rating'] >= 4.5].copy()
# Sort by avg_rating desc, then review_count desc
result = result.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False])

# Prepare output list
output = []
for _, row in result.iterrows():
    output.append({
        'book_id': row['book_id'],
        'title': row.get('title', None),
        'avg_rating': float(row['avg_rating']),
        'review_count': int(row['review_count'])
    })

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_mEnsxvPivxh8gr3EwHRXDN1g': ['review'], 'var_call_BXsPjup4GRltX1vEipJgVIHp': 'file_storage/call_BXsPjup4GRltX1vEipJgVIHp.json', 'var_call_UBarRFgiDsmo2OZXITJ5mfqL': ['books_info'], 'var_call_cOtGz7ANw5PnpO8c9HmFf0iH': 'file_storage/call_cOtGz7ANw5PnpO8c9HmFf0iH.json'}

exec(code, env_args)
