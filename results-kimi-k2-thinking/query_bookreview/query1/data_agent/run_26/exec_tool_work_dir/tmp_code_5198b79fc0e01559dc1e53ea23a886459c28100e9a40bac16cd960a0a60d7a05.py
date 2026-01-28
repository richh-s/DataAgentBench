code = """import json, re, os, sys

# Load books data
books_raw = locals()['var_functions.query_db:22']
if isinstance(books_raw, str) and os.path.exists(books_raw):
    with open(books_raw) as f:
        books = json.load(f)
else:
    books = books_raw if isinstance(books_raw, list) else []

# Load reviews data
reviews_raw = locals()['var_functions.query_db:5']
if isinstance(reviews_raw, str) and os.path.exists(reviews_raw):
    with open(reviews_raw) as f:
        reviews = json.load(f)
else:
    reviews = reviews_raw if isinstance(reviews_raw, list) else []

print('Loaded', len(books), 'books and', len(reviews), 'reviews')

# Extract publication year
year_map = {}
for b in books:
    details = b.get('details', '')
    year = None
    m = re.search(r'January|February|March|April|May|June|July|August|September|October|November|December\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(1))
    else:
        m = re.search(r'on\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})', details)
        if m:
            year = int(m.group(1))
    if year and 1900 <= year <= 2025:
        decade = str(year // 10 * 10) + 's'
        year_map[b['book_id']] = decade

print('Extracted years for', len(year_map), 'books')

# Group by decade
decade_data = {}
for r in reviews:
    bid = r['purchase_id']
    if bid in year_map:
        decade = year_map[bid]
        if decade not in decade_data:
            decade_data[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        decade_data[decade]['books'].add(bid)
        decade_data[decade]['sum'] += float(r['rating'])
        decade_data[decade]['count'] += 1

# Find best decade with >=10 books
best = None
for decade, data in decade_data.items():
    if len(data['books']) >= 10:
        avg = data['sum'] / data['count']
        if not best or avg > best[1]:
            best = (decade, round(avg, 3), len(data['books']), data['count'])

print('Result:', best)
print('__RESULT__:')"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}}

exec(code, env_args)
