code = """import json, re, os, sys

# Load the actual data from the stored file paths
books_file = locals()['var_functions.query_db:22']
reviews_file = locals()['var_functions.query_db:5']

with open(books_file) as f:
    books = json.load(f)
with open(reviews_file) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from details
def get_year(details):
    if not details or not isinstance(details, str):
        return None
    
    # Pattern 1: "January 1, 2004"
    m = re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details, re.I)
    if m:
        return int(m.group(2))
    
    # Pattern 2: "on May 18, 2014"
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details, re.I)
    if m:
        return int(m.group(1))
    
    # Pattern 3: any year 1900-2025
    m = re.search(r'\b(19\d{2}|20[0-2]\d)\b', details)
    if m:
        return int(m.group(1))
    
    return None

# Map books to decades with actual data check
count_with_years = 0
book_to_decade = {}
decade_book_counts = {}

for book in books:
    book_id = book.get('book_id')
    details = book.get('details', '')
    year = get_year(str(details))
    
    if year and book_id:
        decade = '{}s'.format((year // 10) * 10)
        book_to_decade[book_id] = decade
        decade_book_counts[decade] = decade_book_counts.get(decade, 0) + 1
        count_with_years += 1

print('Books with extractable years: {}'.format(count_with_years))
print('Book count by decade: {}'.format(dict(sorted(decade_book_counts.items()))))

# Get book IDs that have both decade and reviews
review_book_ids = set(r.get('purchase_id') for r in reviews if r.get('purchase_id'))
book_ids_with_decade = set(book_to_decade.keys())
common_books = book_ids_with_decade & review_book_ids

print('Books with decades: {}'.format(len(book_ids_with_decade)))
print('Books in reviews: {}'.format(len(review_book_ids)))
print('Common books (have both decade and reviews): {}'.format(len(common_books)))

if len(common_books) < 10:
    print('Not enough books with both decade and reviews!')
    print('Sample common book IDs:', list(common_books)[:5])

# Group reviews by decade
decade_stats = {}
for review in reviews:
    book_id = review.get('purchase_id')
    rating_str = review.get('rating', '0')
    
    try:
        rating = float(rating_str)
    except:
        continue
    
    if book_id in book_to_decade:
        decade = book_to_decade[book_id]
        
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += rating
        decade_stats[decade]['count'] += 1

print('\nReview statistics by decade:')
for decade in sorted(decade_stats.keys()):
    stats = decade_stats[decade]
    avg_rating = stats['sum'] / stats['count']
    print('  {}: {} books, {} reviews, avg_rating={:.3f}'.format(
        decade, len(stats['books']), stats['count'], avg_rating))

# Find decades with >= 10 distinct books and highest avg rating
decade_results = []
for decade, stats in decade_stats.items():
    distinct_books = len(stats['books'])
    if distinct_books >= 10:
        avg_rating = stats['sum'] / stats['count']
        decade_results.append((decade, avg_rating, distinct_books, stats['count']))

# Sort by average rating descending
decade_results.sort(key=lambda x: x[1], reverse=True)

print('\nValid decades (>=10 distinct books): {}'.format(len(decade_results)))
if decade_results:
    print('All valid decades sorted by avg rating:')
    for i, (decade, avg, books, reviews) in enumerate(decade_results, 1):
        print('  {}. {}: avg={:.3f}, books={}, reviews={}'.format(i, decade, avg, books, reviews))
    
    top_decade = decade_results[0]
    decade_name = top_decade[0]
    avg_rating = round(top_decade[1], 3)
    print('\nTop decade: {}'.format(decade_name))
    print('Average rating: {}'.format(avg_rating))
else:
    decade_name = None
    avg_rating = None
    print('No decade meets criteria of >= 10 distinct books')

# Return just the decade name
result = decade_name
print('__RESULT__:')
sys.stdout.write(str(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None}

exec(code, env_args)
