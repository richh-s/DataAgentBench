code = """import json
import pandas as pd

# Load the data files
books_file_path = locals()['var_functions.query_db:6']
reviews_file_path = locals()['var_functions.query_db:14']

with open(books_file_path, 'r') as f:
    books_data = json.load(f)
with open(reviews_file_path, 'r') as f:
    reviews_data = json.load(f)

# Create DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Convert rating to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'])

# Calculate average rating per purchase_id
avg_ratings = reviews_df.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

# Filter for perfect 5.0 average rating
perfect_ratings = avg_ratings[avg_ratings['avg_rating'] == 5.0]

# Map purchase_id to book_id
# purchaseid_123 -> bookid_123
perfect_ratings['book_id'] = perfect_ratings['purchase_id'].str.replace('purchaseid_', 'bookid_')

# Merge with books data
merged_df = pd.merge(perfect_ratings, books_df, on='book_id', how='inner')

# Filter for Literature & Fiction category
lit_fiction_books = merged_df[merged_df['categories'].astype(str).str.contains('Literature & Fiction', case=False, na=False)]

# Prepare results
results = []
for _, row in lit_fiction_books.iterrows():
    # Extract author name if it's a JSON string
    author_info = row['author']
    author_name = 'None'
    if author_info and author_info != 'None':
        try:
            author_json = json.loads(author_info)
            author_name = author_json.get('name', 'Unknown')
        except:
            author_name = str(author_info)
    
    results.append({
        'title': row['title'],
        'author': author_name,
        'book_id': row['book_id'],
        'avg_rating': float(row['avg_rating']),
        'review_count': int(row['review_count'])
    })

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'Ha! On me!  I thought this was a cookbook!'}, {'purchase_id': 'purchaseid_191', 'rating': '4', 'title': 'Four Stars'}, {'purchase_id': 'purchaseid_190', 'rating': '4', 'title': 'A wonderful adventure in France'}, {'purchase_id': 'purchaseid_8', 'rating': '5', 'title': 'Best beginner book.  Been looking for something like this for a long time.'}, {'purchase_id': 'purchaseid_178', 'rating': '4', 'title': 'Referance Guide'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'A Good read for Meat Eaters, and Veggie Heads as well'}, {'purchase_id': 'purchaseid_76', 'rating': '5', 'title': 'Greet book'}, {'purchase_id': 'purchaseid_186', 'rating': '4', 'title': 'For anyone except avid non-hunters.'}, {'purchase_id': 'purchaseid_115', 'rating': '5', 'title': 'Highly recommend this book if you love history of Mid Atlantic wrestling...'}, {'purchase_id': 'purchaseid_167', 'rating': '2', 'title': 'Heroine blames others for things & feels her bad behavior is justified'}], 'var_functions.query_db:12': [{'count': '1833'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
