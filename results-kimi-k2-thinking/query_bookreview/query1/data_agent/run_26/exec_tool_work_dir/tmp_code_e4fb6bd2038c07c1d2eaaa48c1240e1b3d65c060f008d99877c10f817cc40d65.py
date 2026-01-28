code = """import json, re
import pandas as pd

# Load data from the stored file paths
books_file = 'var_functions.query_db:22'
reviews_file = 'var_functions.query_db:5'

# Read files
with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year
def get_pub_year(details):
    if not details:
        return None
    
    # Try pattern: "Month day, year"
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if match:
        return int(match.group(2))
    
    # Try pattern: "on Month day, year" or "on year"
    match = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    return None

# Map book_id to decade
book_decades = {}
for book in books:
    year = get_pub_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decades[book['book_id']] = decade

print('Extracted years for {} books'.format(len(book_decades)))

# Group reviews by decade
from collections import defaultdict
decade_data = defaultdict(lambda: {'books': set(), 'sum': 0.0, 'count': 0})

for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_decades:
        decade = book_decades[book_id]
        decade_data[decade]['books'].add(book_id)
        decade_data[decade]['sum'] += float(review['rating'])
        decade_data[decade]['count'] += 1

# Filter decades with >= 10 books and calculate averages
valid_decades = []
for decade, data in decade_data.items():
    distinct_books = len(data['books'])
    if distinct_books >= 10:
        avg_rating = data['sum'] / data['count']
        valid_decades.append((decade, avg_rating, distinct_books, data['count']))

# Sort by average rating descending
valid_decades.sort(key=lambda x: x[1], reverse=True)

print('Found {} valid decades'.format(len(valid_decades)))
if valid_decades:
    print('Top decade:', valid_decades[0])

result = valid_decades[0] if valid_decades else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
