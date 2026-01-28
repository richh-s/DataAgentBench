code = """import json, re, os, sys

# Read file paths from the stored results
books_path = var_functions.query_db:22 if isinstance(var_functions.query_db:22, str) else None
reviews_path = var_functions.query_db:5 if isinstance(var_functions.query_db:5, str) else None

# Load the data
if books_path:
    with open(books_path) as f:
        books = json.load(f)
else:
    books = var_functions.query_db:22

if reviews_path:
    with open(reviews_path) as f:
        reviews = json.load(f)
else:
    reviews = var_functions.query_db:5

print('Data loaded:', len(books), 'books,', len(reviews), 'reviews')

# Extract publication year and decade
def extract_decade(details):
    if not details:
        return None
    
    patterns = [
        r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\bin\s+(?:its\s+)?(?:first|second|third|fourth)?\s*(?:edition\s+)?(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b'
    ]
    
    for pat in patterns:
        m = re.search(pat, details, re.I)
        if m:
            year = int(m.groups()[-1])
            if 1900 <= year <= 2025:
                return '{}s'.format(year // 10 * 10)
    
    return None

# Map book_id to decade
book_decades = {}
for book in books:
    decade = extract_decade(book.get('details', ''))
    if decade:
        book_decades[book['book_id']] = decade

print('Books with decade:', len(book_decades))

# Reviews that match books and calculate decade stats
decade_data = {}
matched_reviews = 0
for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_decades:
        matched_reviews += 1
        decade = book_decades[book_id]
        rating = float(review['rating'])
        
        if decade not in decade_data:
            decade_data[decade] = {'books': set(), 'total': 0.0, 'count': 0}
        
        decade_data[decade]['books'].add(book_id)
        decade_data[decade]['total'] += rating
        decade_data[decade]['count'] += 1

print('Matched reviews:', matched_reviews)
print('Decades found:', list(decade_data.keys()))

# Filter decades with >= 10 distinct books
valid_decades = []
for decade, data in decade_data.items():
    if len(data['books']) >= 10:
        avg_rating = data['total'] / data['count']
        valid_decades.append((decade, avg_rating, len(data['books']), data['count']))

# Sort by avg rating descending
valid_decades.sort(key=lambda x: x[1], reverse=True)
print('Valid decades (>=10 books):', len(valid_decades))
print('Top 3:', valid_decades[:3])

# Get top decade
top_decade = valid_decades[0] if valid_decades else None

# Output result as string for return_answer
result_str = None
if top_decade:
    result_str = '{} (average rating: {:.2f}, {} books, {} reviews)'.format(
        top_decade[0], top_decade[1], top_decade[2], top_decade[3]
    )

print('Final result:', result_str)
print('__RESULT__:')"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}}

exec(code, env_args)
