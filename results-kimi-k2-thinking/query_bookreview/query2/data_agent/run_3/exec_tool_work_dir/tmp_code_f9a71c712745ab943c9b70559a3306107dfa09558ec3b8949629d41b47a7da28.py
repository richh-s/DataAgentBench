code = """import json
import pandas as pd

# Load books data
books_path = var_functions.query_db:16
if isinstance(books_path, str) and '.json' in books_path:
    with open(books_path, 'r') as f:
        books = json.load(f)
else:
    books = books_path

# Load reviews data
reviews_path = var_functions.query_db:14
if isinstance(reviews_path, str) and '.json' in reviews_path:
    with open(reviews_path, 'r') as f:
        reviews = json.load(f)
else:
    reviews = reviews_path

# Create DataFrames
df_books = pd.DataFrame(books)
df_reviews = pd.DataFrame(reviews)

# Convert ratings to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per purchase_id
avg_ratings = df_reviews.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

# Find perfect 5.0 ratings
perfect = avg_ratings[avg_ratings['avg_rating'] == 5.0]

# Filter English books in Literature & Fiction
df_books['is_english'] = df_books['details'].str.contains('English', case=False, na=False)
english_books = df_books[df_books['is_english']]

# Map book_id to purchase_id format
english_books['purchase_id'] = english_books['book_id'].str.replace('bookid_', 'purchaseid_')

# Find matches
matches = pd.merge(english_books, perfect, on='purchase_id', how='inner')

# Prepare result
result = matches[['title', 'book_id', 'categories', 'avg_rating', 'review_count']]
result_list = result.to_dict('records')

print('Books with perfect 5.0 rating:', len(result_list))
print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:3': ['books_info'], 'var_functions.execute_python:8': 'Data structure examined', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
