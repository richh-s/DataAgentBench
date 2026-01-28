code = """import json
import re
import os

# Load books data
books_file = var_functions.query_db:22
if isinstance(books_file, str) and '.json' in books_file:
    with open(books_file) as f:
        books = json.load(f)
else:
    books = books_file

# Load reviews data
reviews_file = var_functions.query_db:5
if isinstance(reviews_file, str) and '.json' in reviews_file:
    with open(reviews_file) as f:
        reviews = json.load(f)
else:
    reviews = reviews_file

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Parse publication year
def extract_year(details):
    if not details:
        return None
    patterns = [r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})', r'(?:in\s+its\s+[^0-9]*|published\s+[^0-9]*|edition\s+[^0-9]*)(\d{4})\b']
    for pat in patterns:
        m = re.search(pat, details, re.I)
        if m:
            year = int(m.groups()[-1])
            if 1800 <= year <= 2025:
                return year
    return None

# Build lookup: book_id -> decade
book_decades = {}
year_counts = {}
for b in books:
    year = extract_year(b.get('details', ''))
    if year:
        decade = '{}s'.format(year // 10 * 10)
        book_decades[b['book_id']] = decade
        year_counts[decade] = year_counts.get(decade, 0) + 1

print('Books with parseable years:', len(book_decades))
print('Books per decade:', year_counts)

# Group reviews by book and calculate averages
grouped = {}
for r in reviews:
    pid = r['purchase_id']
    rating = float(r['rating'])
    if pid in book_decades:
        decade = book_decades[pid]
        if decade not in grouped:
            grouped[decade] = {'books': set(), 'ratings': [], 'sum': 0.0, 'count': 0}
        grouped[decade]['books'].add(pid)
        grouped[decade]['ratings'].append(rating)
        grouped[decade]['sum'] += rating
        grouped[decade]['count'] += 1

# Filter decades with at least 10 distinct books
results = []
for decade, data in grouped.items():
    distinct_books = len(data['books'])
    if distinct_books >= 10:
        avg_rating = data['sum'] / data['count']
        results.append((decade, avg_rating, distinct_books, data['count']))

print('Decades with >=10 books:', len(results))
if results:
    results.sort(key=lambda x: x[1], reverse=True)
    print('Top decade:', results[0])

print('__RESULT__:')
print(json.dumps({
    'num_books_with_years': len(book_decades),
    'decades_found': list(grouped.keys()),
    'valid_decades': results,
    'top_decade': results[0] if results else None
}))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}]}

exec(code, env_args)
