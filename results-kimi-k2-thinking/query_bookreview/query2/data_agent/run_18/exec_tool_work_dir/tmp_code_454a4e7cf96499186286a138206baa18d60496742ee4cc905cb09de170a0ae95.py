code = """import json
import pandas as pd

books_file = locals()['var_functions.query_db:20']
with open(books_file, 'r') as f:
    books_lit_fiction = json.load(f)

reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Convert to DataFrames
books_df = pd.DataFrame(books_lit_fiction)
reviews_df = pd.DataFrame(reviews_data)

print('Literature & Fiction books in English:', len(books_df))
print('Columns:', list(books_df.columns))

# Convert ratings to numeric
reviews_df['rating'] = pd.to_numeric(reviews_df['rating'], errors='coerce')

# Calculate average rating per purchase_id
avg_ratings = reviews_df.groupby('purchase_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['purchase_id', 'avg_rating', 'review_count']

# Find books with perfect 5.0 average rating
perfect_books = avg_ratings[avg_ratings['avg_rating'] == 5.0]
print('Books with perfect 5.0 rating:', len(perfect_books))

# Match book_id to purchase_id
matched_books = []
for _, book in books_df.iterrows():
    book_id = book['book_id']
    # Convert bookid_X to purchaseid_X
    if book_id.startswith('bookid_'):
        purchase_id = book_id.replace('bookid_', 'purchaseid_')
        
        # Check if this book has perfect rating
        if purchase_id in perfect_books['purchase_id'].values:
            matched_books.append({
                'book_id': book_id,
                'title': book['title'],
                'subtitle': book.get('subtitle', ''),
                'category': book['categories']
            })

print('Found matching books:', len(matched_books))
for book in matched_books:
    print(book)

# Get full book details for the matching books
if matched_books:
    matching_ids = [book['book_id'] for book in matched_books]
    result_books = books_df[books_df['book_id'].isin(matching_ids)]
    
    # Extract basic info
    final_result = []
    for _, row in result_books.iterrows():
        # Parse authors from JSON-like string
        author_info = row['author']
        author_name = 'Unknown'
        if author_info and author_info != 'None':
            try:
                # Extract author name from string representation or JSON
                if 'name' in str(author_info):
                    import ast
                    author_dict = ast.literal_eval(author_info)
                    if isinstance(author_dict, dict) and 'name' in author_dict:
                        author_name = author_dict['name']
            except:
                # Fallback: try to extract simple name
                if isinstance(author_info, str):
                    author_name = author_info.split(' (')[0]
        
        final_result.append({
            'title': row['title'],
            'author': author_name,
            'subtitle': row.get('subtitle', ''),
            'categories': row['categories']
        })
    
    print('\nFinal formatted result:')
    for b in final_result:
        print(f"Title: {b['title']}, Author: {b['author']}")
else:
    final_result = []

print('__RESULT__:')
print(json.dumps(final_result, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': [], 'var_functions.query_db:18': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
