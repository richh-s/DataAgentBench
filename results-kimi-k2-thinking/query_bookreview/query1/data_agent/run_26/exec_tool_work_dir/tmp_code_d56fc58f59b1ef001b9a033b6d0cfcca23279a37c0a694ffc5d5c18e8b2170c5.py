code = """import json, re, os, sys

# Get the stored results using locals() with string keys
books_data = locals()['var_functions.query_db:22']
reviews_data = locals()['var_functions.query_db:5']

# Handle file paths
if isinstance(books_data, str) and os.path.exists(books_data):
    with open(books_data) as f:
        books = json.load(f)
else:
    books = books_data

if isinstance(reviews_data, str) and os.path.exists(reviews_data):
    with open(reviews_data) as f:
        reviews = json.load(f)
else:
    reviews = reviews_data

# Extract publication year from details
def extract_year(details):
    if not details:
        return None
    
    # Pattern: "Month day, year"
    m = re.search(r'[A-Za-z]+\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Pattern: "on ... year"
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})', details)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    return None

# Map books to decades
book_decade = {}
for b in books:
    year = extract_year(b.get('details', ''))
    if year:
        decade = str(year // 10 * 10) + 's'
        book_decade[b['book_id']] = decade

print('Extracted years for', len(book_decade), 'books')

# Group reviews by decade
decade_info = {}
for r in reviews:
    bid = r['purchase_id']
    if bid in book_decade:
        decade = book_decade[bid]
        if decade not in decade_info:
            decade_info[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        decade_info[decade]['books'].add(bid)
        decade_info[decade]['sum'] += float(r['rating'])
        decade_info[decade]['count'] += 1

# Find best decade
best = None
for decade, info in decade_info.items():
    if len(info['books']) >= 10:
        avg = info['sum'] / info['count']
        if not best or avg > best[1]:
            best = (decade, avg, len(info['books']), info['count'])

print('Result:', best)
print('__RESULT__:')
sys.stdout.write(json.dumps(best))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
