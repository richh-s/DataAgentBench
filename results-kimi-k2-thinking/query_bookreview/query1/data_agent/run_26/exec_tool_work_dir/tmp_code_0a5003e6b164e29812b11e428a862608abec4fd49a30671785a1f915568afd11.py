code = """import json, re, os, sys

# Load the data from the file paths stored in the results
books_result = locals()['var_functions.query_db:22']
reviews_result = locals()['var_functions.query_db:5']

# Read books data from file if it's a path
if isinstance(books_result, str) and os.path.exists(books_result):
    with open(books_result) as f:
        books = json.load(f)
else:
    # If it's not a path, assume it's the data directly
    books = books_result

# Read reviews data from file if it's a path  
if isinstance(reviews_result, str) and os.path.exists(reviews_result):
    with open(reviews_result) as f:
        reviews = json.load(f)
else:
    reviews = reviews_result

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from book details
def extract_pub_year(details_txt):
    if not details_txt:
        return None
    
    # Pattern 1: "January 1, 2004" or "May 20, 1996"
    m = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details_txt)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Pattern 2: "on May 18, 2014" or "on July 1, 2003"
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details_txt)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Pattern 3: "March 20, 1995" (shorter version)
    m = re.search(r'[A-Za-z]+\s+\d{1,2},\s+(\d{4})', details_txt)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
            
    return None

# Map book_id to decade
book_to_decade = {}
for book in books:
    year = extract_pub_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_to_decade[book['book_id']] = decade

print('Extracted publication years for {} books'.format(len(book_to_decade)))

# Group reviews by decade and calculate statistics
decade_stats = {}
for review in reviews:
    book_id = review['purchase_id']
    rating = float(review['rating'])
    
    if book_id in book_to_decade:
        decade = book_to_decade[book_id]
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum_ratings': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum_ratings'] += rating
        decade_stats[decade]['count'] += 1

print('Found reviews for {} decades'.format(len(decade_stats)))

# Filter decades with at least 10 distinct books and find highest average
valid_decades = []
for decade, stats in decade_stats.items():
    distinct_books = len(stats['books'])
    if distinct_books >= 10:
        avg_rating = stats['sum_ratings'] / stats['count']
        valid_decades.append((decade, avg_rating, distinct_books, stats['count']))

# Sort by average rating descending
valid_decades.sort(key=lambda x: x[1], reverse=True)

print('Decades with >=10 books: {}'.format(len(valid_decades)))
if valid_decades:
    print('Top decade: {}'.format(valid_decades[0]))

# Get the top decade result
top_decade = valid_decades[0] if valid_decades else None

# Prepare result for JSON serialization
if top_decade:
    result = {'decade': top_decade[0], 'avg_rating': round(top_decade[1], 3)}
else:
    result = None

print('__RESULT__:')
j = json.dumps(result)
sys.stdout.write(j)"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None}

exec(code, env_args)
