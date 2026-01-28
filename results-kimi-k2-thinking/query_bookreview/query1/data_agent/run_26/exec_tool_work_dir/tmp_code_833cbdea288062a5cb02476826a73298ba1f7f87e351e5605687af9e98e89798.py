code = """import json
import re
import os

# Read the books data file
books_file = var_functions.query_db:22
with open(books_file, 'r') as f:
    books = json.load(f)

# Read the reviews data file  
reviews_file = var_functions.query_db:5
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# Preview the data structure
print('Books loaded:', len(books))
print('Reviews loaded:', len(reviews))

# Check ID patterns
print('\nBook ID pattern samples:', [b['book_id'] for b in books[:5]])
print('Review purchase_id samples:', [r['purchase_id'] for r in reviews[:5]])

print('__RESULT__:')
print(json.dumps({
    'num_books': len(books),
    'num_reviews': len(reviews),
    'book_id_samples': [b['book_id'] for b in books[:5]],
    'review_id_samples': [r['purchase_id'] for r in reviews[:5]]
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
