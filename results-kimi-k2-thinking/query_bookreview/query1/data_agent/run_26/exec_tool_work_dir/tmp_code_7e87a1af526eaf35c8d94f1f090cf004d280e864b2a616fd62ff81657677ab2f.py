code = """import json, re, os

# Load data
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract numeric ID from book_id and purchase_id
def get_numeric_id(id_str):
    m = re.search(r'(\d+)$', id_str)
    return int(m.group(1)) if m else None

# Map numeric IDs to decades
numeric_to_decade = {}
for book in books:
    book_id = book['book_id']
    num_id = get_numeric_id(book_id)
    
    # Extract year from details
    details = book.get('details', '')
    year = None
    
    # Try multiple patterns for year extraction
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(2))
    else:
        m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
        if m:
            year = int(m.group(1))
    
    if year and 1900 <= year <= 2025:
        decade = '{}s'.format((year // 10) * 10)
        numeric_to_decade[num_id] = decade

print('Mapped {} books to decades by numeric ID'.format(len(numeric_to_decade)))
print('Sample mapping:', list(numeric_to_decade.items())[:5])

# Group reviews by decade using numeric ID mapping
decade_stats = {}
matched_reviews = 0

for review in reviews:
    purchase_id = review['purchase_id']
    num_id = get_numeric_id(purchase_id)
    rating = float(review['rating'])
    
    if num_id in numeric_to_decade:
        matched_reviews += 1
        decade = numeric_to_decade[num_id]
        
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(num_id)
        decade_stats[decade]['sum'] += rating
        decade_stats[decade]['count'] += 1

print('Matched {} reviews to books with publication years'.format(matched_reviews))
print('Decades with reviews: {}'.format(list(decade_stats.keys())))

# Calculate average ratings for decades with >= 10 books
decade_averages = []
for decade, stats in decade_stats.items():
    distinct_books = len(stats['books'])
    if distinct_books >= 10:
        avg_rating = stats['sum'] / stats['count']
        decade_averages.append((decade, avg_rating, distinct_books, stats['count']))

# Sort by average rating descending
decade_averages.sort(key=lambda x: x[1], reverse=True)

print('Decades with >= 10 distinct books: {}'.format(len(decade_averages)))
for i, (decade, avg, books, reviews) in enumerate(decade_averages, 1):
    print('{}. {}: avg={:.3f}, books={}, reviews={}'.format(i, decade, avg, books, reviews))

# Get top decade
top_decade = decade_averages[0][0] if decade_averages else None
print('Top decade: {}'.format(top_decade))

# Return result
print('__RESULT__:')
print(json.dumps(top_decade))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}]}

exec(code, env_args)
