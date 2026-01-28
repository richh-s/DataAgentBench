code = """import json
import re
import os

# Load books data
books_path = locals()['var_functions.query_db:22']
with open(books_path) as f:
    books = json.load(f)

# Load reviews data
reviews_path = locals()['var_functions.query_db:5']
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from details
def get_year(details):
    if not details:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        return int(m.group(2))
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if m:
        return int(m.group(1))
    return None

# Add decade to books
for book in books:
    year = get_year(book.get('details', ''))
    book['decade'] = str(year // 10 * 10) + 's' if year else None

# Filter books with decades
books_with_decades = [b for b in books if b['decade'] is not None]
print('Books with decades: {}'.format(len(books_with_decades)))

# Count books per decade
decade_counts = {}
for book in books_with_decades:
    decade = book['decade']
    decade_counts[decade] = decade_counts.get(decade, 0) + 1

print('Books per decade: {}'.format(dict(sorted(decade_counts.items()))))

# Get review book IDs
review_book_ids = set(r['purchase_id'] for r in reviews)
print('Review book IDs: {}'.format(len(review_book_ids)))

# Common books
book_ids = set(b['book_id'] for b in books_with_decades)
common = book_ids & review_book_ids
print('Common books: {}'.format(len(common)))

# Group reviews by decade
from collections import defaultdict
decade_data = defaultdict(lambda: {'books': set(), 'sum': 0.0, 'count': 0})

for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_ids:
        # Find the decade for this book
        book = next(b for b in books_with_decades if b['book_id'] == book_id)
        decade = book['decade']
        rating = float(review['rating'])
        
        decade_data[decade]['books'].add(book_id)
        decade_data[decade]['sum'] += rating
        decade_data[decade]['count'] += 1

print('Decades with reviews: {}'.format(list(decade_data.keys())))

# Find decades with >= 10 books
valid_decades = []
for decade, data in decade_data.items():
    if len(data['books']) >= 10:
        avg = data['sum'] / data['count']
        valid_decades.append((decade, avg, len(data['books']), data['count']))

# Sort by average rating
valid_decades.sort(key=lambda x: x[1], reverse=True)
print('Valid decades (>=10 books): {}'.format(len(valid_decades)))

if valid_decades:
    for i, d in enumerate(valid_decades[:5]):
        print('{}. {}: avg={:.3f}, books={}, reviews={}'.format(i+1, d[0], d[1], d[2], d[3]))

result = valid_decades[0][0] if valid_decades else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books'}

exec(code, env_args)
