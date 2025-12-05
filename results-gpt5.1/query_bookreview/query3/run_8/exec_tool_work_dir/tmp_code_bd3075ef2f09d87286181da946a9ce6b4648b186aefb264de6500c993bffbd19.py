code = """import json, pandas as pd, os

# Load full books_info and review data
with open(var_call_OfkIXVnFLM6iKlN9FKT38llC, 'r') as f:
    books = json.load(f)
with open(var_call_ML4zT8RXRV2DyUSlUczlaSgs, 'r') as f:
    reviews = json.load(f)

books_df = pd.DataFrame(books)
reviews_df = pd.DataFrame(reviews)

# Filter Children's Books based on categories string containing "Children's Books"
child_books = books_df[books_df['categories'].str.contains("Children's Books", na=False)].copy()

# Compute average rating per purchase_id from 2020 onward
reviews_df['rating'] = reviews_df['rating'].astype(float)
avg_ratings = reviews_df.groupby('purchase_id', as_index=False)['rating'].mean()

# Fuzzy join: book_id in books_df matches purchase_id in reviews
merged = pd.merge(child_books, avg_ratings, left_on='book_id', right_on='purchase_id', how='inner')

# Filter by average rating >= 4.5
high_rated = merged[merged['rating'] >= 4.5]

# Select distinct book titles
result_titles = sorted(high_rated['title'].unique().tolist())

out = json.dumps(result_titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OfkIXVnFLM6iKlN9FKT38llC': 'file_storage/call_OfkIXVnFLM6iKlN9FKT38llC.json', 'var_call_xhaIWHkJ94Ag6IskRx5Taryg': ['review'], 'var_call_ML4zT8RXRV2DyUSlUczlaSgs': 'file_storage/call_ML4zT8RXRV2DyUSlUczlaSgs.json'}

exec(code, env_args)
