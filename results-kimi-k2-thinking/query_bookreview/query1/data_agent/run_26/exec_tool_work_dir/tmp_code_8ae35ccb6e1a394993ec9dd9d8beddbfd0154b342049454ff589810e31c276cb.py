code = """import json, re, os, sys

# Load the file paths from stored results
books_path_key = 'var_functions.query_db:22'
reviews_path_key = 'var_functions.query_db:5'

books_result = locals()[books_path_key]
reviews_result = locals()[reviews_path_key]

# Load the actual data from files
with open(books_result) as f:
    books = json.load(f)
with open(reviews_result) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from book details
def extract_year(details):
    if not details or not isinstance(details, str):
        return None
    
    # Look for patterns like "January 1, 2004" or "May 20, 1996"
    patterns = [
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details, re.I)
        if match:
            year = int(match.group(1))
            if 1900 <= year <= 2025:
                return year
    
    return None

# Map book_id to decade
book_to_decade = {}
for book in books:
    year = extract_year(book.get('details', ''))
    if year:
        book_to_decade[book['book_id']] = '{}s'.format((year // 10) * 10)

print('Books with publication years: {}'.format(len(book_to_decade)))

# Group reviews by decade
decade_stats = {}
for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_to_decade:
        decade = book_to_decade[book_id]
        rating = float(review['rating'])
        
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += rating
        decade_stats[decade]['count'] += 1

# Calculate averages and filter for >= 10 books
decade_avg = []
for decade, stats in decade_stats.items():
    if len(stats['books']) >= 10:
        avg = stats['sum'] / stats['count']
        decade_avg.append((decade, avg, len(stats['books']), stats['count']))

# Sort by average rating descending
decade_avg.sort(key=lambda x: x[1], reverse=True)

print('Valid decades: {}'.format(len(decade_avg)))
for d in decade_avg:
    print(' {}: avg={:.3f}, books={}'.format(d[0], d[1], d[2]))

result = decade_avg[0][0] if decade_avg else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None}

exec(code, env_args)
