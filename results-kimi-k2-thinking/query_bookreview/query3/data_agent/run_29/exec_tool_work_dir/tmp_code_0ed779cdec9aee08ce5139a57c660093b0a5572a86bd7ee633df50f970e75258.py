code = """import json
import pandas as pd
import re

# Load reviews data from file (reviews from 2020 onwards)
with open(var_functions.query_db:2, 'r') as f:
    reviews_data = json.load(f)

# Load books data from file
with open(var_functions.query_db:6, 'r') as f:
    books_data = json.load(f)

# Convert to DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_books = pd.DataFrame(books_data)

# Filter children's books - check if "Children's Books" is in categories
df_children_books = df_books[df_books['categories'].str.contains("Children's Books", na=False)].copy()

# Extract numeric ID from book_id (e.g., "bookid_4" -> 4)
df_children_books['id_num'] = df_children_books['book_id'].str.extract(r'\d+$').astype(int)

# Extract numeric ID from purchase_id (e.g., "purchaseid_4" -> 4) 
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'\d+$').astype(int)

# Merge reviews with children's books on numeric ID
# We use left join from reviews to keep only books that have reviews
# and then filter to those that are children's books
merged_df = pd.merge(df_reviews, df_children_books, on='id_num', how='inner')

# Group by book and calculate average rating
grouped = merged_df.groupby(['book_id', 'title']).agg({
    'rating': ['mean', 'count']
}).reset_index()

grouped.columns = ['book_id', 'title', 'avg_rating', 'review_count']

# Filter books with average rating >= 4.5
result = grouped[grouped['avg_rating'] >= 4.5].copy()

# Round average rating to 2 decimal places
result['avg_rating'] = result['avg_rating'].round(2)

# Format and sort by rating (descending) then review count (descending)
result = result.sort_values(['avg_rating', 'review_count'], ascending=[False, False])

# Print result in required format
if not result.empty:
    result_dict = result.to_dict('records')
else:
    result_dict = []

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['books_info'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
