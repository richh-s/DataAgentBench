code = """import json
import pandas as pd

# Check what's in storage
books_key = 'var_functions.query_db:16'
reviews_key = 'var_functions.query_db:14'

books_data = locals()[books_key]
reviews_data = locals()[reviews_key]

# Handle file paths
if isinstance(books_data, str) and '.json' in books_data:
    with open(books_data, 'r') as f:
        books = json.load(f)
else:
    books = books_data

if isinstance(reviews_data, str) and '.json' in reviews_data:
    with open(reviews_data, 'r') as f:
        reviews = json.load(f)
else:
    reviews = reviews_data

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Get average ratings
avg_ratings = df_reviews.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

# Find perfect 5.0 ratings
perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]

# Filter for English Literature & Fiction books
mask = (df_books['details'].str.contains('English', case=False, na=False)) & (df_books['categories'].str.contains('Literature & Fiction', case=False, na=False))
df_books_filtered = df_books[mask].copy()

# Map IDs
df_books_filtered['purchase_id'] = df_books_filtered['book_id'].str.replace('bookid_', 'purchaseid_')

# Merge
result = pd.merge(df_books_filtered, perfect_ratings, on='purchase_id', how='inner')

# Output
output = result[['title', 'book_id', 'categories', 'avg_rating', 'review_count']].to_dict('records')
print('Found', len(output), 'books')
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:3': ['books_info'], 'var_functions.execute_python:8': 'Data structure examined', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
