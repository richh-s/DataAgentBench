code = """import json, re, os

# Load books data
books_raw = locals()['var_functions.query_db:22']
books_file = books_raw if isinstance(books_raw, str) and os.path.exists(books_raw) else None
books = json.load(open(books_file)) if books_file else (books_raw if isinstance(books_raw, list) else [])

# Load reviews data
reviews_raw = locals()['var_functions.query_db:5']
reviews_file = reviews_raw if isinstance(reviews_raw, str) and os.path.exists(reviews_raw) else None
reviews = json.load(open(reviews_file)) if reviews_file else (reviews_raw if isinstance(reviews_raw, list) else [])

# Extract publication year from details text
def extract_year(details):
    if not details:
        return None
    
    # Try "Month day, year" pattern first
    m = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        return int(m.group(1))
    
    # Try "on ... year" pattern
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if m:
        return int(m.group(1))
    
    return None

# Map books to decades
book_decade = {}
for book in books:
    year = extract_year(book.get('details', ''))
    if year and 1900 <= year <= 2025:
        book_decade[book['book_id']] = str(year // 10 * 10) + 's'

# Group reviews by decade
decade_stats = {}
for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_decade:
        decade = book_decade[book_id]
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += float(review['rating'])
        decade_stats[decade]['count'] += 1

# Find decade with highest average rating (>=10 distinct books)
best_decade = None
best_avg = 0.0
for decade, data in decade_stats.items():
    if len(data['books']) >= 10:
        avg = data['sum'] / data['count']
        if avg > best_avg:
            best_avg = avg
            best_decade = decade

# Create final result
result = {'decade': best_decade, 'avg_rating': round(best_avg, 3)} if best_decade else None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}}

exec(code, env_args)
