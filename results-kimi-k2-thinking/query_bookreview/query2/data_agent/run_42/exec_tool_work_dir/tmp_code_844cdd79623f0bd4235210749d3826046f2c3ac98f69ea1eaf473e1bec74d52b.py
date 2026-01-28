code = """import json

books_file = locals()['var_functions.query_db:6']
reviews_file = locals()['var_functions.query_db:8']

with open(books_file, 'r') as f:
    books_data = json.load(f)

with open(reviews_file, 'r') as f:
    reviews_data = json.load(f)

# Find English books with Literature & Fiction category and perfect 5.0 rating
english_lit_books = []
for book in books_data:
    # Check English
    details = book.get('details', '')
    if not details or 'English' not in str(details):
        continue
    
    # Already filtered for Literature & Fiction
    is_5_star = False
    book_id = book.get('book_id')
    
    # Check if this book has perfect 5.0 rating
    if book_id:
        # Extract number to map to purchase_id
        try:
            book_num = book_id.split('_')[1]
            purchase_id = f'purchaseid_{book_num}'
            
            for review in reviews_data:
                if review.get('purchase_id') == purchase_id:
                    if float(review.get('avg_rating', 0)) == 5.0:
                        is_5_star = True
                        break
        except:
            pass
    
    if is_5_star:
        english_lit_books.append({
            'book_id': book_id,
            'title': book.get('title'),
            'categories': book.get('categories'),
            'details': details
        })

print('__RESULT__:')
print(json.dumps(english_lit_books, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:22': {'books_type': "<class 'str'>", 'reviews_type': "<class 'str'>"}}

exec(code, env_args)
