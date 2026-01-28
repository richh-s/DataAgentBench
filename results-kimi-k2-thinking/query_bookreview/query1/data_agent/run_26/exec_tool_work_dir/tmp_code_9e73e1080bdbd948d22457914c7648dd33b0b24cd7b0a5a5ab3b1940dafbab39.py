code = """import json, re, os

books_file = var_functions.query_db:22
reviews_file = var_functions.query_db:5

# Load books
if 'json' in str(books_file):
    with open(books_file) as f:
        books = json.load(f)
else:
    books = books_file

# Load reviews
if 'json' in str(reviews_file):
    with open(reviews_file) as f:
        reviews = json.load(f)
else:
    reviews = reviews_file

print('Loaded', len(books), 'books and', len(reviews), 'reviews')

# Extract publication year
year_map = {}
for b in books:
    details = b.get('details', '')
    year = None
    m = re.search(r'[A-Za-z]+\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(1))
    else:
        m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})', details)
        if m:
            year = int(m.group(1))
    if year and 1900 <= year <= 2025:
        decade = str(year // 10 * 10) + 's'
        year_map[b['book_id']] = decade

print('Extracted years for', len(year_map), 'books')

# Group reviews by decade
decade_groups = {}
for r in reviews:
    pid = r['purchase_id']
    if pid in year_map:
        decade = year_map[pid]
        if decade not in decade_groups:
            decade_groups[decade] = {'books': set(), 'sum': 0, 'count': 0}
        decade_groups[decade]['books'].add(pid)
        decade_groups[decade]['sum'] += float(r['rating'])
        decade_groups[decade]['count'] += 1

valid = []
for d, info in decade_groups.items():
    if len(info['books']) >= 10:
        avg = info['sum'] / info['count']
        valid.append((d, avg, len(info['books']), info['count']))

valid.sort(key=lambda x: x[1], reverse=True)

result = valid[0] if valid else None
print('Result:', result)
print('__RESULT__:')
import sys
sys.stdout.write(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
