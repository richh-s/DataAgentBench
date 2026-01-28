code = """import json
import pandas as pd

# Load the Literature & Fiction books
books_file = var_functions.query_db:6
if isinstance(books_file, str) and books_file.endswith('.json'):
    with open(books_file, 'r') as f:
        books_data = json.load(f)
else:
    books_data = var_functions.query_db:6

# Load the review averages
reviews_file = var_functions.query_db:8
if isinstance(reviews_file, str) and reviews_file.endswith('.json'):
    with open(reviews_file, 'r') as f:
        reviews_data = json.load(f)
else:
    reviews_data = var_functions.query_db:8

# Convert to DataFrames
books_df = pd.DataFrame(books_data)
reviews_df = pd.DataFrame(reviews_data)

# Filter English books
def is_english(details_str):
    if not details_str:
        return False
    return 'English' in str(details_str)

books_df['is_english'] = books_df['details'].apply(is_english)
english_books = books_df[books_df['is_english']].copy()

# Find books with perfect 5.0 rating
perfect_ratings = reviews_df[reviews_df['avg_rating'] == 5.0].copy()

# Map purchase_id to book_id (they follow pattern: purchaseid_X -> bookid_X)
def map_purchase_to_book(purchase_id):
    try:
        # Extract number from purchase_id
        num = purchase_id.split('_')[1]
        return f'bookid_{num}'
    except:
        return None

perfect_ratings['book_id'] = perfect_ratings['purchase_id'].apply(map_purchase_to_book)

# Merge the datasets
merged = pd.merge(
    english_books,
    perfect_ratings[['book_id', 'avg_rating', 'review_count']],
    on='book_id',
    how='inner'
)

# Format results
result = merged[['book_id', 'title', 'categories', 'details', 'avg_rating', 'review_count']].to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
