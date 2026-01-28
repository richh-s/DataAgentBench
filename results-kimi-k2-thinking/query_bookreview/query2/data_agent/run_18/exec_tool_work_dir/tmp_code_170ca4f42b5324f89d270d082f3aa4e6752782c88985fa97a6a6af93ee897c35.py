code = """import json
import pandas as pd

books_file = locals()['var_functions.query_db:20']
with open(books_file, 'r') as f:
    books_data = json.load(f)

reviews_file = locals()['var_functions.query_db:6']
with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

books = pd.DataFrame(books_data)
reviews = pd.DataFrame(reviews_data)

reviews['rating'] = pd.to_numeric(reviews['rating'])
avg_ratings = reviews.groupby('purchase_id')['rating'].mean().reset_index()

# Get perfect 5.0 ratings
perfect_ids = avg_ratings[avg_ratings['rating'] == 5.0]['purchase_id'].tolist()

# Create mapping: purchaseid_X -> X
perfect_numbers = [pid.replace('purchaseid_', '') for pid in perfect_ids]

# Find matching books
matching_books = []
for _, book in books.iterrows():
    book_id = book['book_id']
    num = book_id.replace('bookid_', '')
    if num in perfect_numbers:
        # Parse author
        author_info = book['author']
        author = 'Unknown'
        if pd.notna(author_info) and author_info != 'None':
            try:
                import ast
                author_dict = ast.literal_eval(author_info)
                if isinstance(author_dict, dict) and 'name' in author_dict:
                    author = author_dict['name']
            except:
                author = str(author_info)
        
        matching_books.append({
            'title': book['title'],
            'author': author,
            'subtitle': str(book.get('subtitle', '')),
            'categories': book['categories']
        })

print('Matching books found:', len(matching_books))
print('__RESULT__:')
print(json.dumps(matching_books, indent=2))"""

env_args = {'var_functions.list_db:0': ['books_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['review'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': [], 'var_functions.query_db:18': [{'book_id': 'bookid_1', 'title': 'Chaucer', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_9', 'title': 'Reunion: The Children of Lauderdale Park', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_13', 'title': 'Girl Made of Glass', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_30', 'title': 'Sugary Sweets (A Taste of Love Series)', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_36', 'title': 'Therapy Mammals', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_37', 'title': "A Most Dangerous Book: Tacitus's Germania from the Roman Empire to the Third Reich", 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}, {'book_id': 'bookid_38', 'title': 'The Prophet: With Original 1923 Illustrations by the Author', 'categories': '["Books", "Literature & Fiction", "Poetry"]'}, {'book_id': 'bookid_39', 'title': 'The Melancholy Strumpet Master', 'categories': '["Books", "Literature & Fiction", "Humor & Satire"]'}, {'book_id': 'bookid_44', 'title': 'Reptilian', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]'}, {'book_id': 'bookid_49', 'title': 'Primeval: A Journal of the Uncanny - Issue #1', 'categories': '["Books", "Literature & Fiction", "History & Criticism"]'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
