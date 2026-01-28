code = """import json
import pandas as pd

# Load books data
books_file = locals()['var_functions.query_db:30']
with open(books_file, 'r') as f:
    books_data = json.load(f)

# Load reviews data  
reviews_file = locals()['var_functions.query_db:31']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
df_books = pd.DataFrame(books_data)
df_reviews = pd.DataFrame(reviews_data)

# Convert rating to numeric
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'], errors='coerce')

# Extract numeric IDs for joining
df_books['book_num_id'] = df_books['book_id'].str.extract('(\d+)').astype(int)
df_reviews['purchase_num_id'] = df_reviews['purchase_id'].str.extract('(\d+)').astype(int)

# Join reviews with books
merged = df_reviews.merge(df_books, left_on='purchase_num_id', right_on='book_num_id', how='inner')

# Calculate average rating per book
avg_ratings = merged.groupby(['book_id', 'title', 'author'])['rating'].agg(['mean', 'count']).reset_index()

# Filter for perfect 5.0 rating
perfect_books = avg_ratings[avg_ratings['mean'] == 5.0]
perfect_books = perfect_books[perfect_books['count'] > 0]  # Must have at least 1 review

# Get full book details and add rating info
perfect_book_ids = perfect_books['book_id'].tolist()
result_books = df_books[df_books['book_id'].isin(perfect_book_ids)].copy()

# Merge with rating stats
result_with_ratings = result_books.merge(
    perfect_books[['book_id', 'mean', 'count']], 
    on='book_id', 
    how='inner'
)

# Sort by title
result_with_ratings = result_with_ratings.sort_values('title')

# Prepare clean output
output = []
for _, row in result_with_ratings.iterrows():
    # Parse author JSON if possible
    author_name = "Unknown"
    try:
        if row['author'] and row['author'] != 'None':
            author_info = json.loads(row['author'].replace("'", '"'))
            author_name = author_info.get('name', 'Unknown')
    except:
        author_name = str(row['author'])
    
    output.append({
        'title': row['title'],
        'author': author_name,
        'average_rating': float(row['mean']),
        'review_count': int(row['count'])
    })

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:1': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_191', 'rating': '4'}, {'purchase_id': 'purchaseid_190', 'rating': '4'}, {'purchase_id': 'purchaseid_8', 'rating': '5'}, {'purchase_id': 'purchaseid_178', 'rating': '4'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_76', 'rating': '5'}, {'purchase_id': 'purchaseid_186', 'rating': '4'}, {'purchase_id': 'purchaseid_115', 'rating': '5'}, {'purchase_id': 'purchaseid_167', 'rating': '2'}], 'var_functions.query_db:6': [{'total_books': '200'}], 'var_functions.execute_python:14': {'books_count': 10, 'reviews_count': 10, 'first_book': {'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]', 'description': '[]'}, 'first_review': {'purchase_id': 'purchaseid_186', 'rating': '4'}}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': [{'purchase_id': 'purchaseid_1', 'rating': '4'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '4'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '3'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '4'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_10', 'rating': '5'}, {'purchase_id': 'purchaseid_100', 'rating': '4'}, {'purchase_id': 'purchaseid_100', 'rating': '5'}, {'purchase_id': 'purchaseid_100', 'rating': '1'}, {'purchase_id': 'purchaseid_101', 'rating': '5'}, {'purchase_id': 'purchaseid_101', 'rating': '5'}, {'purchase_id': 'purchaseid_102', 'rating': '3'}, {'purchase_id': 'purchaseid_103', 'rating': '1'}, {'purchase_id': 'purchaseid_103', 'rating': '4'}, {'purchase_id': 'purchaseid_103', 'rating': '5'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:21': 'file_storage/functions.query_db:21.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.list_db:34': ['books_info'], 'var_functions.list_db:35': ['review']}

exec(code, env_args)
