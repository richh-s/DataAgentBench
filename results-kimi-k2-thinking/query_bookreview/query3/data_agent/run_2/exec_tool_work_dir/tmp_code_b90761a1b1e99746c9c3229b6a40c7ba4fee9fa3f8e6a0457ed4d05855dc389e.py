code = """import json
import pandas as pd

# Load the review data from file (it's stored as a JSON file path)
review_file_path = locals()['var_functions.query_db:5']
with open(review_file_path, 'r') as f:
    reviews_data = json.load(f)

# Load the books data from file
books_file_path = locals()['var_functions.query_db:6']
with open(books_file_path, 'r') as f:
    books_data = json.load(f)

# Convert to DataFrames
reviews_df = pd.DataFrame(reviews_data)
books_df = pd.DataFrame(books_data)

# Filter books that are in 'Children's Books' category
childrens_books_df = books_df[books_df['categories'].str.contains("Children's Books", na=False)]

# Extract numeric ID from purchase_id and book_id for joining
reviews_df['book_numeric_id'] = reviews_df['purchase_id'].str.extract(r'purchaseid_(\d+)')
childrens_books_df['book_numeric_id'] = childrens_books_df['book_id'].str.extract(r'bookid_(\d+)')

# Merge reviews with children's books
merged_df = pd.merge(reviews_df, childrens_books_df, on='book_numeric_id', how='inner', suffixes=('_review', '_book'))

# Convert rating to float
merged_df['rating'] = merged_df['rating'].astype(float)

# Calculate average rating per book
book_ratings = merged_df.groupby('book_id').agg({
    'rating': ['mean', 'count'],
    'title_book': 'first',
    'categories': 'first'
}).reset_index()

# Flatten column names
book_ratings.columns = ['book_id', 'average_rating', 'review_count', 'title', 'categories']

# Filter books with average rating >= 4.5 and at least 1 review
result_df = book_ratings[(book_ratings['average_rating'] >= 4.5) & (book_ratings['review_count'] >= 1)]

# Sort by average rating descending
result_df = result_df.sort_values('average_rating', ascending=False)

# Convert the result to JSON string and print it
result_json = result_df.to_json(orient='records', indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'columns': ['purchase_id', 'title_review', 'rating', 'review_time', 'book_numeric_id', 'book_id', 'title_book', 'categories']}}

exec(code, env_args)
