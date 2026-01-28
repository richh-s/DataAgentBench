code = """import json, re

# The data is stored as lists in the variables
books_json = locals()['var_functions.query_db:20']
reviews_json = locals()['var_functions.query_db:5']

# Check what we actually have
print('Type of books data:', type(books_json))
print('Type of reviews data:', type(reviews_json))
print('Books length:', len(books_json) if hasattr(books_json, '__len__') else 'no len')
print('Reviews length:', len(reviews_json) if hasattr(reviews_json, '__len__') else 'no len')

# For testing, let's work with the preview we saw earlier
# which should be actual list data
if isinstance(books_json, list) and len(books_json) > 0:
    sample_books = books_json
else:
    # Fallback to first 10 from preview
    sample_books = [{'book_id':'bookid_1','details':'Published on January 1, 2004'},{'book_id':'bookid_2','details':'Published on May 20, 1996'}]

if isinstance(reviews_json, list) and len(reviews_json) > 0:
    sample_reviews = reviews_json
else:
    sample_reviews = []

print('Sample books:', [b['book_id'] for b in sample_books[:5]])
print('Sample reviews:', [r['purchase_id'] for r in sample_reviews[:5]] if sample_reviews else 'none')

# Let's try to extract years from the sample
def get_year(details):
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        return int(m.group(2))
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})', details)
    if m:
        return int(m.group(1))
    return None

print('Year extraction test:')
for book in sample_books[:3]:
    y = get_year(book.get('details', ''))
    print(book['book_id'], '->', y, 'from:', book.get('details', '')[:60])

# Count reviews
total_reviews = len(sample_reviews)
print('\nTotal reviews:', total_reviews)
if total_reviews > 0:
    print('Sample ratings:', [float(r['rating']) for r in sample_reviews[:3]])

print('__RESULT__:')
print(json.dumps({
    'books_count': len(sample_books),
    'reviews_count': len(sample_reviews),
    'year_extraction_working': any(get_year(b.get('details','')) for b in sample_books[:10])
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}}

exec(code, env_args)
