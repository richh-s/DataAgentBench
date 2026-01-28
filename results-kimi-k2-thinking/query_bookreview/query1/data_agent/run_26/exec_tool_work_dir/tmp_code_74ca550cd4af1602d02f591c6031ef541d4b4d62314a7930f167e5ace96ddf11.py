code = """import json
import re

# Load data
books_file = var_functions.query_db:22
reviews_file = var_functions.query_db:5

with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

# Parse publication years
year_map = {}
for b in books:
    details = b.get('details', '')
    year = None
    
    # Pattern: "January 1, 2004"
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(2))
    else:
        # Pattern: "published on May 18, 2014" or "edition on July 1, 2003"
        m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
        if m:
            year = int(m.group(1))
    
    if year and 1900 <= year <= 2025:
        decade = str(year // 10 * 10) + 's'
        year_map[b['book_id']] = decade

# Group reviews by decade
decade_stats = {}
for r in reviews:
    book_id = r['purchase_id']
    if book_id in year_map:
        decade = year_map[book_id]
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += float(r['rating'])
        decade_stats[decade]['count'] += 1

# Filter for decades with >= 10 distinct books
candidates = []
for decade, stats in decade_stats.items():
    if len(stats['books']) >= 10:
        avg = stats['sum'] / stats['count']
        candidates.append((decade, avg, len(stats['books']), stats['count']))

# Find highest average rating
candidates.sort(key=lambda x: x[1], reverse=True)
result = candidates[0] if candidates else None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
