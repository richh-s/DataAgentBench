code = """import json, re, os

# Load data
books_path = locals()['var_functions.query_db:22']
reviews_path = locals()['var_functions.query_db:5']

with open(books_path) as f:
    books = json.load(f)
with open(reviews_path) as f:
    reviews = json.load(f)

print('Loaded {} books and {} reviews'.format(len(books), len(reviews)))

# Check ID patterns
book_id_samples = [b['book_id'] for b in books[:10]]
review_id_samples = [r['purchase_id'] for r in reviews[:10]]

print('\nBook ID samples:', book_id_samples)
print('Review purchase_id samples:', review_id_samples)

# Check for exact matches
exact_matches = set(book_id_samples) & set(review_id_samples)
print('\nExact ID matches in samples:', exact_matches)

# Try to extract years more robustly
def extract_year_robust(details):
    if not details or not isinstance(details, str):
        return None
    
    # Look for "released on Month day, year" pattern
    pattern = r'released\s+(?:on\s+)?(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'
    match = re.search(pattern, details, re.I)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Look for "Month day, year" pattern without "released"
    pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+(\d{4})'
    match = re.search(pattern, details, re.I)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Look for "on Month day, year" pattern
    pattern = r'on\s+(?:[A-Za-z]+\s+\d{1,2},\s+)?(\d{4})'
    match = re.search(pattern, details, re.I)
    if match:
        year = int(match.group(1))
        if 1900 <= year <= 2025:
            return year
    
    # Last resort: first 4-digit year between 1900-2025
    pattern = r'\b(19\d{2}|20[0-2]\d)\b'
    match = re.search(pattern, details)
    if match:
        year = int(match.group(1))
        return year
    
    return None

# Try to map all books to decades using exact book_id matching
book_decades_exact = {}
for book in books:
    book_id = book['book_id']
    details = book.get('details', '')
    year = extract_year_robust(details)
    
    if year:
        decade = '{}s'.format((year // 10) * 10)
        book_decades_exact[book_id] = decade

print('\nBooks mapped to decades using exact book_id: {}'.format(len(book_decades_exact)))

# Check exact matches between book IDs and purchase IDs
review_ids = set(r['purchase_id'] for r in reviews)
book_ids = set(book_decades_exact.keys())
exact_common = book_ids & review_ids

print('Books with decades that also have reviews: {}'.format(len(exact_common)))

if not exact_common:
    print('\nNo exact ID matches found. Checking ID patterns...')
    # Check if IDs follow similar patterns
    pattern_counts = {}
    for book_id in book_ids:
        pattern = book_id.rsplit('_', 1)[0] if '_' in book_id else 'no_underscore'
        pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
    
    print('Book ID patterns:', dict(sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True)))
    
    review_pattern_counts = {}
    for review_id in review_ids:
        pattern = review_id.rsplit('_', 1)[0] if '_' in review_id else 'no_underscore'
        review_pattern_counts[pattern] = review_pattern_counts.get(pattern, 0) + 1
    
    print('Review ID patterns:', dict(sorted(review_pattern_counts.items(), key=lambda x: x[1], reverse=True)))

# Try a substring match approach
substring_matches = 0
matched_books = {}
for book_id in book_ids:
    book_num = book_id.split('_')[-1] if '_' in book_id else book_id
    for review_id in review_ids:
        review_num = review_id.split('_')[-1] if '_' in review_id else review_id
        if book_num == review_num:
            substring_matches += 1
            matched_books[book_id] = True
            break

print('\nSubstring ID matches (numbers only): {}'.format(len(matched_books)))

# Output summary for debug
summary = {
    'total_books': len(books),
    'total_reviews': len(reviews),
    'books_with_decades': len(book_decades_exact),
    'exact_id_matches': len(exact_common),
    'substring_id_matches': len(matched_books)
}

print('\nSummary:', summary)
print('__RESULT__:')
print(json.dumps(summary))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'books_with_years': 0, 'total_reviews': 10, 'books_with_reviews': 8, 'books_with_both': 0, 'sample_books': []}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': [{'book_count': '200'}], 'var_functions.execute_python:34': None, 'var_functions.execute_python:56': None, 'var_functions.execute_python:58': {'status': 'debug_done'}, 'var_functions.execute_python:66': None, 'var_functions.execute_python:68': None, 'var_functions.execute_python:70': 'No decade found with at least 10 distinct books', 'var_functions.execute_python:74': None, 'var_functions.query_db:76': [{'details': 'Published by Chatto & Windus, the first edition of this book was released on January 1, 2004. It is written in English and comes in a hardcover format, comprising 196 pages. The book has an ISBN-10 of 0701169850 and an ISBN-13 of 978-0701169855. Weighing 10.1 ounces, its dimensions are 5.39 x 0.71 x 7.48 inches.'}], 'var_functions.query_db:80': [{'total_reviews': '1833'}], 'var_functions.execute_python:82': None, 'var_functions.execute_python:86': None, 'var_functions.query_db:88': [{'purchase_id': 'purchaseid_186'}, {'purchase_id': 'purchaseid_191'}, {'purchase_id': 'purchaseid_190'}, {'purchase_id': 'purchaseid_8'}, {'purchase_id': 'purchaseid_178'}, {'purchase_id': 'purchaseid_76'}, {'purchase_id': 'purchaseid_115'}, {'purchase_id': 'purchaseid_167'}, {'purchase_id': 'purchaseid_188'}, {'purchase_id': 'purchaseid_23'}, {'purchase_id': 'purchaseid_196'}, {'purchase_id': 'purchaseid_3'}, {'purchase_id': 'purchaseid_48'}, {'purchase_id': 'purchaseid_154'}, {'purchase_id': 'purchaseid_99'}, {'purchase_id': 'purchaseid_169'}, {'purchase_id': 'purchaseid_145'}, {'purchase_id': 'purchaseid_194'}, {'purchase_id': 'purchaseid_81'}, {'purchase_id': 'purchaseid_199'}], 'var_functions.execute_python:90': None, 'var_functions.execute_python:92': None}

exec(code, env_args)
