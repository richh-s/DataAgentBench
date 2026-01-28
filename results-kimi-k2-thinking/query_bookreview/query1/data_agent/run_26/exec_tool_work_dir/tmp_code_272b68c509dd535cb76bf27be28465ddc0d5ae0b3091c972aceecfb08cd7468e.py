code = """import json, re

# Load books data
books_path = locals()['var_functions.query_db_22']
reviews_path = locals()['var_functions.query_db_5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

# Extract publication year from details
def get_pub_year(details):
    if not details:
        return None
    
    # Pattern 1: "January 1, 2004"
    match = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if match:
        return int(match.group(2))
    
    # Pattern 2: "on May 18, 2014" or "released on July 1, 2003"
    match = re.search(r'(?:on|in)\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    return None

# Build book_id -> decade mapping
book_decades = {}
year_dist = {}
for book in books:
    year = get_pub_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decades[book['book_id']] = decade
        year_dist[decade] = year_dist.get(decade, 0) + 1

print('Parsed publication years for {} books'.format(len(book_decades)))
print('Decade distribution:', year_dist)

# Group reviews by decade
decade_groups = {}
for review in reviews:
    book_id = review['purchase_id']
    rating = float(review['rating'])
    
    if book_id in book_decades:
        decade = book_decades[book_id]
        if decade not in decade_groups:
            decade_groups[decade] = {'books': set(), 'total_rating': 0.0, 'review_count': 0}
        
        decade_groups[decade]['books'].add(book_id)
        decade_groups[decade]['total_rating'] += rating
        decade_groups[decade]['review_count'] += 1

# Filter decades with >= 10 distinct books and calculate averages
valid_decades = []
for decade, data in decade_groups.items():
    distinct_books = len(data['books'])
    if distinct_books >= 10:
        avg_rating = data['total_rating'] / data['review_count']
        valid_decades.append((decade, avg_rating, distinct_books, data['review_count']))

# Sort by average rating descending
valid_decades.sort(key=lambda x: x[1], reverse=True)

print('Found {} valid decades'.format(len(valid_decades)))
print('Top 3 decades:', valid_decades[:3])

# Return top decade result
top_decade = valid_decades[0] if valid_decades else None
print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
