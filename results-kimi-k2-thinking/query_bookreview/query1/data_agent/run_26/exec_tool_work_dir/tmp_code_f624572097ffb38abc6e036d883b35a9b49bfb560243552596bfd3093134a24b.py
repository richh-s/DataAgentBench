code = """import json, re, os

# Load data from the stored file paths
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from book details
def get_pub_year(details):
    if not details or not isinstance(details, str):
        return None
    
    # Pattern 1: "January 1, 2004" or "May 20, 1996"  
    m = re.search(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})', details)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Pattern 2: "on May 18, 2014"
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return year
    
    return None

# Map books to decades
book_decades = {}
decade_counts = {}
for book in books:
    year = get_pub_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decades[book['book_id']] = decade
        decade_counts[decade] = decade_counts.get(decade, 0) + 1

print('Books with publication years:', len(book_decades))
print('Book distribution by decade:')
for decade in sorted(decade_counts.keys()):
    print('  {}: {} books'.format(decade, decade_counts[decade]))

# Check book ID mapping between books and reviews
review_book_ids = set(r['purchase_id'] for r in reviews)
book_ids = set(book_decades.keys())
common_ids = book_ids & review_book_ids

print('\nBook ID matching:')
print('  Books with years:', len(book_ids))
print('  Books in reviews:', len(review_book_ids))
print('  Common books:', len(common_ids))

if common_ids:
    print('  Sample common IDs:', list(common_ids)[:5])

# Group reviews by decade (only matching books)
decade_review_stats = {}
for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_decades:
        decade = book_decades[book_id]
        rating = float(review['rating'])
        
        if decade not in decade_review_stats:
            decade_review_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_review_stats[decade]['books'].add(book_id)
        decade_review_stats[decade]['sum'] += rating
        decade_review_stats[decade]['count'] += 1

print('\nReviews grouped by decade:')
for decade in sorted(decade_review_stats.keys()):
    stats = decade_review_stats[decade]
    avg = stats['sum'] / stats['count']
    print('  {}: {} books, {} reviews, avg={:.3f}'.format(
        decade, len(stats['books']), stats['count'], avg))

# Now find top decade with >= 10 books
decade_averages = []
for decade, stats in decade_review_stats.items():
    if len(stats['books']) >= 10:
        avg_rating = stats['sum'] / stats['count']
        decade_averages.append((decade, avg_rating, len(stats['books']), stats['count']))

decade_averages.sort(key=lambda x: x[1], reverse=True)

print('\nTop decades (>=10 books):')
for i, (decade, avg, books, reviews) in enumerate(decade_averages[:5], 1):
    print('  {}. {}: avg={:.3f}, {} books, {} reviews'.format(i, decade, avg, books, reviews))

top_decade = decade_averages[0] if decade_averages else None

if top_decade:
    final_answer = '{} (average rating: {:.3f}, {} books, {} reviews)'.format(
        top_decade[0], top_decade[1], top_decade[2], top_decade[3])
else:
    final_answer = 'No decade found with at least 10 distinct books that have reviews'

print('\nFinal answer:', final_answer)

result = {'answer': final_answer, 'top_decade': top_decade}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books'}

exec(code, env_args)
