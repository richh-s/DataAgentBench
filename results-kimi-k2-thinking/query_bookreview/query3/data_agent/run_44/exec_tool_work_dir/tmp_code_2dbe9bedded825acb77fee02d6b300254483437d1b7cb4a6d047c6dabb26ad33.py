code = """import json
import pandas as pd

# Load the children's books data
with open('var_functions.query_db:4', 'r') as f:
    children_books_raw = f.read()
    
# The file contains a single string, not a JSON array
# Let's parse it correctly
import ast
children_books = ast.literal_eval(children_books_raw.strip())

# Create DataFrame for children's books
books_df = pd.DataFrame(children_books)

# Load the reviews data (from 2020 onwards)
with open('var_functions.query_db:5', 'r') as f:
    reviews_data = json.load(f)

# Create DataFrame for reviews
reviews_df = pd.DataFrame(reviews_data)

# Convert rating to float for calculations
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Filter reviews to only include 2020 and later
reviews_df['review_time'] = pd.to_datetime(reviews_df['review_time'])
reviews_2020 = reviews_df[reviews_df['review_time'] >= '2020-01-01'].copy()

# Perform the join: purchase_id (reviews) with book_id (books)
merged_df = reviews_2020.merge(books_df, left_on='purchase_id', right_on='book_id', how='inner')

# Calculate average rating per book
grouped = merged_df.groupby(['book_id', 'title_y']).agg({
    'rating': ['mean', 'count']
}).reset_index()

# Flatten the column names
grouped.columns = ['book_id', 'title', 'avg_rating', 'review_count']

# Filter for books with average rating >= 4.5
high_rated_books = grouped[grouped['avg_rating'] >= 4.5].sort_values('avg_rating', ascending=False)

# Prepare the result list
result_books = high_rated_books[['title', 'avg_rating', 'review_count']].to_dict('records')

# Print in the required format
print('__RESULT__:')
print(json.dumps(result_books, indent=2, default=str))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
