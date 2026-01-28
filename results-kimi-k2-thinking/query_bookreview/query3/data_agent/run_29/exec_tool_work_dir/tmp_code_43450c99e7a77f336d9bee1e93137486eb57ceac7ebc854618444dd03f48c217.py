code = """import json
import pandas as pd

# Load the data from the file paths stored in variables
reviews_path = var_functions_query_db_2
books_path = var_functions_query_db_6

# Load reviews data
with open(reviews_path, 'r') as f:
    reviews_data = json.load(f)

# Load books data  
with open(books_path, 'r') as f:
    books_data = json.load(f)

# Create DataFrames
df_reviews = pd.DataFrame(reviews_data)
df_books = pd.DataFrame(books_data)

# Filter for children's books (checking if 'Children's Books' is in categories string)
df_children = df_books[df_books['categories'].str.contains("Children's Books", na=False)].copy()

# Extract numeric IDs for joining
df_children['id_num'] = df_children['book_id'].str.extract(r'(\d+)').astype(int)
df_reviews['id_num'] = df_reviews['purchase_id'].str.extract(r'(\d+)').astype(int)

# Merge reviews with children's books
merged = pd.merge(df_reviews, df_children, on='id_num', how='inner')

# Group by book and calculate average rating
grouped = merged.groupby(['book_id', 'title']).agg({
    'rating': ['mean', 'count']
}).reset_index()

grouped.columns = ['book_id', 'title', 'avg_rating', 'review_count']

# Filter books with avg rating >= 4.5
result = grouped[grouped['avg_rating'] >= 4.5].copy()

# Round the average rating
result['avg_rating'] = result['avg_rating'].round(2)

# Sort by rating and review count
result = result.sort_values(['avg_rating', 'review_count'], ascending=[False, False])

# Prepare output
output = result.to_dict('records') if not result.empty else []

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['books_info'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
