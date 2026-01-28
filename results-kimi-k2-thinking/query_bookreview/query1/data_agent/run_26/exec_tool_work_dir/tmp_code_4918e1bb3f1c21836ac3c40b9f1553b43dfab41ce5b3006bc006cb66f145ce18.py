code = """import json, re, os

# Load books data
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract numeric ID from book/purchase IDs
def get_numeric_id(id_str):
    if not id_str:
        return None
    match = re.search(r'(\d+)$', id_str)
    return int(match.group(1)) if match else None

# Extract publication year from book details
def extract_year(details):
    if not details or not isinstance(details, str):
        return None
    
    # Try "Month day, year" pattern
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details, re.I)
    if m:
        year = int(m.group(2))
        if 1900 <= year <= 2025:
            return year
    
    # Try "on ... year" pattern
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details, re.I)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Try any 4-digit year
    m = re.search(r'\b(19\d{2}|20[0-2]\d)\b', details)
    if m:
        return int(m.group(1))
    
    return None

# Map numeric book IDs to decades
numeric_id_to_decade = {}
books_with_years = 0

for book in books:
    book_id = book.get('book_id')
    details = book.get('details', '')
    
    year = extract_year(details)
    if year:
        decade = '{}s'.format((year // 10) * 10)
        numeric_id = get_numeric_id(book_id)
        if numeric_id:
            numeric_id_to_decade[numeric_id] = decade
            books_with_years += 1

print('Books with extractable years: {}'.format(books_with_years))
print('Sample mapping (numeric_id -> decade):', list(numeric_id_to_decade.items())[:5])

# Group reviews by decade using numeric ID matching
decade_stats = {}
matched_review_count = 0

for review in reviews:
    purchase_id = review.get('purchase_id')
    rating_str = review.get('rating', '0')
    
    try:
        rating = float(rating_str)
    except:
        continue
    
    numeric_id = get_numeric_id(purchase_id)
    if numeric_id and numeric_id in numeric_id_to_decade:
        matched_review_count += 1
        decade = numeric_id_to_decade[numeric_id]
        
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum_ratings': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(numeric_id)
        decade_stats[decade]['sum_ratings'] += rating
        decade_stats[decade]['count'] += 1

print('Matched {} reviews to books with publication years'.format(matched_review_count))
print('Decades found: {}'.format(list(decade_stats.keys())))

# Filter decades with >= 10 distinct books and find highest average rating
decade_averages = []
for decade, stats in decade_stats.items():
    distinct_books = len(stats['books'])
    if distinct_books >= 10:
        avg_rating = stats['sum_ratings'] / stats['count']
        decade_averages.append((decade, avg_rating, distinct_books, stats['count']))

# Sort by average rating descending
decade_averages.sort(key=lambda x: x[1], reverse=True)

print('Decades with >= 10 distinct books: {}'.format(len(decade_averages)))
for i, (decade, avg, books, reviews) in enumerate(decade_averages, 1):
    print('{}. {}: avg={:.3f}, books={}, reviews={}'.format(i, decade, avg, books, reviews))

# Get the top decade
top_decade = decade_averages[0][0] if decade_averages else None
print('Top decade: {}'.format(top_decade))
print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}], 'var_functions.execute_python:90': None}

exec(code, env_args)
