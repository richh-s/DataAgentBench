code = """import json
import re
import os

# Helper to load JSON file
books_json = var_functions.query_db:22
if isinstance(books_json, str) and '.json' in books_json:
    with open(books_json) as f:
        books = json.load(f)
else:
    books = books_json

reviews_json = var_functions.query_db:5  
if isinstance(reviews_json, str) and '.json' in reviews_json:
    with open(reviews_json) as f:
        reviews = json.load(f)
else:
    reviews = reviews_json

# Parse publication year from details text
def get_pub_year(details_str):
    if not details_str:
        return None
    patterns = [
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})',
        r'\bin\s+[^0-9]*?(\d{4})\b'
    ]
    for pat in patterns:
        m = re.search(pat, details_str, re.I)
        if m:
            year = int(m.groups()[-1])
            if 1800 <= year <= 2025:
                return year
    return None

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))
print('Sample book IDs:', [b['book_id'] for b in books[:3]])
print('Sample purchase IDs:', [r['purchase_id'] for r in reviews[:3]])

print('__RESULT__:')
print(json.dumps({
    'books': len(books),
    'reviews': len(reviews),
    'sample_book': books[0]['book_id'] if books else None,
    'sample_review': reviews[0]['purchase_id'] if reviews else None
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}]}

exec(code, env_args)
