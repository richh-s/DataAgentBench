code = """import json
import pandas as pd
import ast

# Load data from storage-provided JSON file paths
with open(var_call_mHBuaMljJWA7qDkMlkLUv7NL, 'r') as f:
    reviews = json.load(f)
with open(var_call_I66Y4ZxGaVWvQz8bte7GLmev, 'r') as f:
    books = json.load(f)

# Create DataFrames
df_rev = pd.DataFrame(reviews)
df_books = pd.DataFrame(books)

# Keep necessary columns and normalize types
if 'purchase_id' not in df_rev.columns:
    df_rev['purchase_id'] = None
if 'rating' not in df_rev.columns:
    df_rev['rating'] = None
if 'review_time' not in df_rev.columns:
    df_rev['review_time'] = None

df_rev = df_rev[['purchase_id', 'rating', 'review_time']].copy()
# Convert rating to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
# Convert review_time to datetime
df_rev['review_time'] = pd.to_datetime(df_rev['review_time'], errors='coerce')

# Filter reviews from 2020-01-01 onwards
df_rev = df_rev[df_rev['review_time'] >= pd.to_datetime('2020-01-01')]

# Map purchase_id -> book_id by replacing prefix
# Handle None values
df_rev['book_id'] = df_rev['purchase_id'].fillna('').astype(str).str.replace('purchaseid_', 'bookid_', regex=False)

# Group to compute average rating and count per book_id
grp = df_rev.groupby('book_id').agg(avg_rating=('rating', 'mean'), review_count=('rating', 'count')).reset_index()

# Parse categories in books (stored as string representation of list)
def parse_categories(x):
    if pd.isna(x):
        return []
    try:
        val = ast.literal_eval(x)
        if isinstance(val, list):
            return val
        else:
            return []
    except Exception:
        return []

if 'categories' not in df_books.columns:
    df_books['categories'] = '[]'

df_books['categories_list'] = df_books['categories'].apply(parse_categories)

# Filter books that have "Children's Books" in categories
df_children = df_books[df_books['categories_list'].apply(lambda lst: "Children's Books" in lst)].copy()

# Merge children's books with review aggregates
merged = df_children.merge(grp, on='book_id', how='left')

# Filter for average rating >= 4.5 and at least one review in 2020+
result_df = merged[(merged['avg_rating'] >= 4.5) & (merged['review_count'] > 0)].copy()

# Build output
out = []
for _, row in result_df.sort_values(['avg_rating', 'review_count'], ascending=[False, False]).iterrows():
    out.append({
        'book_id': row.get('book_id'),
        'title': row.get('title'),
        'average_rating': None if pd.isna(row.get('avg_rating')) else round(float(row.get('avg_rating')), 3),
        'review_count_2020_onwards': None if pd.isna(row.get('review_count')) else int(row.get('review_count'))
    })

# Print result in required format
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_YZ6NiNFlLvnKc4dEyjarBNJk': ['review'], 'var_call_A4BU90FlZy0yAmgVDaTymuQW': ['books_info'], 'var_call_mHBuaMljJWA7qDkMlkLUv7NL': 'file_storage/call_mHBuaMljJWA7qDkMlkLUv7NL.json', 'var_call_I66Y4ZxGaVWvQz8bte7GLmev': 'file_storage/call_I66Y4ZxGaVWvQz8bte7GLmev.json'}

exec(code, env_args)
