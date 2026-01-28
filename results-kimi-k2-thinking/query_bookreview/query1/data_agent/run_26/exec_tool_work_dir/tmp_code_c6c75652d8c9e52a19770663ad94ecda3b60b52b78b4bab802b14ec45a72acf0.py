code = """import json, re, os

# Load data from file paths
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Extract publication year from details
def extract_year(details):
    if not details:
        return None
    
    patterns = [
        r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})',
        r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
        r'\breleased\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details)
        if match:
            try:
                year = int(match.group(1))
                if 1900 <= year <= 2025:
                    return year
            except:
                continue
    
    return None

# Map book to decade
book_decades = {}
for book in books:
    year = extract_year(book.get('details', ''))
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decades[book['book_id']] = decade

print('Books with years extracted: {}'.format(len(book_decades)))

# Group reviews by decade
decade_stats = {}
matches = 0

for review in reviews:
    book_id = review['purchase_id']
    if book_id in book_decades:
        matches += 1
        decade = book_decades[book_id]
        rating = float(review['rating'])
        
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += rating
        decade_stats[decade]['count'] += 1

print('Matched {} reviews across {} decades'.format(matches, len(decade_stats)))

# Find decades with >=10 distinct books and highest avg rating
best_decade = None
best_avg = 0.0

for decade, stats in decade_stats.items():
    if len(stats['books']) >= 10:
        avg = stats['sum'] / stats['count']
        if avg > best_avg:
            best_avg = avg
            best_decade = {
                'decade': decade,
                'avg_rating': round(avg, 3),
                'distinct_books': len(stats['books']),
                'total_reviews': stats['count']
            }

print('Best decade:', best_decade)

# Return just the decade string
result = best_decade['decade'] if best_decade else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}]}

exec(code, env_args)
