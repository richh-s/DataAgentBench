code = """import json, re

# Load the data from stored file paths
books_path = var_functions.query_db:22
reviews_path = var_functions.query_db:5

# Read directly from the file paths
with open(books_path) as f:
    books_data = json.load(f)
with open(reviews_path) as f:
    reviews_data = json.load(f)

print('Data loaded: {} books, {} reviews'.format(len(books_data), len(reviews_data)))

# Extract publication years from details
def get_decade(details_string):
    if not details_string:
        return None
    
    # Look for "Month day, year" pattern
    m = re.search(r'[A-Za-z]+\s+\d{1,2},\s+(\d{4})', details_string)
    if m:
        year = int(m.group(1))
        return str((year // 10) * 10) + 's'
    
    # Look for "on...year" pattern
    m = re.search(r'\bon\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})\b', details_string)
    if m:
        year = int(m.group(1))
        if 1900 <= year <= 2025:
            return str((year // 10) * 10) + 's'
    
    return None

# Map book_id to decade
book_to_decade = {}
for book in books_data:
    decade = get_decade(book.get('details', ''))
    if decade:
        book_to_decade[book['book_id']] = decade

print('Mapped {} books to decades'.format(len(book_to_decade)))

# Group reviews by decade
decade_stats = {}
for review in reviews_data:
    book_id = review['purchase_id']
    rating = float(review['rating'])
    
    if book_id in book_to_decade:
        decade = book_to_decade[book_id]
        if decade not in decade_stats:
            decade_stats[decade] = {'books': set(), 'sum': 0.0, 'count': 0}
        
        decade_stats[decade]['books'].add(book_id)
        decade_stats[decade]['sum'] += rating
        decade_stats[decade]['count'] += 1

# Filter for decades with >= 10 books and find highest average
best_decade = None
best_avg = 0.0
valid_count = 0

for decade, stats in decade_stats.items():
    num_books = len(stats['books'])
    if num_books >= 10:
        avg_rating = stats['sum'] / stats['count']
        valid_count += 1
        if avg_rating > best_avg:
            best_avg = avg_rating
            best_decade = (decade, avg_rating, num_books, stats['count'])

print('Valid decades:', valid_count)
print('Best decade:', best_decade)

result = best_decade
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None}

exec(code, env_args)
