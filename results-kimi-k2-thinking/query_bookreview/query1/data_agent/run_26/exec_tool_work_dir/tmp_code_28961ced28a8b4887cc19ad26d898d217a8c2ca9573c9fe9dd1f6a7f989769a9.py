code = """import json, re

# Load data
books_file = var_functions.query_db:22
reviews_file = var_functions.query_db:5

with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

# Extract year
def get_year(details):
    if not details:
        return None
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        return int(m.group(2))
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if m:
        return int(m.group(1))
    m = re.search(r'\b(\d{4})\b', details)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    return None

# Prep data
book_years = {b['book_id']: get_year(b['details']) for b in books}
book_decades = {k: '{}s'.format(v // 10 * 10) for k, v in book_years.items() if v}
print('Books with years:', len(book_decades))

# Group reviews
decade_data = {}
for r in reviews:
    pid = r['purchase_id']
    rating = float(r['rating'])
    if pid in book_decades:
        decade = book_decades[pid]
        if decade not in decade_data:
            decade_data[decade] = []
        decade_data[decade].append((pid, rating))

# Filter and compute
candidates = []
for decade, items in decade_data.items():
    books = set(i[0] for i in items)
    if len(books) >= 10:
        ratings = [i[1] for i in items]
        avg = sum(ratings) / len(ratings)
        candidates.append((decade, avg, len(books), len(ratings)))

candidates.sort(key=lambda x: x[1], reverse=True)
print('Top 5:', candidates[:5])
print('__RESULT__:')
print(json.dumps(candidates[0] if candidates else None))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}]}

exec(code, env_args)
