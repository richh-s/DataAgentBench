code = """import json, re, os

books_file = 'temp_books_data.json'
reviews_file = 'temp_reviews_data.json'

# For debugging, let's try to load and check what we have
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

if isinstance(books_path, str):
    print('Books path:', books_path[:100])
if isinstance(reviews_path, str):
    print('Reviews path:', reviews_path[:100])

# Try to use the actual data
books = books_path if isinstance(books_path, list) else []
reviews = reviews_path if isinstance(reviews_path, list) else []

print('Books type:', type(books), 'Length:', len(books))
print('Reviews type:', type(reviews), 'Length:', len(reviews))

# Let's create smaller working datasets for testing
sample_books = books[:20] if books else []
sample_reviews = reviews[:50] if reviews else []

# Debug year extraction
def try_extract_year(details):
    if not details:
        return None
    patterns = [
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\b(\d{4})\b'
    ]
    for pat in patterns:
        m = re.search(pat, details)
        if m:
            try:
                year = int(m.groups()[-1])
                if 1900 <= year <= 2025:
                    return year
            except:
                continue
    return None

print('Sample year extraction:')
for i, book in enumerate(sample_books[:3]):
    year = try_extract_year(book.get('details', ''))
    print('Book {}: {} -> {}'.format(book['book_id'], year, book.get('details', '')[:60]))

print('Sample review book IDs:', [r['purchase_id'] for r in sample_reviews[:5]])

# Check ID matching
if sample_books and sample_reviews:
    book_ids = set(b['book_id'] for b in sample_books)
    review_ids = set(r['purchase_id'] for r in sample_reviews)
    common = book_ids & review_ids
    print('Common IDs in samples:', common)

print('__RESULT__:')
print(json.dumps({'status': 'debug_done'}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None}

exec(code, env_args)
