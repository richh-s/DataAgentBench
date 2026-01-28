code = """import json
# Read books info
books_file = var_functions.query_db:22
if isinstance(books_file, str):
    with open(books_file) as f:
        books = json.load(f)
else:
    books = books_file
# Read reviews
reviews_file = var_functions.query_db:5
if isinstance(reviews_file, str):
    with open(reviews_file) as f:
        reviews = json.load(f)
else:
    reviews = reviews_file
print('Books loaded:', len(books))
print('Reviews loaded:', len(reviews))
print('__RESULT__:')
print(json.dumps({'books': len(books), 'reviews': len(reviews)}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
