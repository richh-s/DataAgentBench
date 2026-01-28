code = """import json
import pandas as pd

# Load the books data
books_file = var_functions.query_db:16
if isinstance(books_file, str) and '.json' in books_file:
    with open(books_file, 'r') as f:
        books_data = json.load(f)
else:
    books_data = books_file

# Load the reviews data  
reviews_file = var_functions.query_db:14
if isinstance(reviews_file, str) and '.json' in reviews_file:
    with open(reviews_file, 'r') as f:
        reviews_data = json.load(f)
else:
    reviews_data = reviews_file

print('Books loaded:', len(books_data))
print('Reviews loaded:', len(reviews_data))

# Convert to DataFrames
df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Filter books for English language (check details field)
df_books_english = df_books[df_books['details'].str.contains('English', case=False, na=False)]
print('English books:', len(df_books_english))

# Calculate average rating per purchase_id/book_id
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])
avg_ratings = df_reviews.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

# Find books with perfect 5.0 rating
perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]
print('Books with perfect 5.0 rating:', len(perfect_ratings))

# Now match with English Literature & Fiction books
# Map book_id to purchase_id format (bookid_X -> purchaseid_X)
df_books_english['purchase_id'] = df_books_english['book_id'].str.replace('bookid_', 'purchaseid_')

# Merge to find matches
result = pd.merge(df_books_english, perfect_ratings, on='purchase_id', how='inner')
print('Matching English books with perfect rating:', len(result))

# Show results
if len(result) > 0:
    print('\nMatching books:')
    for idx, row in result.iterrows():
        print(f"- {row['title']} (book_id: {row['book_id']}, reviews: {row['review_count']})")
else:
    print('No matching books found')

print('__RESULT__:')
print(result[['title', 'book_id', 'categories', 'avg_rating', 'review_count']].to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:3': ['books_info'], 'var_functions.execute_python:8': 'Data structure examined', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
