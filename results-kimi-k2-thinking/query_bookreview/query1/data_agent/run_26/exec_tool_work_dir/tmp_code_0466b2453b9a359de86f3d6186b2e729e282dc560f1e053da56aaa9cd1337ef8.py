code = """import json, re, os, sys

# Load books data from the stored file path
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

# Load data from files
with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from book details using regex
def get_publication_year(details):
    if not details or not isinstance(details, str):
        return None
    
    patterns = [
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\b(\d{4})\b'  # Last resort: any 4-digit year
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details)
        if match:
            year = int(match.group(1))
            if 1900 <= year <= 2025:
                return year
    
    return None

# Create mapping from book_id to decade
book_decade_mapping = {}
year_distribution = {}

for book in books:
    if 'book_id' not in book:
        continue
    year = get_publication_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decade_mapping[book['book_id']] = decade
        year_distribution[decade] = year_distribution.get(decade, 0) + 1

print('Extracted publication years for {} books'.format(len(book_decade_mapping)))
print('Book count by decade:', dict(sorted(year_distribution.items())))

# Get distinct book IDs from reviews
review_book_ids = set()
for review in reviews:
    if 'purchase_id' in review:
        review_book_ids.add(review['purchase_id'])

print('Number of distinct books in reviews: {}'.format(len(review_book_ids)))

# Find books that exist in both books and reviews
common_book_ids = set(book_decade_mapping.keys()) & review_book_ids
print('Books with both publication year and reviews: {}'.format(len(common_book_ids)))

if common_book_ids:
    print('Sample common book IDs:', list(common_book_ids)[:5])

# Group reviews by decade and calculate statistics
decade_statistics = {}
for review in reviews:
    book_id = review.get('purchase_id', '')
    if book_id in common_book_ids:
        decade = book_decade_mapping[book_id]
        rating = float(review.get('rating', 0))
        
        if decade not in decade_statistics:
            decade_statistics[decade] = {'books': set(), 'sum_ratings': 0.0, 'count': 0}
        
        decade_statistics[decade]['books'].add(book_id)
        decade_statistics[decade]['sum_ratings'] += rating
        decade_statistics[decade]['count'] += 1

print('Decades with review data:', list(decade_statistics.keys()))

# Filter for decades with at least 10 distinct books and calculate average ratings
decade_results = []
for decade, stats in decade_statistics.items():
    distinct_book_count = len(stats['books'])
    if distinct_book_count >= 10:
        avg_rating = stats['sum_ratings'] / stats['count']
        decade_results.append({
            'decade': decade,
            'avg_rating': round(avg_rating, 3),
            'distinct_books': distinct_book_count,
            'total_reviews': stats['count']
        })

# Sort by average rating descending
decade_results.sort(key=lambda x: x['avg_rating'], reverse=True)

print('Valid decades (>=10 books): {}'.format(len(decade_results)))
if decade_results:
    print('All valid decades:')
    for result in decade_results:
        print('  {}'.format(result))
    
    top_result = decade_results[0]
    print('Top decade:', top_result)
else:
    print('No decades found with >= 10 distinct books')
    top_result = None

# Create final answer string
if top_result:
    final_answer = '{} (average rating: {}, {} books, {} reviews)'.format(
        top_result['decade'], 
        top_result['avg_rating'],
        top_result['distinct_books'],
        top_result['total_reviews']
    )
else:
    final_answer = 'No decade found with at least 10 distinct books'

print('Final answer:', final_answer)
print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None}

exec(code, env_args)
